# Test A/B/C : « Retirer une page de Google : la bonne méthode »

**Vidéo :** script `scripts-video/desindexation-webmaster.md`.
**Outil :** « Tester et comparer » de YouTube Studio (titres et miniatures).
**Miniatures :** `video/miniatures-desindexation/`, version 2 : `miniature-a-v2.png`, `miniature-b-v2.png`, `miniature-c-v2.png` (HTML source à côté, rendu avec `node render.mjs a-v2 b-v2 c-v2`). Les v1 restent dans le dossier pour mémoire ; ne pas les utiliser pour le test.
**Objectif du test :** savoir quel angle fait cliquer ET regarder une cible d'entreprises, de responsables de site et d'équipes marketing : un visage et un bénéfice, une réponse technique précise, ou le problème qu'ils vivent.

---

## Les trois variantes

Chaque variante associe un titre et une miniature qui racontent la même chose. Les trois couples testent trois hypothèses différentes, pas trois habillages du même message.

### Variante A : le bénéfice, porté par un visage

- **Titre :** Retirer une page de Google : la bonne méthode (45 caractères)
- **Miniature :** `miniature-a-v2.png`. Un résultat de recherche « Catalogue 2019 », cerclé d'orange, est éjecté d'une liste de résultats où reste un emplacement vide ; le présentateur illustré le regarde partir, satisfait. En haut, « Dehors ! » en très gros, en orange : le mot complète le titre au lieu de le répéter.
- **Hypothèse :** montrer le résultat obtenu (la page sort de Google) avec un visage qui réagit attire le regard et rassure une cible non technique. C'est aussi la variante la plus proche du titre prévu dans le script : elle sert de témoin.

### Variante B : la réponse technique, en curiosité

- **Titre :** Supprimer une page de Google : 404 ou 410 ? (43 caractères)
- **Miniature :** `miniature-b-v2.png`. Un tampon « 410 » orange écrase une page « Catalogue 2019 » ; à droite, « Pas 404 », le 404 barré en orange. Le bon et le mauvais choix se lisent sans connaître les codes HTTP.
- **Hypothèse :** les responsables de site connaissent la 404 ; leur montrer qu'il existe un meilleur code crée une question qu'ils veulent résoudre. Bonus de marque : le chiffre héros est le nom de l'agence. Risque à observer : un visuel trop technique peut faire fuir la partie marketing de la cible.

### Variante C : l'erreur à éviter, par la tension

