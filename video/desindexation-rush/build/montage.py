"""Repères temporels du montage sur le rush HeyGen. Source unique pour les scripts de préparation.

Les scènes de motion design ont été écrites sur la voix ElevenLabs (temps « v »). Le rush HeyGen dit
le même texte à un autre rythme : on apparie les mots des deux transcriptions et on en tire une
correspondance v vers temps du rush, puis temps du rush vers temps de la timeline (coupe pour l'ouverture).

Usage (depuis video/desindexation-rush) :
  python3 build/montage.py chemin/transcript-elevenlabs.json
Écrit assets/carte-temps.js (window.CARTE et window.DEBUT) et build/cues-musique.json, puis affiche les repères.
"""
import difflib, json, re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Rush : coupe entre « proprement » (fin 13,60 s) et « Google ne retire pas » (13,80 s)
COUPE = 13.70
OPEN = 13.70          # ouverture 410 Gone, juste après le hook
OPEN_DUREE = 3.6      # 2,6 s d'origine + 1 s de tenue demandée
REPRISE = 17.40       # le rush reprend ici après l'ouverture
DECALAGE = REPRISE - COUPE
FIN_RUSH = 149.45     # dans le rush, juste avant « Abonnez-vous »
FIN = 153.40          # début de l'écran de fin
VOIX_FIN = 154.20     # la réplique « Abonnez-vous… » se pose ici, sur l'écran de fin
TOTAL = FIN + 15.0

# Débuts de scène, en temps de la voix ElevenLabs (début de la première phrase de chaque scène)
SCENES_V = {
    "signal-410": 28.16, "signal-301": 47.31, "signal-noindex": 56.96, "signal-prive": 71.16,
    "robots": 81.76, "accelerer": 105.76, "verifier": 130.76, "arbre": 153.46,
}


def norm(w):
    w = unicodedata.normalize("NFD", w.lower())
    w = "".join(c for c in w if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]", "", w)


def mots(path):
    d = json.load(open(path))
    out = []
    for s in d:
        for w in s["words"]:
            n = norm(w["w"])
            if n:
                out.append((n, w["s"]))
    return out


def rush_vers_global(r):
    if r < COUPE:
        return r
    if r < FIN_RUSH:
        return r + DECALAGE
    return r - FIN_RUSH + VOIX_FIN


def main():
    el = mots(sys.argv[1])
    ru = mots(ROOT / "transcript.json")
    sm = difflib.SequenceMatcher(a=[w for w, _ in el], b=[w for w, _ in ru], autojunk=False)
    ancres = []
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            ancres.append((el[a + k][1], ru[b + k][1]))
    # ancres strictement croissantes des deux côtés
    propres, last_v, last_r = [], -1, -1
    for v, r in ancres:
        if v > last_v and r > last_r:
            propres.append((round(v, 3), round(rush_vers_global(r), 3)))
            last_v, last_r = v, r
    couverture = len(propres) / len(el)

    def carte(v):
        if v <= propres[0][0]:
            return propres[0][1] + (v - propres[0][0])
        for (v0, g0), (v1, g1) in zip(propres, propres[1:]):
            if v0 <= v <= v1:
                return g0 + (g1 - g0) * (v - v0) / (v1 - v0)
        return propres[-1][1] + (v - propres[-1][0])

    debut = {"principe": round(OPEN + OPEN_DUREE, 2)}
    for k, v in SCENES_V.items():
        debut[k] = round(carte(v + 0.08) - 0.12, 2)
    js = ("// FICHIER GÉNÉRÉ par build/montage.py : ne pas éditer à la main.\n"
          "// CARTE(v) : temps de la voix ElevenLabs (scènes d'origine) vers temps de la timeline du rush.\n"
          f"window.ANCRES = {json.dumps(propres, separators=(',', ':'))};\n"
          f"window.DEBUT = {json.dumps(debut)};\n"
          "window.CARTE = function (v) {\n"
          "  const A = window.ANCRES;\n"
          "  if (v <= A[0][0]) return A[0][1] + (v - A[0][0]);\n"
          "  for (let i = 1; i < A.length; i++) {\n"
          "    if (v <= A[i][0]) return A[i - 1][1] + (A[i][1] - A[i - 1][1]) * (v - A[i - 1][0]) / (A[i][0] - A[i - 1][0]);\n"
          "  }\n"
          "  return A[A.length - 1][1] + (v - A[A.length - 1][0]);\n"
          "};\n")
    (ROOT / "assets/carte-temps.js").write_text(js)
    cues = {"total": TOTAL, "open_duree": OPEN_DUREE,
            "sections": {"open": OPEN, "open_duree": OPEN_DUREE, "robots": round(carte(81.88) - 0.3, 2),
                         "robots_end": round(carte(87.28), 2), "fin": FIN}}
    (ROOT / "build/cues-musique.json").write_text(json.dumps(cues))
    ordre = ["principe"] + list(SCENES_V)
    print(f"ancres : {len(propres)} mots appariés sur {len(el)} ({couverture:.0%})")
    for i, k in enumerate(ordre):
        fin = debut[ordre[i + 1]] if i + 1 < len(ordre) else FIN
        print(f"{k:15s} début {debut[k]:7.2f}  durée {fin - debut[k]:6.2f}")
    print(f"total {TOTAL}")


if __name__ == "__main__":
    main()
