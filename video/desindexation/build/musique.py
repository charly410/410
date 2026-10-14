"""Fond musical original et habillage sonore de l'ouverture, synthétisés de zéro (numpy).

Aucun échantillon externe : la musique est libre de droits puisqu'elle est créée ici.
Usage : python3 build/musique.py build/cues.json assets/
Écrit assets/musique.mp3 (toute la vidéo) et assets/sting-open.wav (ouverture, 2,6 s).
Le rendu est déterministe : bruit tiré d'un générateur à graine fixe.
"""
import json, os, subprocess, sys, wave
import numpy as np

SR = 44100
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
rng = np.random.default_rng(410)


def note(n):  # numéro MIDI vers fréquence
    return 440.0 * 2 ** ((n - 69) / 12)


def lowpass_fast(x, fc):
    # passe-bas à un pôle appliqué deux fois (12 dB/oct), par réponse impulsionnelle tronquée et convolution FFT
    a = np.exp(-2 * np.pi * fc / SR)
    n = int(SR * 0.02)
    h = (1 - a) * a ** np.arange(n)
    h = np.convolve(h, h)
    return fftconv(x, h)[: len(x)]


def fftconv(x, h):
    n = len(x) + len(h) - 1
    N = 1 << (n - 1).bit_length()
    return np.fft.irfft(np.fft.rfft(x, N) * np.fft.rfft(h, N), N)[:n]


def reverb(x, seconds=2.2, mix=0.25):
    n = int(SR * seconds)
    t = np.arange(n) / SR
    ir = rng.standard_normal(n) * np.exp(-t * 6.9 / seconds)
    ir = lowpass_fast(ir, 3500)
    ir /= np.sqrt(np.sum(ir ** 2))
    wet = fftconv(x, ir)[: len(x)]
    return (1 - mix) * x + mix * wet


def env(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


def saw(f, t, detune=0.0):
    out = 0
    for k in range(1, 12):  # dent de scie à bande limitée
        if f * k > 9000:
            break
        out = out + np.sin(2 * np.pi * f * (1 + detune) * k * t) / k
    return out


# Progression la mineur : Am  F  C  G  (vi IV I V en do), deux mesures par accord
CHORDS = [
    (57, [57, 60, 64, 69]),  # Am
    (53, [53, 57, 60, 65]),  # F
    (48, [55, 60, 64, 67]),  # C
    (55, [55, 59, 62, 67]),  # G
]


def compose(total, sections):
    n = int(total * SR)
    t_all = np.arange(n) / SR
    pad = np.zeros(n); pluck = np.zeros(n); bass = np.zeros(n); drums = np.zeros(n)
    chord_len = 2 * BAR
    k = 0
    start = 0.0
    while start < total:
        root, tones = CHORDS[k % 4]
        a, b = int(start * SR), min(n, int((start + chord_len + 0.4) * SR))
        t = np.arange(b - a) / SR
        p = sum(saw(note(m), t, 0.003) + saw(note(m), t, -0.004) for m in tones) / 8
        pad[a:b] += p * env(b - a, 0.6, 0.5)
        # basse : fondamentale sur les temps 1 et 3
        for beat in range(0, 8, 2):
            s = start + beat * BEAT
            if s >= total:
                break
            a2, b2 = int(s * SR), min(n, int((s + 2 * BEAT) * SR))
            tb = np.arange(b2 - a2) / SR
            bass[a2:b2] += (np.sin(2 * np.pi * note(root - 12) * tb) + 0.25 * np.sin(2 * np.pi * note(root) * tb)) * np.exp(-tb * 1.8) * env(b2 - a2, 0.01, 0.08)
        # arpège en croches
        arp = tones + [tones[1] + 12]
        for step in range(16):
            s = start + step * BEAT / 2
            if s >= total:
                break
            m = arp[[0, 2, 1, 3, 4, 2, 3, 1][step % 8]] + 12
            a3, b3 = int(s * SR), min(n, int((s + 0.9) * SR))
            tp = np.arange(b3 - a3) / SR
            f = note(m)
            tone = np.sin(2 * np.pi * f * tp) + 0.3 * np.sin(2 * np.pi * 2 * f * tp) + 0.1 * np.sin(2 * np.pi * 3 * f * tp)
            pluck[a3:b3] += tone * np.exp(-tp * 7) * env(b3 - a3, 0.003, 0.05) * (1.0 if step % 2 == 0 else 0.7)
        # batterie légère : grosse caisse sur 1 et 3, charleston en croches
        for step in range(16):
            s = start + step * BEAT / 2
            if s >= total:
                break
            a4 = int(s * SR)
            if step % 4 == 0:
                b4 = min(n, a4 + int(0.35 * SR)); tk = np.arange(b4 - a4) / SR
                f = 50 + 70 * np.exp(-tk * 30)
                drums[a4:b4] += np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tk * 9) * 0.9
            b5 = min(n, a4 + int(0.06 * SR))
            nz = rng.standard_normal(b5 - a4)
            nz = nz - lowpass_fast(nz, 6000)
            drums[a4:b5] += nz * np.exp(-np.arange(b5 - a4) / SR * 70) * (0.22 if step % 2 else 0.12)
        start += chord_len
        k += 1

    pad = lowpass_fast(pad, 1400)
    # niveaux par section : courbes d'intensité (0 à 1) de chaque couche
    def curve(points):
        xs = [p[0] for p in points]; ys = [p[1] for p in points]
        return np.interp(t_all, xs, ys)

    s = sections
    pad_c = curve([(0, 0), (1.5, 0.8), (total, 0.8)])
    pluck_c = curve([(0, 0), (s["open"], 0), (s["open"] + 0.3, 0.8), (s["robots"] - 0.5, 0.8), (s["robots"], 0.35), (s["robots_end"], 0.35), (s["robots_end"] + 0.5, 0.8), (total, 0.8)])
    bass_c = curve([(0, 0.25), (s["open"], 0.25), (s["open"] + 0.3, 0.7), (total, 0.7)])
    drum_c = curve([(0, 0), (s["open"] + 2.6, 0), (s["open"] + 2.7, 0.55), (s["robots"] - 0.5, 0.55), (s["robots"], 0), (s["robots_end"], 0), (s["robots_end"] + 0.3, 0.55), (s["fin"], 0.55), (s["fin"] + 0.3, 0.8), (total, 0.8)])
    mix = 0.55 * pad * pad_c + 0.22 * pluck * pluck_c + 0.5 * bass * bass_c + 0.35 * drums * drum_c
    mix = reverb(mix, 2.4, 0.22)
    # silence musical pendant l'ouverture (le sting prend la place), puis fondu final
    gate = curve([(0, 1), (s["open"] - 0.15, 1), (s["open"], 0), (s["open"] + 2.4, 0), (s["open"] + 2.6, 1), (total - 3, 1), (total, 0)])
    mix *= gate
    return mix / (np.max(np.abs(mix)) + 1e-9) * 0.7