- **Titre :** Désindexer une page : l'erreur qui la garde dans Google (55 caractères)
- **Miniature :** `miniature-c-v2.png`. « Toujours là ? » en très gros au-dessus d'un grand résultat de recherche fictif « Catalogue 2019 », entouré d'un trait orange façon feutre ; à droite, une corbeille cochée : la page a bien été supprimée, et pourtant elle reste dans Google. Fond indigo profond, pour ressortir aussi en mode clair.
- **Hypothèse :** le spectateur se reconnaît plus vite dans son problème (« j'ai supprimé la page, elle est toujours dans Google ») que dans une solution. La peur de l'erreur est un moteur de clic fort, et la vidéo y répond réellement (scène 3, le piège du robots.txt).

**Mot-clé en début de titre :** les trois titres commencent par un verbe de recherche réel (« retirer », « supprimer », « désindexer » une page). C'est volontaire : le test dira aussi quel vocabulaire parle à la cible. « Désindexer » est le terme du métier, « retirer » et « supprimer » ceux du client.

**Typographie des titres :** dans YouTube, taper une espace normale avant « : » et « ? ». Une espace insécable passe aussi, mais certains affichages la rendent mal ; la vérifier dans l'aperçu.

---

## Lancer le test dans YouTube Studio

1. Mettre la vidéo en ligne avec la variante A comme titre et miniature par défaut (c'est le témoin, cohérent avec le script et la description).
2. Dans le détail de la vidéo, section Miniature (ou menu de la miniature), choisir « Tester et comparer ».
3. Choisir le test **titres et miniatures** : chaque variante est alors un couple titre plus miniature. Saisir A, B et C dans les trois emplacements, en associant bien chaque titre à sa miniature (A avec `miniature-a.png`, etc.).
4. Enregistrer. YouTube répartit les impressions entre les trois variantes et désigne le gagnant selon la **part de durée de visionnage** (watch time share), pas selon le taux de clics.

**Conditions habituelles :** fonction disponible sur ordinateur uniquement, pour les chaînes qui ont accès aux fonctionnalités avancées ; pas pour les vidéos « conçues pour les enfants » ni les vidéos privées. Les PNG font moins de 2 Mo (209 à 334 Ko), en 1280x720.

### À vérifier dans l'interface du moment

L'interface et les règles de « Tester et comparer » évoluent souvent. Avant de lancer, vérifier :

- **Le libellé exact** du bouton et son emplacement (« Tester et comparer », « Test & compare »), et s'il apparaît dès la mise en ligne ou seulement une fois la vidéo publiée.
- **Le mode titres et miniatures** : qu'il est bien proposé sur la chaîne (il a été déployé progressivement) et qu'il associe titre et miniature par couple. S'il ne propose que les miniatures, garder le titre A pour les trois et ne tester que les images (le test devient alors purement visuel, ce qui est plus propre à lire).
- **Le nombre de variantes** autorisé (trois à ce jour) et la limite de longueur du titre.
- **Les libellés de résultat** (par exemple « Gagnant », « Performances équivalentes », « Non concluant ») et ce que YouTube fait à la fin : appliquer automatiquement la variante gagnante, ou garder la variante par défaut quand le test n'est pas concluant.
- **La durée maximale** du test et l'éventuel délai minimal avant résultat.
- **Le format accepté** pour les miniatures (PNG ou JPG, 2 Mo maximum, 1280x720 conseillé).

---

## Durée conseillée

- **Laisser tourner jusqu'au bout**, soit environ deux semaines, durée maximale habituelle. Ne pas arrêter au bout de deux jours sur une tendance : les premiers jours mélangent abonnés et notifications, un public qui n'est pas celui de la recherche.
- Une vidéo tutoriel vit surtout de la recherche et des suggestions, et ce trafic monte lentement. Si YouTube rend « non concluant » faute de volume, relancer un test plus tard avec deux variantes seulement (le témoin et la meilleure des deux autres) plutôt que trois : chaque variante reçoit alors plus d'impressions.
- Ne rien modifier pendant le test : ni titre, ni description, ni miniature, sous peine de fausser la comparaison.

---

## Quoi regarder au résultat

1. **Le verdict de YouTube** (part de durée de visionnage par variante). C'est le critère principal : une variante qui fait cliquer mais déçoit perd ici.
2. **Le taux de clics par variante**, s'il est affiché, à lire à côté de la durée : un taux de clics élevé avec une durée faible signale une miniature ou un titre qui promet autre chose que la vidéo (risque surtout pour B, si le spectateur attend un comparatif détaillé 404 / 410, et pour C, si la tension promet un drame).
3. **Les sources de trafic** dans YouTube Analytics une fois le test fini : si la recherche YouTube domine, le mot du titre gagnant (« retirer », « supprimer » ou « désindexer ») est un indice de vocabulaire à réutiliser dans les prochains titres et dans l'article associé.
4. **La fidélisation à 30 secondes** de la vidéo pendant et après le test : l'accroche (préproduction, gamme arrêtée, piratage) doit tenir la promesse du couple gagnant.

### Comment lire le gagnant

Comme titre et miniature changent ensemble, le test désigne un **couple**, pas un titre ni une image isolément. Pour savoir lequel des deux a fait la différence :

- garder le couple gagnant en place quelques semaines ;
- puis lancer un second test **miniatures seules** avec le titre gagnant, ou **titres seuls** avec la miniature gagnante, selon ce qu'on veut apprendre pour les prochaines vidéos de la chaîne.

Les enseignements sont à noter pour la série : résultat montré avec un visage, code technique mis en scène ou problème vécu, et vocabulaire client contre vocabulaire métier. Les trois miniatures partagent le même fond indigo : le test ne mesure donc pas l’effet de la couleur de fond.

---

## Points de vigilance sur le contenu

- **Titre B, « 404 ou 410 ? » :** la vidéo y répond (scène 2a), mais ce n'est qu'une des quatre situations. Si la durée de visionnage de B décroche nettement après la scène 2a, c'est que le titre attire un public venu chercher uniquement ce comparatif.
- **Affirmation sur la 410 :** le script dit que Google prend en compte la 410 « plus vite » que la 404. Google a indiqué que l'écart entre les deux est faible en pratique. La miniature B ne fait pas de promesse chiffrée, mais garder la formulation du script prudente.
- **Miniatures A, B et C :** les résultats de recherche sont fictifs et génériques (« monsite.fr », sans logo ni couleurs de Google) pour ne pas imiter une capture réelle de Google.
