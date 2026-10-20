# Journal de montage : « Retirer une page de Google » sur rush HeyGen

Ce journal consigne les décisions de montage, version par version, pour le monteur qui reprend le projet : ce qui a changé, pourquoi, où le modifier. La mise en place et les commandes sont dans `README.md`.

## v1 (16/10/2026) : rush en base, scènes recalées

- Rush HeyGen en base, trois cadrages : plein écran, moitié droite (hook), colonne de gauche (chapitres).
- Scènes de motion design du premier montage recalées sur la voix du rush par appariement des transcriptions (`build/montage.py`, 97 % des mots appariés).
- Ouverture 410 Gone allongée d'une seconde (3,6 s), jingle allongé d'autant.
- Plein écran sur « c'est aussi le nom de notre agence » et « un signal clair… c'est tout le secret ».
- Voix normalisée de -20 à -15 LUFS ; vidéo finale à -16 LUFS.
- Rendu : `rendu/desindexation-rush-410.mp4`.

Retour : l'ensemble fait encore trop IA, sur l'avatar comme sur la voix.

## v2 (20/10/2026) : masquer l'aspect IA par le montage

Objectif : que l'avatar ne soit jamais exposé longtemps dans un plan fixe, ajouter du réel, et donner une texture commune à l'image. Moteur : HyperFrames 0.8.181 (projet mis à jour depuis 0.8.156), avec trois éléments du catalogue HyperFrames.

### 1. Un plan qui change à chaque phrase

| Quoi | Comment | Où |
|---|---|---|
| Changement de « caméra » à chaque début de phrase du rush | Trois motifs en boucle : coupe franche en plan moyen, coupe franche en plan serré, poussée lente (zoom progressif sur la durée de la phrase, 6 s au plus) | `index.html`, bloc « rythme de montage » |
| Débuts de phrase | Calculés depuis la transcription du rush (mot qui suit un point, un point d'interrogation ou d'exclamation) | `build/montage.py`, `window.PHRASES` dans `assets/carte-temps.js` |
| Zooms centrés sur le visage | Origine du zoom à 51 % / 31 % de l'image (visage de l'avatar) ; serré = +38 % en colonne, +18 % en plein écran ou à droite | `ETATS` dans `index.html` |
| Pas de zoom pendant un changement de cadrage | Les phrases à moins de 0,6 s d'un changement de cadrage sont ignorées ; chaque changement repart d'un plan moyen | `prochesDunPlan` dans `index.html` |

Les helpers de zoom sont ceux du bloc `yt-camera-move` du catalogue (copie dans `compositions/components/yt-camera-move.html`).

La fenêtre du rush a été reconstruite selon les règles HyperFrames : la forme vient d'un masque (`clip-path` sur `#cadre`), le cadrage d'un conteneur `#cadrage` (translation et échelle), les zooms d'un second conteneur `#camera`. On n'anime plus ni position ni taille, ce qui évite les à-coups.

Pour changer le rythme : modifier les motifs (`motif === 0 / 1 / 2`) ou la force du plan serré (`serre` dans `ETATS`).

### 2. Du réel : deux preuves tirées de la documentation Google

| Moment | Capture | Phrase mise en valeur |
|---|---|---|
| « Résultat : Google ne lit plus votre noindex… la page reste dans les résultats » | Google Search Central, page « Bloquer l'indexation avec noindex » | Encadré « Important » : la page ne doit pas être bloquée par un fichier robots.txt |
| « Mais il ne fait que masquer, pour environ six mois » | Aide Search Console, page « Outil de suppression » | « L'outil de suppression ne permet d'effectuer qu'une suppression temporaire d'environ six mois » |

- Captures faites dans le navigateur par `build/preuves.mjs` : page affichée en 1200 x 675 à une densité de 1,6, pour que le texte soit lisible en vidéo. La position de la phrase est enregistrée automatiquement (`assets/preuves/preuves.json` et `preuves.js`). La capture HyperFrames (`hyperframes capture`) a servi à repérer la phrase exacte dans la page.
- Chaque preuve passe en plein écran, sans le rush, avec un zoom lent qui amène la phrase au centre (calculé pour ne jamais la couper), un cadre orange, le projecteur du bloc `yt-feather-highlight` du catalogue, l'étiquette « Ce que dit Google » et la source.
- Fenêtres : `PREUVES_V` dans `build/montage.py` (temps de la voix d'origine). Composition : `compositions/preuves.html`.
- Si Google modifie ses pages, relancer `node build/preuves.mjs` et vérifier les images.

### 3. Texture commune : étalonnage et grain

- **Étalonnage du rush** par l'outil de traitement HyperFrames (`hyperframes media-treatment`), recette « Natural Portrait » (tête qui parle, rendu naturel) après analyse de l'image : préréglage `skin-soft` à 0,55, hautes lumières -0,06, ombres +0,06, température -0,02, vibrance +0,02, vignette 0,03, grain 0,08. Attribut `data-color-grading` sur les deux vidéos `.rush`.
- **Grain sur toute l'image**, rush et motion design, pour casser l'aspect trop lisse : bloc `grain-overlay` du catalogue, opacité réduite à 0,06 et animation rendue finie (337 cycles de 0,5 s) pour respecter le rendu image par image de HyperFrames. Élément `#grain-overlay` dans `index.html`.

### Vérifications

- `hyperframes lint` : 0 erreur, 0 avertissement.
- `hyperframes check` par tranches (0-45, 45-90, 90-130, 130-168 s) : 0 erreur. Restent des alertes de contraste prises en pleine transition ou sous une preuve (invisibles à l'écran) et des messages du moteur graphique liés à l'étalonnage.
- Images de contrôle : hook, colonne en plan moyen et serré, plein écran, deux preuves, arbre de décision.

### Rendu

`rendu/desindexation-rush-410-v2.mp4` (1920 x 1080, 2 min 48 s, -16 LUFS). La v1 reste dans `rendu/` pour comparer.

- Le rendu HyperFrames brut pèse 150 Mo : le grain se compresse mal, et GitHub refuse les fichiers de plus de 100 Mo. La version commitée est réencodée en deux passes à 4,3 Mbit/s (95 Mo) :
  `ffmpeg -i brut.mp4 -c:v libx264 -preset slow -b:v 4300k -pass 1 -an -f mp4 /dev/null`, puis la même commande en `-pass 2` avec `-c:a aac -b:a 192k -movflags +faststart`.
- Pour la mise en ligne YouTube, le rendu brut est préférable : le relancer (`README.md`) et l'envoyer tel quel, sans le commiter.
- Le rendu prend environ une heure dans ce conteneur (étalonnage calculé sans carte graphique), contre une dizaine de minutes pour la v1.
