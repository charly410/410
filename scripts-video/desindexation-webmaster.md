# Script voix off : « Retirer une page de Google : la bonne méthode »

**Cible :** entreprises, responsables de site, équipes marketing et techniques.
**Format :** tuto / motion design, 16:9, avec chapitres YouTube (un par scène).
**Durée estimée :** 3 min 20 environ (à peu près 475 mots de voix off, débit posé).
**Ton :** clair, direct, sans jargon inutile. On parle à quelqu'un qui a un site à gérer, pas à un développeur.
**Règle d'écriture :** chaque notion est expliquée une seule fois, au moment où elle sert. Pas de récap parlé : l'arbre de décision final fait office de résumé.

---

## 0. Accroche (0:00 à 0:15)

**VISUEL :** trois résultats Google tombent l'un après l'autre, chacun surligné en orange : « preprod.monsite.fr », « Catalogue 2019 - Gamme arrêtée », puis une série de pages en caractères japonais sur le domaine de l'entreprise.

**VOIX OFF :**
> Votre préproduction dans Google. Une gamme arrêtée depuis des années. Ou des centaines de pages de spam après un piratage.
> Toutes ces pages ont un point commun : elles sont sur votre site, et vous voulez les faire sortir de Google. Proprement.

---

## 1. Le principe à retenir (0:15 à 0:40)

**VISUEL :** un petit robot Googlebot revient sur une page. Une étiquette apparaît sur la page (« 410 », « noindex »). Le robot la lit, puis la page se détache de l'index, représenté comme une étagère de fiches.

**VOIX OFF :**
> Google ne retire pas une page parce que vous le lui demandez. Il la retire quand il revient la visiter et qu'il y trouve un signal clair.
> Tout tient donc en deux conditions : envoyer le bon signal, et laisser Google venir le lire.

---

## 2. Choisir le bon signal (0:40 à 1:50)

**VISUEL :** une question s'affiche : « Que devient la page ? ». Quatre cartes se retournent une à une, chacune avec son signal en gros caractères.

### 2a. La page disparaît pour de bon

**VISUEL :** carte « 404 / 410 ». Le « 410 » pulse discrètement, clin d'œil au logo de l'agence.

**VOIX OFF :**
> La page n'existe plus et rien ne la remplace ? Le serveur répond 404, ou 410.
> Pour Google, les deux mènent au même résultat. La 410 dit simplement plus clairement que c'est définitif. Et oui, c'est aussi le nom de notre agence.

### 2b. La page a un remplaçant

**VISUEL :** carte « 301 ». Une flèche relie « Catalogue 2019 » à « Catalogue 2026 ». Une seconde flèche, vers la page d'accueil, se fait barrer.

**VOIX OFF :**
> Elle a un équivalent sur votre site ? Redirigez-la en 301 vers cette page précise. Pas vers l'accueil : Google traite ces redirections fourre-tout comme des pages introuvables.

### 2c. La page reste en ligne, mais hors de Google

**VISUEL :** carte « noindex ». La balise `<meta name="robots" content="noindex">` se tape façon code, puis l'en-tête HTTP `X-Robots-Tag: noindex` apparaît à côté d'une icône PDF.

**VOIX OFF :**
> Vos visiteurs doivent toujours y accéder, mais pas les moteurs de recherche ? Ajoutez une balise noindex.
> Pour un PDF ou une image, qui n'ont pas de code HTML, le même ordre passe par un en-tête HTTP : X-Robots-Tag.

### 2d. Personne ne doit y accéder

**VISUEL :** carte « mot de passe ». Un cadenas se ferme sur la préproduction.

**VOIX OFF :**
> Une préproduction, un espace client, des documents internes ? Le noindex ne suffit pas : la page reste lisible par n'importe qui qui a le lien. Protégez-la par un mot de passe.

---

## 3. Le piège du robots.txt (1:50 à 2:20)

