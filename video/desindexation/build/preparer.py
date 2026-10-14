"""Prépare les données calculées du montage à partir de la voix et de sa transcription.

- compositions/presentateur.html : le personnage, avec la bouche calée sur l'enveloppe de la voix
  (image par image, 30 i/s), les clignements, les hochements en début de phrase et les sourcils.
- assets/musique.wav et assets/sting-open.wav : via build/musique.py, aux durées du montage.

Usage (depuis video/desindexation) : python3 build/preparer.py
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))
import montage as M  # repères temporels partagés avec la composition

FPS = 30
SR = 16000


def voix_globale():
    """Rejoue la voix sur la timeline finale (coupe pour l'ouverture, réplique de fin décalée)."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(ROOT / "assets/voix.mp3"), "-ar", str(SR), "-ac", "1", "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    v = np.frombuffer(raw, dtype=np.float32)
    out = np.zeros(int(M.TOTAL * SR) + SR, dtype=np.float32)
    for g_start, m_start, dur in M.VOIX:
        a, b = int(m_start * SR), int((m_start + dur) * SR)
        seg = v[a:b]
        o = int(g_start * SR)
        out[o:o + len(seg)] += seg
    return out


def niveaux_bouche(sig):
    hop = SR // FPS
    n = len(sig) // hop
    rms = np.sqrt(np.mean(sig[: n * hop].reshape(n, hop) ** 2, axis=1))
    rms = np.convolve(rms, [0.25, 0.5, 0.25], mode="same")
    voiced = rms[rms > 0.02 * rms.max()]
    seuil0 = 0.08 * rms.max()
    q1, q2 = np.percentile(voiced, [40, 75])
    lv = np.where(rms < seuil0, 0, np.where(rms < q1, 1, np.where(rms < q2, 2, 3)))
    # une forme tenue moins de deux images sautille : on la fusionne avec la précédente
    for i in range(1, n - 1):
        if lv[i] != lv[i - 1] and lv[i] != lv[i + 1]:
            lv[i] = lv[i - 1]
    changes, prev = [], -1
    for i, l in enumerate(lv):
        t = i / FPS
        visible = any(a <= t < b for a, b in M.PRESENTATEUR_VISIBLE)
        l = int(l) if visible else 0
        if l != prev:
            changes.append([round(t, 3), l])
            prev = l
    return changes


def debuts_de_phrase():
    d = json.load(open(ROOT / "transcript.json"))
    starts = []
    for s in d:
        g = M.global_time(s["start"])
        if g is not None and any(a + 0.3 <= g < b for a, b in M.PRESENTATEUR_VISIBLE):
            starts.append(round(g, 2))
    return starts


TEMPLATE = (ROOT / "build/presentateur.template.html").read_text()


def main():
    sig = voix_globale()
    mouth = niveaux_bouche(sig)
    nods = debuts_de_phrase()
    blinks, t = [], 1.3
    k = 0
    while t < M.TOTAL:
        blinks.append(round(t, 2))
        t += [3.7, 4.6, 2.9, 5.1, 4.2][k % 5]
        k += 1
    svg = (ROOT / "assets/presentateur.svg").read_text()
    svg = svg[svg.index("<svg"):]
    html = (TEMPLATE
            .replace("/*MOUTH*/[]", json.dumps(mouth, separators=(",", ":")))
            .replace("/*NODS*/[]", json.dumps(nods))
            .replace("/*BLINKS*/[]", json.dumps(blinks))
            .replace("/*BROWS*/[]", json.dumps(M.SOURCILS))
            .replace("/*POSES*/{}", json.dumps(M.POSES))
            .replace("<!--SVG-->", svg))
    (ROOT / "compositions/presentateur.html").write_text(html)
    cues = {"total": M.TOTAL, "sections": M.SECTIONS_MUSIQUE}
    (ROOT / "build/cues-musique.json").write_text(json.dumps(cues))
    subprocess.run([sys.executable, str(ROOT / "build/musique.py"), str(ROOT / "build/cues-musique.json"), str(ROOT / "assets")], check=True)
    print(f"bouche : {len(mouth)} changements, {len(nods)} hochements, {len(blinks)} clignements")


if __name__ == "__main__":
    main()
