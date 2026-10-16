# Montage « Retirer une page de Google » sur le rush HeyGen

Projet HyperFrames du montage qui prend le rush HeyGen comme base et y intègre le motion design.
Rush : `video/heygen/dereferencement-heygen.mp4` (1280 x 720, 25 i/s, 2 min 37 s). Script : `scripts-video/desindexation-webmaster.md`.

## Mise en place

Le rush n'est pas dupliqué dans le dépôt. Avant tout aperçu ou rendu :

```
cd video/desindexation-rush
mkdir -p rush && cp ../heygen/dereferencement-heygen.mp4 rush/rush-heygen.mp4
npm install
```

Pour passer au rush 1080p ré-exporté depuis HeyGen, remplacer `rush/rush-heygen.mp4` et `assets/rush-voix.m4a` (`ffmpeg -i rush/rush-heygen.mp4 -vn -af loudnorm=I=-15:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k assets/rush-voix.m4a` : la voix HeyGen sort à -20 LUFS, on la remonte vers -15 pour que la vidéo finale arrive près des -14 de YouTube). Si le minutage est identique, rien d'autre ne change ; sinon refaire la transcription et `build/montage.py`.

## Déroulé

| Moment | Rush | Motion design |
|---|---|---|
| Hook (0 à 13,7 s) | Plein écran, puis glisse dans la moitié droite | Résultats de recherche qui apparaissent à gauche, puis « Les sortir de Google, proprement » |
| Ouverture (13,7 à 17,3 s) | Coupé | Planche 410 Gone de 3,6 s (2,6 s + 1 s de tenue) et son jingle |
| Chapitres (17,3 à 153,4 s) | Colonne de gauche | Les scènes du premier montage, recalées sur la voix du rush |
| « C'est aussi le nom de notre agence » | Plein écran | Bandeau logo 410 Gone |
| « Un signal clair… c'est tout le secret » | Plein écran | Titre en bandeau bas, puis retour en colonne pour l'arbre de décision |
| Écran de fin (153,4 à 168,4 s) | Coupé, la voix continue | Écran de fin réutilisable 410 Gone |

## Fichiers

| Élément | Fichier |
|---|---|
| Composition principale : fenêtre du rush et ses trois cadrages, pistes audio, habillage | `index.html` |
| Motion design sur le rush | `compositions/hook-rush.html`, `compositions/temps-forts.html` |
| Scènes des chapitres (reprises du premier montage) | `compositions/principe.html` à `compositions/arbre.html` |
| Correspondance voix d'origine vers voix du rush, débuts de scène | `assets/carte-temps.js` (**généré**) |
| Repères du montage (coupe, ouverture, fin) et calcul de la correspondance | `build/montage.py` |
| Musique et jingle, composés par synthèse | `build/musique.py`, `assets/musique.mp3`, `assets/sting-open.wav` (**générés**) |
| Transcriptions mot à mot : rush et voix d'origine | `transcript.json`, `build/transcript-elevenlabs.json` |

Les scènes ont été écrites sur la voix ElevenLabs. `build/montage.py` apparie les mots des deux transcriptions (97 % appariés) et fournit `window.CARTE(v)`, qui convertit un temps de la voix d'origine en temps de la timeline ; chaque scène l'utilise dans sa fonction `T()`.

## Régénérer

```
python3 build/montage.py build/transcript-elevenlabs.json
python3 build/musique.py build/cues-musique.json assets
node ~/.claude/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --bed musique --voice voix-hook --voice voix-corps --voice voix-fin
```

Après le creusement, remettre `"sources":["voix"]` dans `data-fx-carve` de `#musique`. Si `build/montage.py` affiche d'autres débuts de scène, reporter les valeurs dans les `data-start` et `data-duration` de `index.html`.

## Vérifier et rendre

`npx hyperframes check` d'un seul tenant dépasse son délai à cause du rush ; le lancer par tranches :

```
for r in 0,40 40,85 85,125 125,168; do npx hyperframes check --timeout 60000 --range $r --samples 5; done
npx hyperframes render -q standard --browser-timeout 180 -o rendu/desindexation-rush-410.mp4
```
