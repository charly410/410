"""Repères temporels du montage, en secondes. Source unique pour les scripts de préparation.

La voix ElevenLabs est un seul fichier : on la coupe après le hook pour insérer l'ouverture,
puis on décale la réplique de l'écran de fin. Les compositions reprennent ces valeurs.
"""

OPEN = 15.0          # début de l'ouverture 410 Gone (2,6 s)
COUPE = 15.06        # point de coupe dans la voix, entre « proprement » et « Google ne retire pas »
DECALAGE = 2.64      # décalage de la voix après la coupe
FIN = 164.5          # début de l'écran de fin
TOTAL = 179.5

# (début sur la timeline, début dans le fichier voix, durée)
VOIX = [
    (0.0, 0.0, COUPE),
    (COUPE + DECALAGE, COUPE, 161.5 - COUPE),
    (165.3, 161.6, 169.72 - 161.6),
]

PRESENTATEUR_VISIBLE = [(8.6, OPEN), (OPEN + 2.6, FIN)]


def global_time(v):
    """Temps dans le fichier voix vers temps sur la timeline (None hors des segments gardés)."""
    for g, m, d in VOIX:
        if m <= v < m + d:
            return v - m + g
    return None


def g(v):
    return round(v + DECALAGE, 2) if v >= COUPE else v


# Sourcils levés sur les mots d'insistance (temps voix, convertis)
SOURCILS = [g(x) for x in (7.66, 40.52, 81.88, 112.90, 145.98)]

# Positions du personnage : grand à droite pendant le hook, puis en colonne de gauche
POSES = {"entree": 8.62, "colonne": 16.2}

SECTIONS_MUSIQUE = {"open": OPEN, "robots": g(81.88) - 0.3, "robots_end": g(87.28), "fin": FIN}
