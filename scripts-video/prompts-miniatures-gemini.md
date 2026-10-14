# Prompts Gemini : miniatures du test A/B/C « Retirer une page de Google »

Trois prompts pour générer les miniatures du test A/B/C avec Gemini (génération d'images), un par hypothèse du plan `abc-test-desindexation.md`. Les titres YouTube ne changent pas.

## Mode d'emploi

- **Prompts en anglais :** les modèles d'image les suivent mieux. Le texte à afficher reste en français, entre guillemets.
- **Format :** demander du 16:9. Exporter ou recadrer en 1280 x 720, moins de 2 Mo.
- **Logo 410 Gone :** les modèles déforment les logos. Ne pas demander le logo dans l'image : l'ajouter au montage (Canva, Figma, Photoshop) avec le fichier officiel `video/desindexation/assets/logo-410gone-blanc.svg`. Les prompts demandent seulement un polo indigo uni, avec un emplacement libre sur la poitrine pour l'ajouter.
- **Texte dans l'image :** Gemini écrit correctement les mots courts, pas toujours les accents. Vérifier chaque lettre. En cas de faute, générer l'image sans texte (retirer la ligne « Text ») et poser le texte au montage en Montserrat ExtraBold.
- **Personne à l'image :** les prompts décrivent une personne générique. Pour mettre un membre de l'équipe, joindre sa photo comme référence, avec son accord, et ajouter « Use the person in the reference photo ».
- **Google :** pas de logo ni de couleurs de Google. Une page de résultats générique suffit et évite d'imiter la marque.
- **Itérer :** générer 4 variantes par prompt, garder la meilleure, puis corriger par petites consignes (« make the text bigger », « more contrast on the face »).

Couleurs de la charte, répétées dans chaque prompt : indigo #31249F, indigo profond #201A64, orange #FFB400.

---

## A : « Dehors ! », la page qui sort de Google

**Hypothèse :** montrer le résultat obtenu avec un visage qui réagit.

```
Professional YouTube thumbnail, 16:9, 1280x720, high-end tech channel style, photographic with subtle 3D elements.

Subject: on the right third, a friendly French web consultant in his thirties, short brown hair, modern glasses, wearing a plain deep indigo polo shirt (#31249F) with a clean empty area on the chest. Waist-up, three-quarter view, confident satisfied grin, one hand making a flicking "get out" gesture toward the left. Sharp focus on the face, expressive eyes, studio key light with a warm orange rim light (#FFB400) on his shoulder and hair.

Left side: a floating white search results panel in perspective, generic search engine (no logo, no brand colors), three result cards. The middle result card is being violently ejected out of the list toward the viewer, tilted, with motion blur and small paper debris, outlined with a bright orange glow (#FFB400). An empty dashed slot remains where it was.

Background: deep indigo gradient (#201A64 to #31249F), soft bokeh, subtle depth, no clutter.

Text: top left, huge bold sans-serif headline "Dehors !" in bright orange (#FFB400) with a thin dark shadow, perfectly spelled, French.

Composition: three elements only (person, ejected result, headline). Keep the bottom right corner free of important details. High contrast, readable at small size, crisp, premium, no watermark, no extra text.
```

---

## B : le tampon « 410 », pas 404

**Hypothèse :** la réponse technique, mise en scène pour être comprise sans connaître les codes HTTP.

```
Professional YouTube thumbnail, 16:9, 1280x720, bold editorial 3D style, cinematic lighting.

Subject: a white web page document floating at an angle on the left, realistic paper texture, with blurred placeholder lines. A heavy rubber stamp has just slammed onto it, leaving a big bold "410" stamp mark in bright orange ink (#FFB400), slightly rotated, with a tiny ink splash and a dramatic impact shadow. The wooden-and-metal rubber stamp is still lifting off above the page, with motion blur.

Right side: a large white "404" in bold sans-serif, crossed out with a thick hand-drawn orange stroke (#FFB400), and the word "Pas" above it in white. Perfectly spelled, French.

Background: deep indigo gradient (#201A64 to #31249F) with soft radial light behind the page, subtle depth.

Composition: three elements only (stamped page, stamp, crossed-out 404). Keep the bottom right corner free of important details. High contrast, readable at small size, crisp, premium, no logos, no watermark, no extra text.
```

---

## C : « Toujours là ? », la page supprimée qui reste dans Google

**Hypothèse :** le spectateur se reconnaît dans son problème.

```
Professional YouTube thumbnail, 16:9, 1280x720, high-end tech channel style, photographic with subtle 3D elements.

Subject: on the right, a French business owner in her thirties, wearing a plain deep indigo polo shirt (#31249F) with a clean empty area on the chest, holding a laptop, looking at the screen with a shocked, disbelieving expression (raised eyebrows, open mouth), studio lighting with an orange rim light (#FFB400).

Left side: a large floating search result card from a generic search engine (no logo, no brand colors), white, slightly tilted, showing the title "Catalogue 2019" in bold dark indigo. It is circled with a thick hand-drawn orange marker stroke (#FFB400). Next to it, a small white trash bin icon with an orange check mark badge, meaning the page was already deleted.

Background: deep indigo gradient (#201A64 to #31249F), soft bokeh, subtle depth.

Text: top left, huge bold white sans-serif headline "Toujours là ?" with the question mark in orange, perfectly spelled with the accent on "là", French.

Composition: three elements only (headline, circled result, person). Keep the bottom right corner free of important details. High contrast, readable at small size, crisp, premium, no watermark, no extra text.
```

---

## Avant de valider

- Regarder chaque miniature réduite à 320 x 180 : le sujet doit se comprendre sans lire le petit texte.
- Vérifier l'orthographe et les accents (« Dehors ! », « Pas 404 », « Toujours là ? ») et l'espace avant « ! » et « ? ».
- Vérifier qu'aucun logo ni aucune couleur de Google n'est apparu, et qu'aucun texte parasite n'a été inventé.
- Ajouter le logo 410 Gone sur le polo (A et C) au montage, à partir du fichier officiel.
- Si des personnes générées apparaissent, garder un style crédible mais sans ressemblance voulue avec une personne réelle.
