# Fond studio podcast 410 Gone

Fond virtuel pour les vidéos face caméra de la chaîne YouTube 410 Gone : un studio podcast photoréaliste rendu en 3D (Blender Cycles), aux couleurs de l'agence.

| Fichier | Usage |
|---|---|
| `studio-podcast-410-4k.png` | 3840 × 2160, montage 4K ou recadrage |
| `studio-podcast-410-1080p.png` | 1920 × 1080, OBS, NVIDIA Broadcast, Camo, Descript, CapCut |

## Composition

- **Gauche** : mur de lattes en noyer sur feutre noir, enseigne néon 410 Gone (variante « orange » de la charte : « 410 » blanc, GONE et braquets orange), halo LED indigo derrière le panneau.
- **Centre** (derrière la tête) : trois panneaux acoustiques en tissu indigo `#31249F`, éclairés par une douche de lumière pour détacher les cheveux et le t-shirt sombres du fond.
- **Droite** : applique industrielle, enseigne ON AIR orange `#FFB400`, étagère en bois avec livres, plantes et rubans LED chauds.
- Caméra 28 mm à hauteur d'yeux assis, mise au point à 1 m et ouverture f/4 : le fond est légèrement flou, comme filmé avec un vrai boîtier.

Le cadrage laisse la zone centrale calme : la tête tombe sur les panneaux indigo, le logo et l'étagère restent visibles de part et d'autre des épaules.

## Conseils de tournage

- Éclairer le visage avec une lumière un peu chaude (vers 4 000 K) pour se fondre dans l'ambiance du studio ; une petite lumière de contre en arrière, côté gauche ou droit, renforce l'illusion.
- Garder la webcam à hauteur d'yeux, comme la caméra du rendu.
- Avec le détourage d'OBS ou de NVIDIA Broadcast, désactiver le flou d'arrière-plan du logiciel : le fond est déjà flouté.

## Regénérer le rendu

```bash
python -m venv .venv && .venv/bin/pip install bpy opencv-python-headless
.venv/bin/python -I build/fetch_assets.py
.venv/bin/python build/studio_scene.py --out /tmp/brut.png --res 3840 2160 --samples 128
.venv/bin/python -I build/post.py /tmp/brut.png studio-podcast-410-4k.png studio-podcast-410-1080p.png
```

`studio_scene.py` accepte `--fstop` (flou du fond, 4 par défaut) et `--focus` (distance de mise au point, 1 m). `post.py` ajoute le halo des néons, un vignettage doux et un grain de capteur.

## Crédits

- Modèles et textures : [Poly Haven](https://polyhaven.com), licence CC0 (téléchargés par `fetch_assets.py`, non versionnés).
- Police de l'enseigne ON AIR : Oswald, SIL Open Font License (`build/brand/OFL.txt`).
- Logo : kit de la charte 410 Gone.
