# Voix off ElevenLabs v4 : « Retirer une page de Google : la bonne méthode »

Texte prêt à coller dans ElevenLabs (modèle **Eleven v4**), découpé en une génération par scène pour caler facilement le montage.
Script source : `desindexation-webmaster.md`. Les audio tags sont en anglais (c'est ce que le modèle suit le mieux) ; le texte est en français.
Nombres, sigles et termes anglais sont écrits phonétiquement pour éviter les mauvaises lectures.

---

## Scène 0 : Accroche (0:00 à 0:15)

```
[matter-of-fact, slightly ironic] Votre préproduction… dans Google. [short pause] Une gamme arrêtée depuis des années. [short pause] [concerned] Ou des centaines de pages de spam, après un piratage.
[pause] [clear, confident] Toutes ces pages ont un point commun : elles sont sur VOTRE site, et vous voulez les faire sortir de Google. [short pause] [firm] Proprement.
```

## Ouverture 410 Gone (0:15 à 0:18)

Pas de voix off : clip `video/habillage/open-desindexation.mp4`.

## Scène 1 : Le principe à retenir (0:18 à 0:43)

```
[clear, didactic] Google ne retire pas une page parce que vous le lui demandez.
[steady] Il la retire quand il revient la visiter… [short pause] et qu'il y trouve un signal clair.
[pause] [emphasizing] Tout tient donc en deux conditions : [short pause] envoyer le bon signal… [short pause] et laisser Google venir le lire.
```

## Scène 2a : La page disparaît pour de bon (0:43 à 1:05)

```
[questioning] La page est supprimée, et ne reviendra pas ? [short pause] [confident] Le bon signal, c'est le code quatre cent dix.
[didactic] Une quatre cent quatre dit seulement à Google : « introuvable ». [short pause] La quatre cent dix, elle, lui dit : [slower, articulating] « supprimée. Définitivement. »
[confident] Un signal plus fort, qu'il prend en compte plus vite.
[pause] [playful, knowing smile] Et oui… c'est aussi le nom de notre agence.
```

## Scène 2b : La page a un remplaçant (1:05 à 1:20)

```
[conversational] Elle a un équivalent sur votre site ? [short pause] Redirigez-la en trois cent un, vers cette page précise.
[firm] Pas vers l'accueil : [short pause] [explaining] Google traite ces redirections fourre-tout comme des pages introuvables.
```

## Scène 2c : La page reste en ligne, mais hors de Google (1:20 à 1:38)

```
[conversational] Vos visiteurs doivent toujours y accéder, mais pas les moteurs de recherche ? [short pause] Ajoutez une balise « no-index ».
[didactic, steady pace] Pour un P.D.F. ou une image, qui n'ont pas de code H.T.M.L., le même ordre passe par un en-tête H.T.T.P. : [short pause] « iks robots tag ».
```

## Scène 2d : Personne ne doit y accéder (1:38 à 1:55)

```
[listing] Une préproduction… un espace client… des documents internes ?
[serious] Le « no-index » ne suffit pas : la page reste lisible par toute personne qui a le lien.
[firm] Protégez-la par un mot de passe.
```

## Scène 3 : Le piège du robots.txt (1:55 à 2:25)

```
[serious, warning tone] Maintenant, l'erreur la plus courante. [short pause] Bloquer les pages dans le fichier « robots point T.X.T. ».
[clear] Ce fichier interdit à Google de VISITER une page. [short pause] Il ne lui interdit pas de l'AFFICHER.
[explaining] Résultat : Google ne lit plus votre « no-index », ni votre quatre cent dix… [short pause] et la page reste dans les résultats.
[pause] [calm, reassuring] Le bon ordre, c'est d'abord laisser Google constater la désindexation. [short pause] Et seulement ensuite, si besoin, bloquer l'accès.
```

## Scène 4 : Accélérer, sans se tromper d'outil (2:25 à 2:55)

```
[questioning, a bit urgent] Et en cas d'urgence ? Une fuite de données, un piratage ?
[confident] L'outil de suppression de la Search Console masque le résultat en quelques heures.
[short pause] [cautionary] Mais il ne fait que MASQUER, pour environ six mois. [short pause] Si le signal n'est pas en place sur la page d'ici là… [slower] elle revient.
[pause] [practical, upbeat] Pensez aussi à retirer ces adresses de votre « site map ». [short pause] Et n'oubliez pas Bing : il lit les mêmes signaux, et propose son propre outil de blocage, dans Bing Webmaster Tools.
```

## Scène 5 : Vérifier, dans les deux sens (2:55 à 3:20)

```
[practical] Pour vérifier, oubliez la commande « site deux-points » dans Google : [short pause] elle n'est pas fiable.
[didactic, steady pace] Utilisez l'inspection d'U.R.L. et le rapport d'indexation des pages de la Search Console.
[calm] Comptez de quelques jours à quelques semaines, selon la fréquence de passage de Google sur votre site.
[pause] [serious, warning tone] Et surveillez aussi l'inverse : un « no-index » de préproduction oublié à la mise en ligne… [short pause] [slower, emphasizing] et c'est tout votre site qui sort de Google.
```

## Scène 6 : L'arbre de décision (3:20 à 3:30)

```
[warm, concluding] Un signal clair, que Google peut lire. [short pause] C'est tout le secret.
[friendly, inviting] L'arbre de décision complet est dans notre article, en lien, juste en dessous.
```

## Écran de fin (3:30 à 3:45)

Posée sur `video/habillage/fin-410.mp4`. Seule cette réplique change d'une vidéo à l'autre.

```
[friendly, upbeat] Abonnez-vous pour ne pas rater la suite.
[short pause] [warm, inviting] Et si c'est un contenu publié par quelqu'un d'autre qui nuit à votre entreprise… [short pause] la vidéo à l'écran est faite pour vous.
```

---

## Réglages conseillés

- **Modèle :** Eleven v4 (pas la version Turbo, moins expressive : à garder pour itérer vite).
- **Voix :** la même que pour la vidéo déréférencement, pour que la chaîne garde une voix reconnaissable.
- **Une génération par scène :** plus facile à caler sur l'animation, et on ne régénère que la scène ratée.
- **Stabilité :** curseur au milieu (« Natural » si le preset existe). Plus bas, les tags sont exagérés ; plus haut, ils sont ignorés.
- **Vitesse :** 1.0 par défaut. Ralentir légèrement (environ 0.95) sur les scènes 2c, 3 et 5, les plus techniques.
- **Générer 2 à 3 prises par scène** et garder la meilleure : le suivi des tags varie d'une prise à l'autre.
- **Test de prononciation :** lancer d'abord la scène 2c, qui concentre les sigles (P.D.F., H.T.M.L., H.T.T.P., « iks robots tag »). Si un sigle passe mal, essayer la variante du tableau ci-dessous avant de toucher aux réglages.

## Pièges de prononciation neutralisés dans le texte

| Écrit dans le script | Écrit pour ElevenLabs | Pourquoi |
|---|---|---|
| 404 / 410 / 301 | quatre cent quatre / quatre cent dix / trois cent un | évite « quatre zéro quatre » |
| noindex | « no-index » | évite « noïndex » |
| robots.txt | « robots point T.X.T. » | forme orale courante chez les développeurs ; variante : « robots point texte » |
| X-Robots-Tag | « iks robots tag » | évite « x » lu comme un signe de multiplication |
| PDF, HTML, HTTP, URL | P.D.F., H.T.M.L., H.T.T.P., U.R.L. | force l'épellation |
| sitemap | « site map » | évite « sitmap » à la française |
| site: | « site deux-points » | le deux-points n'est pas lu sinon |
| n'importe qui qui a le lien | toute personne qui a le lien | évite le « qui qui » à l'oreille |
