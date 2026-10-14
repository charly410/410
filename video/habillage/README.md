# Habillage vidéo 410 Gone

Ouverture et écran de fin communs à toutes les vidéos de la chaîne, aux couleurs de la charte (indigo `#31249F` et `#201A64`, orange `#FFB400`, Montserrat et Inter).

## Ouverture (2,6 s)

À placer juste après le hook, jamais en tout début de vidéo. Le titre change à chaque vidéo :

```
cd video
node habillage/render.mjs open "Retirer une page de Google" "La bonne méthode" habillage/open-desindexation.mp4
```

## Écran de fin (15 s)

`fin-410.mp4` sert pour toutes les vidéos ; seule la voix off posée dessus change. YouTube accepte un écran de fin de 5 à 20 secondes : les 15 s du clip couvrent toute sa durée.

Dans YouTube Studio, onglet « Écran de fin », placer :

| Élément YouTube | Zone sur le clip (cadre 1920 x 1080) |
|---|---|
| S'abonner | cercle de 360 px centré en (520, 560), dans l'anneau orange |
| Vidéo (choix précis ou « la plus récente ») | rectangle 880 x 495 d'origine (900, 312), dans le cadre à braquets |

Pour vérifier le placement, générer une image avec les zones dessinées :

```
node habillage/render.mjs stills fin 3 guides
```

Pour régénérer le clip après une modification de `habillage.html` :

```
node habillage/render.mjs fin habillage/fin-410.mp4
```