def sting():
    d = 2.6
    n = int(d * SR)
    t = np.arange(n) / SR
    # souffle : bruit filtré dont la coupure monte puis redescend (whoosh), calé sur l'entrée en cercle
    nz = rng.standard_normal(n)
    lo, mid, hi = lowpass_fast(nz, 500), lowpass_fast(nz, 1800), lowpass_fast(nz, 6000)
    # balayage continu : on glisse du grave vers l'aigu puis on retombe, par fondus entre trois bandes
    wl = np.interp(t, [0, 0.25, 0.5, 0.9], [1, 0.3, 0, 0.6])
    wm = np.interp(t, [0, 0.25, 0.5, 0.9], [0, 0.8, 0.5, 0.4])
    wh = np.interp(t, [0, 0.25, 0.5, 0.9], [0, 0.2, 0.9, 0.1])
    whoosh = wl * lo + wm * mid * 1.6 + wh * hi * 2.2
    whoosh *= np.interp(t, [0, 0.45, 0.7, 1.2], [0, 1, 0.3, 0])
    # carillon : accord la mineur 9 en notes claires, à l'apparition du logo puis du titre
    bell = np.zeros(n)
    for when, m, g in [(0.22, 81, 1.0), (0.24, 88, 0.7), (0.65, 76, 0.6), (0.68, 83, 0.5), (0.70, 93, 0.25)]:
        a = int(when * SR); tb = np.arange(n - a) / SR; f = note(m)
        tone = np.sin(2 * np.pi * f * tb) + 0.4 * np.sin(2 * np.pi * 2.76 * f * tb) * np.exp(-tb * 6) + 0.2 * np.sin(2 * np.pi * 5.4 * f * tb) * np.exp(-tb * 12)
        bell[a:] += g * tone * np.exp(-tb * 2.2)
    # impact grave sous le logo
    a = int(0.2 * SR); tk = np.arange(n - a) / SR
    boom = np.zeros(n); boom[a:] = np.sin(2 * np.pi * np.cumsum(45 + 60 * np.exp(-tk * 25)) / SR) * np.exp(-tk * 4)
    # souffle de sortie, plus court, sur la fermeture en cercle à 2,1 s
    out = np.zeros(n); a = int(2.0 * SR)
    out[a:] = lowpass_fast(rng.standard_normal(n - a), 2500) * np.interp(np.arange(n - a) / SR, [0, 0.25, 0.6], [0, 0.6, 0])
    s = 0.5 * whoosh + 0.35 * bell + 0.6 * boom + 0.4 * out
    s = reverb(s, 1.8, 0.3)
    s *= np.interp(t, [0, d - 0.15, d], [1, 1, 0])
    return s / (np.max(np.abs(s)) + 1e-9) * 0.8


def write(path, x):
    x = np.clip(x, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())


if __name__ == "__main__":
    cues = json.load(open(sys.argv[1]))
    out = sys.argv[2].rstrip("/")
    write(f"{out}/sting-open.wav", sting())
    write(f"{out}/musique.wav", compose(cues["total"], cues["sections"]))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{out}/musique.wav", "-c:a", "libmp3lame", "-b:a", "256k", f"{out}/musique.mp3"], check=True)
    os.remove(f"{out}/musique.wav")
    print("ok")