**VISUEL :** un fichier robots.txt avec la ligne `Disallow: /ancienne-gamme/`. Googlebot se cogne contre une porte fermée. Derrière la porte, l'étiquette « noindex » reste invisible. Dans Google, le résultat est toujours là, avec la mention « Aucune information n'est disponible pour cette page ».

**VOIX OFF :**
> Maintenant, l'erreur la plus courante. Bloquer les pages dans le fichier robots.txt.
> Ce fichier interdit à Google de visiter une page. Il ne lui interdit pas de l'afficher. Résultat : Google ne lit plus votre noindex ni votre 410, et la page reste dans les résultats.
> Le bon ordre, c'est d'abord laisser Google constater la désindexation. Et seulement ensuite, si besoin, bloquer l'accès.

---

## 4. Accélérer, sans se tromper d'outil (2:20 à 2:50)

**VISUEL :** interface stylisée de Google Search Console, menu « Suppressions ». Un compte à rebours « six mois » s'affiche sur le résultat masqué. À côté, un fichier sitemap.xml dont des lignes s'effacent. Le logo stylisé de Bing Webmaster Tools apparaît en bas.

**VOIX OFF :**
> Et en cas d'urgence, une fuite de données ou un piratage ? L'outil de suppression de la Search Console masque le résultat en quelques heures.
> Mais il ne fait que masquer, pour environ six mois. Si le signal n'est pas en place sur la page d'ici là, elle revient.
> Pensez aussi à retirer ces adresses de votre sitemap. Et n'oubliez pas Bing : il lit les mêmes signaux, et propose son propre outil de blocage dans Bing Webmaster Tools.

---

## 5. Vérifier, dans les deux sens (2:50 à 3:15)

**VISUEL :** l'outil d'inspection d'URL de la Search Console affiche « Exclue par la balise noindex ». Puis bascule : la page d'accueil du site, avec la même mention, et un voyant qui passe à l'alerte.

**VOIX OFF :**
> Pour vérifier, oubliez la commande « site: » dans Google, qui n'est pas fiable. Utilisez l'inspection d'URL et le rapport d'indexation des pages de la Search Console. Comptez de quelques jours à quelques semaines, selon la fréquence de passage de Google sur votre site.
> Et surveillez aussi l'inverse : un noindex de préproduction oublié à la mise en ligne, et c'est tout votre site qui sort de Google.

---

## 6. Fin (3:15 à 3:30)

**VISUEL :** l'arbre de décision complet se construit une seule fois, sans voix sur chaque branche. Question centrale « Que devient la page ? », puis quatre branches : disparaît (404 / 410), remplacée (301 vers l'équivalent), en ligne hors Google (noindex ou X-Robots-Tag), privée (mot de passe). En bandeau sous l'arbre : « Pas de blocage robots.txt avant désindexation ». Le logo de l'agence s'affiche ensuite.

**VOIX OFF :**
> Un signal clair, que Google peut lire. C'est tout le secret.
> L'arbre de décision complet est dans notre article, en lien juste en dessous.

---

## Notes de production

- **Chapitres YouTube :** Le principe, Choisir le bon signal, Le piège du robots.txt, Accélérer, Vérifier.
- **Mots à appuyer à l'enregistrement :** signal, 404 ou 410, 301, noindex, mot de passe, robots.txt, masquer.
- **Prononciation :** « quatre cent quatre », « quatre cent dix », « trois cent un », « no-index », « robots point texte », « X robots tag ».
- **Textes à l'écran :** uniquement les signaux et les mots-clés, jamais de phrases entières.
- **Vérification avant diffusion :** relire les intitulés exacts de la Search Console (« Suppressions », « Inspection de l'URL », rapport « Pages ») et de Bing Webmaster Tools, qui changent régulièrement. Vérifier aussi que l'article cité en appel à l'action contient bien l'arbre de décision.
- **Hors périmètre volontaire :** le droit à l'oubli et le déréférencement de contenus publiés par des tiers (sujet de la vidéo précédente, destiné aux particuliers).
