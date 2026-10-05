# Voix off ElevenLabs v4 : « Déréférencement Google »

Texte prêt à coller dans ElevenLabs (modèle **Eleven v4**), découpé en une génération par scène pour caler facilement le montage.
Les audio tags sont en anglais (c'est ce que le modèle suit le mieux) ; le texte est en français.
Nombres, sigles et termes anglais sont écrits phonétiquement pour éviter les mauvaises lectures.

---

## Scène 0 : Hook (0:00 à 0:10)

```
[curious, slightly mysterious] Vous tapez votre nom sur Google… [short pause] et là… [disappointed sigh] ce résultat.
[warm] Un vieil article. Une info dépassée. Quelque chose que vous préféreriez… oublier.
[pause] [upbeat, reassuring] Bonne nouvelle : on peut le faire disparaître. [confident] Voyons comment.
```

## Scène 1 : Déréférencer ≠ supprimer (0:10 à 0:35)

```
[clear, didactic] D'abord, une distinction essentielle.
[emphasizing] DÉRÉFÉRENCER, c'est retirer un lien des résultats de Google. [calm] Le contenu, lui, existe toujours sur le site d'origine — simplement, plus personne ne tombe dessus en cherchant.
[short pause] [emphasizing] SUPPRIMER, en revanche, c'est effacer le contenu à la source, directement sur la page web.
[knowing tone] Et les deux ne s'obtiennent pas de la même façon… [short pause] ni auprès des mêmes personnes.
```

## Scène 2 : Qui contrôle le contenu ? (0:35 à 0:45)

```
[thoughtful] Tout dépend d'une seule question : [pause] est-ce que ce contenu est sur VOTRE site… [short pause] ou sur celui de quelqu'un d'autre ?
```

## Scène 3 : Le contenu est sur votre site (0:45 à 1:20)

```
[confident, energetic] Si c'est votre site, bonne nouvelle : vous avez la main.
[didactic] Vous pouvez supprimer la page. Elle renverra alors une erreur quatre cent quatre… [short pause] [playful] ou mieux, une quatre cent dix, qui dit clairement à Google : [slower, articulating] « ce contenu a disparu. Définitivement. »
[pause] [conversational] Vous voulez garder la page en ligne, mais hors de Google ? Ajoutez simplement une balise « no-index ».
[upbeat] Et pour accélérer les choses, passez par l'outil de suppression de la Search Console : il masque le résultat rapidement, le temps que Google prenne en compte vos modifications.
```

## Scène 4a : Site tiers, contacter le site (1:20 à 1:35)

```
[calm, practical] Si le contenu est ailleurs, commencez par le plus simple : écrivez au responsable du site.
Demandez la suppression, l'anonymisation… [short pause] ou, à défaut, l'ajout d'une balise « no-index ».
```

## Scène 4b : Le droit à l'oubli (1:35 à 2:00)

```
[short pause] [slightly serious] Pas de réponse ? [pause] [firm, empowering] Vous avez un droit : le droit à l'oubli, renforcé par le R.G.P.D.
[clear] Il vous permet de demander à Google de ne plus associer votre nom à certaines pages.
[didactic, steady pace] Pour cela, on remplit le formulaire officiel de Google, avec une pièce d'identité, la liste EXACTE des adresses concernées… et une justification solide.
[measured, listing] Google accepte quand l'information est inexacte… périmée… non pertinente… [short pause] ou excessive.
```

## Scène 4c : Le piège à éviter (2:00 à 2:15)

```
[serious, warning tone] Attention, piège classique.
[clear] L'outil « contenu obsolète » de Google ne sert PAS à déréférencer une page toujours en ligne.
[calmer] Il sert seulement quand le site a déjà modifié ou supprimé la page… mais que l'ancienne version traîne encore dans les résultats.
```

## Scène 5 : Et si Google refuse ? (2:15 à 2:35)

```
[questioning] Et si Google dit non ? [short pause] [determined] Ce n'est pas fini.
[confident] Vous pouvez saisir la Cnil. [steady] Si elle juge votre plainte légitime, elle peut OBLIGER le moteur de recherche à déréférencer le lien.
```

## Scène 6 : Récap + CTA (2:35 à 2:55)

```
[warm, upbeat, wrapping up] En résumé :
[rhythmic] votre site ? Vous agissez directement. [short pause] Un site tiers ? Vous contactez, puis vous activez votre droit à l'oubli. [short pause] Un refus ? Vous saisissez la Cnil.
[pause] [friendly, inviting] Pour aller plus loin, avec les modèles d'e-mails et la checklist complète… retrouvez notre article en lien, juste en dessous.
```

---

## Réglages conseillés

- **Modèle :** Eleven v4 (pas la version Turbo, qui est moins expressive : à garder pour itérer vite).
- **Une génération par scène :** plus facile à caler sur l'animation, et on ne régénère que la scène ratée.
- **Stabilité :** curseur au milieu (« Natural » si le preset existe). Plus bas, les tags sont exagérés ; plus haut, ils sont ignorés.
- **Vitesse :** 1.0 par défaut. Ralentir légèrement (environ 0.95) sur les scènes 3 et 4b, les plus denses.
- **Générer 2 à 3 prises par scène** et garder la meilleure : le suivi des tags varie d'une prise à l'autre.

## Choix de la voix (Voice Library, filtre « French »)

**Profil recommandé :** voix masculine ou féminine, 30-45 ans, accent français standard (pas québécois), timbre chaleureux, débit posé. Catégorie « Narrative / Informative & Educational ».
Éviter les voix « conversational » trop jeunes ou les voix « trailer » trop dramatiques : on fait un tuto, pas une bande-annonce.

**Méthode :** tester chaque voix candidate sur la scène 3, la plus technique (« quatre cent dix », « no-index », « Search Console »).
C'est elle qui révèle le mieux les problèmes de prononciation et d'intonation.

## Pièges de prononciation déjà neutralisés dans le texte

| Écrit dans l'article | Écrit pour ElevenLabs | Pourquoi |
|---|---|---|
| 404 / 410 | quatre cent quatre / quatre cent dix | évite « quatre zéro quatre » |
| noindex | « no-index » | évite « noïndex » |
| RGPD | R.G.P.D. | force l'épellation |
| CNIL | Cnil | lu comme un mot, comme à l'oral |
| URLs | adresses | plus fluide à l'oral |
