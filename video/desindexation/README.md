# Montage « Retirer une page de Google : la bonne méthode »

Projet HyperFrames (HTML vers vidéo) de la vidéo désindexation, version entreprises.
Script : `scripts-video/desindexation-webmaster.md`. Voix : ElevenLabs v4, voix « Fred - Radio Host » (`assets/voix.mp3`).

## Structure

| Élément | Fichier |
|---|---|
| Composition principale : fond, scènes, présentateur, habillage, pistes audio | `index.html` |
| Une scène par chapitre du script | `compositions/hook.html` à `compositions/arbre.html` |
| Repères de chapitre et logo | `compositions/reperes.html` |
| Présentateur illustré, bouche calée sur la voix | `compositions/presentateur.html` (**généré**, voir plus bas) |
| Ouverture et écran de fin 410 Gone | `assets/open-desindexation.mp4`, `assets/fin-410.mp4` (source : `video/habillage/`) |
| Musique et jingle d'ouverture, composés par synthèse | `assets/musique.mp3`, `assets/sting-open.wav` (**générés**) |
| Transcription mot à mot de la voix (faster-whisper) | `transcript.json` |

La voix est un seul fichier, coupé en trois clips : le hook (0 à 15,06 s), le corps (décalé de 2,64 s pour laisser passer l'ouverture) et la réplique de l'écran de fin. Les repères temporels sont dans `build/montage.py` ; chaque scène convertit les temps de la voix avec sa fonction `T()`.

## Régénérer les éléments calculés

```
cd video/desindexation
python3 build/preparer.py
```

Le script recalcule la bouche du présentateur (enveloppe de la voix, 30 images par seconde), ses clignements, hochements et sourcils, puis recompose la musique et le jingle aux durées du montage. Ne pas éditer `compositions/presentateur.html` à la main : modifier `build/presentateur.template.html` ou `assets/presentateur.svg`.

La musique est creusée sous la voix (« voiceover carve » de HyperFrames, attributs `data-fx-*` sur `#musique`). Après un changement de voix ou de musique, refaire le creusement :

```
node ~/.claude/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --bed musique --voice voix-hook --voice voix-corps --voice voix-fin
```

puis remettre `"sources":["voix"]` dans `data-fx-carve` (le groupe plutôt que les clips).

## Vérifier et rendre

```
npm install
npx hyperframes check
npx hyperframes render -q standard -o rendu/desindexation-410.mp4
```

Le rendu final est `rendu/desindexation-410.mp4` (1920 x 1080, 30 images par seconde, 2 min 59 s 5).

## Musique

La musique est originale, composée par synthèse dans `build/musique.py` (aucun échantillon externe), donc libre de droits. Pour la remplacer par un titre de la bibliothèque audio de YouTube, déposer le fichier dans `assets/`, changer le `src` de `#musique`, ajuster `data-volume` et refaire le creusement.
