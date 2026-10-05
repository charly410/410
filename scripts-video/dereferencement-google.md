# Script voix off : « Déréférencement Google : comment faire disparaître un résultat ? »

**Format :** tuto / motion design, 16:9 (une version 9:16 est possible en découpant les séquences)
**Durée estimée :** 2 min 45 à 3 min (environ 430 mots de voix off, débit posé)
**Ton :** clair, rassurant, un peu complice. On tutoie le problème, pas le spectateur.
**Source :** https://www.410-gone.fr/blog/dereferencement.html

---

## 0. Hook (0:00 à 0:10)

**VISUEL :** une barre de recherche Google se remplit avec « Prénom Nom ». Les résultats tombent. Le 3e résultat clignote en rouge, avec un vieil article et une photo floutée.

**VOIX OFF :**
> Vous tapez votre nom sur Google… et là, ce résultat. Un vieil article, une info dépassée, quelque chose que vous préféreriez oublier.
> Bonne nouvelle : on peut le faire disparaître. Voyons comment.

---

## 1. Déréférencer ≠ supprimer (0:10 à 0:35)

**VISUEL :** écran coupé en deux. À gauche, « DÉRÉFÉRENCEMENT » : le lien se détache de la page de résultats Google, mais la page web reste intacte en arrière-plan. À droite, « SUPPRESSION » : la page web elle-même se désintègre en pixels.

**VOIX OFF :**
> D'abord, une distinction essentielle.
> **Déréférencer**, c'est retirer un lien des résultats de Google. Le contenu, lui, existe toujours sur le site d'origine. Simplement, plus personne ne tombe dessus en cherchant.
> **Supprimer**, c'est effacer le contenu à la source, directement sur la page web.
> Les deux ne s'obtiennent pas de la même façon, et surtout pas auprès des mêmes personnes.

---

## 2. Première question : qui contrôle le contenu ? (0:35 à 0:45)

**VISUEL :** un embranchement en forme de flèche. Branche A : « C'est mon site », avec une icône de clé. Branche B : « C'est le site de quelqu'un d'autre », avec une icône de cadenas.

**VOIX OFF :**
> Tout dépend d'une seule question : est-ce que ce contenu est sur **votre** site, ou sur celui de quelqu'un d'autre ?

---

## 3. Cas A : le contenu est sur votre site (0:45 à 1:20)

**VISUEL :** checklist animée, chaque ligne se coche :
1. Supprimer la page, avec un code HTTP **404 / 410** qui s'affiche (clin d'œil : le « 410 Gone » pulse).
2. Ou ajouter la balise `<meta name="robots" content="noindex">`, tapée façon code.
3. Interface stylisée de Google Search Console : « Suppressions », puis « Nouvelle demande ».

**VOIX OFF :**
> Si c'est votre site, vous avez la main.
> Vous pouvez supprimer la page : elle renverra une erreur 404, ou mieux, une **410**, qui dit clairement à Google « ce contenu a disparu, définitivement ».
> Vous voulez garder la page en ligne mais hors de Google ? Ajoutez une balise **noindex**.
> Et pour accélérer les choses, passez par l'outil de **suppression de la Search Console** : il masque le résultat rapidement, le temps que Google prenne en compte vos modifications.

---

## 4. Cas B : le contenu est sur un site tiers (1:20 à 2:15)

### 4a. Contacter le site

**VISUEL :** une enveloppe s'envole vers une icône de site web. Le texte « Bonjour, je vous demande de supprimer / anonymiser… » s'écrit dans la bulle.

**VOIX OFF :**
> Si le contenu est ailleurs, commencez par le plus simple : écrivez au responsable du site. Demandez la suppression, l'anonymisation, ou à défaut l'ajout d'une balise noindex.

### 4b. Le droit à l'oubli

**VISUEL :** un badge « RGPD » apparaît. Le formulaire Google « Droit à l'oubli » se remplit tout seul : pièce d'identité jointe, liste d'URLs précises, justification. Quatre mots-clés s'empilent : **inexact**, **périmé**, **non pertinent**, **excessif**.

**VOIX OFF :**
> Pas de réponse ? Vous avez un droit : le **droit à l'oubli**, renforcé par le RGPD.
> Il vous permet de demander à Google de ne plus associer votre nom à certaines pages.
> Pour cela, on remplit le formulaire officiel de Google, avec une pièce d'identité, la liste **exacte** des URLs concernées et une justification solide.
> Google accepte quand l'information est inexacte, périmée, non pertinente ou excessive.

### 4c. Le piège à éviter

**VISUEL :** panneau « ⚠️ ATTENTION ». Icône de l'outil « Contenu obsolète » barrée sur une page encore en ligne, puis validée sur une page déjà modifiée.

**VOIX OFF :**
> Attention à un piège classique : l'outil « contenu obsolète » de Google ne sert **pas** à déréférencer une page toujours en ligne.
> Il sert seulement quand le site a déjà modifié ou supprimé la page, mais que l'ancienne version traîne encore dans les résultats.

---

## 5. Et si Google refuse ? (2:15 à 2:35)

**VISUEL :** un tampon « REFUSÉ » s'abat sur le formulaire. Une flèche mène au logo stylisé de la CNIL, puis à un marteau de justice. Le tampon se transforme en « DÉRÉFÉRENCÉ ».

**VOIX OFF :**
> Et si Google dit non ? Ce n'est pas fini.
> Vous pouvez saisir la **CNIL**. Si elle juge votre plainte légitime, elle peut obliger le moteur de recherche à déréférencer le lien.

---

## 6. Récap + CTA (2:35 à 2:55)

**VISUEL :** les 3 étapes se résument en icônes alignées : 🔑 mon site (404/410, noindex, Search Console), ✉️ site tiers (contact puis formulaire droit à l'oubli), ⚖️ refus (CNIL). La page Google réapparaît… sans le résultat rouge. Le logo de l'agence s'affiche ensuite.

**VOIX OFF :**
> En résumé : votre site, vous agissez directement. Un site tiers, vous contactez, puis vous activez votre droit à l'oubli. Un refus, vous saisissez la CNIL.
> Pour aller plus loin, avec les modèles d'e-mails et la checklist complète, retrouvez notre article en lien juste en dessous.

---

## Notes de production

- **Mots à appuyer à l'enregistrement :** déréférencer / supprimer, 410, noindex, droit à l'oubli, CNIL.
- **Textes à l'écran :** reprendre les mots-clés en gras plutôt que des phrases entières.
- **Vérification avant diffusion :** relire les intitulés exacts des formulaires et des menus Google (Search Console, Droit à l'oubli), qui changent régulièrement.
