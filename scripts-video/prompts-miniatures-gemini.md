# Prompts Gemini : miniatures du test A/B/C « Retirer une page de Google »

Trois prompts pour générer avec Gemini les miniatures du test A/B/C, une par hypothèse du plan `abc-test-desindexation.md`. Patrick y est mis en situation à partir de sa photo, en polo 410 Gone. Les titres YouTube ne changent pas.

## Images à joindre à chaque prompt

Dans `video/miniatures-desindexation/references/` :

1. `patrick.png` : la photo de référence de Patrick (détourée).
2. `logo-410gone-blanc-sur-indigo.png` : le logo à broder sur le polo, tel qu'il doit apparaître sur un tissu indigo.

Joindre les deux images dans cet ordre : les prompts parlent de « image 1 » et « image 2 ».

## Mode d'emploi

- **Prompts en anglais :** Gemini les suit mieux. Le texte à afficher reste en français, entre guillemets.
- **Format :** demander du 16:9, puis exporter ou recadrer en 1280 x 720, moins de 2 Mo.
- **Ressemblance :** chaque prompt demande de garder le visage à l'identique. Comparer avec la photo d'origine : si le visage dérive (barbe, lunettes, forme du visage), relancer avec « Keep his face exactly identical to image 1 ».
- **Logo sur le polo :** vérifier qu'il est complet et sans faute (« 410 », « GONE », les deux équerres). Gemini déforme souvent les logos. Si c'est le cas, demander « Make the chest logo an exact copy of image 2 », ou effacer le logo généré et poser le vrai au montage avec `logo-410gone-blanc.png` (fond transparent).
- **Ancien logo :** la photo d'origine porte le logo « Domaine du Gouverneur » sur la poitrine et « FJ » sur le col. Vérifier qu'il n'en reste rien.
- **Texte dans l'image :** vérifier chaque lettre et les accents. En cas de faute, générer sans texte (supprimer le paragraphe « Text ») et poser le texte au montage en Montserrat ExtraBold.
- **Google :** pas de logo ni de couleurs de Google. Une page de résultats générique suffit et évite d'imiter la marque.
- **Itérer :** générer plusieurs variantes par prompt, garder la meilleure, puis corriger par petites consignes (« make the headline bigger », « more contrast on his face »).

Couleurs de la charte, répétées dans chaque prompt : indigo #31249F, indigo profond #201A64, orange #FFB400.

## Bloc commun (déjà inclus dans chaque prompt)

```
Use the man in image 1 as the only person. Keep his face, beard, glasses, hairstyle, skin tone and identity exactly identical to image 1. Change only his pose, expression and clothing as described. He wears a deep indigo polo shirt (#31249F), same cut as in image 1, with an orange (#FFB400) inner collar trim. Remove every existing logo and text from his clothes, including the chest logo and the collar logo. On the left chest, add the logo from image 2, embroidered in white thread, small and perfectly legible, exact copy of the shapes in image 2.
```

---

## A : « Dehors ! », la page qui sort de Google

**Hypothèse :** montrer le résultat obtenu, avec un visage qui réagit.

```
Professional YouTube thumbnail, 16:9, 1280x720, high-end tech channel style, photographic with subtle 3D elements.

Use the man in image 1 as the only person. Keep his face, beard, glasses, hairstyle, skin tone and identity exactly identical to image 1. Change only his pose, expression and clothing as described. He wears a deep indigo polo shirt (#31249F), same cut as in image 1, with an orange (#FFB400) inner collar trim. Remove every existing logo and text from his clothes, including the chest logo and the collar logo. On the left chest, add the logo from image 2, embroidered in white thread, small and perfectly legible, exact copy of the shapes in image 2.

Pose and expression: he stands on the right third, waist-up, three-quarter view toward the left, big confident satisfied grin, one hand making a flicking "get out" gesture toward the left. Sharp focus on his face, studio key light, warm orange rim light (#FFB400) on his shoulder and hair.

Left side: a floating white search results panel in perspective, generic search engine (no logo, no brand colors), three result cards. The middle card, titled "Catalogue 2019", is being violently ejected out of the list toward the viewer, tilted, with motion blur and small paper debris, outlined with a bright orange glow (#FFB400). An empty dashed slot remains where it was.

Background: deep indigo gradient (#201A64 to #31249F), soft bokeh, subtle depth, no clutter.

Text: top left, huge bold sans-serif headline "Dehors !" in bright orange (#FFB400) with a thin dark shadow, perfectly spelled, French.

Composition: three elements only (the man, the ejected result, the headline). Keep the bottom right corner free of important details. High contrast, readable at small size, crisp, premium, no watermark, no extra text.
```

---

## B : le tampon « 410 », pas 404

**Hypothèse :** la réponse technique, mise en scène pour être comprise sans connaître les codes HTTP.

```
Professional YouTube thumbnail, 16:9, 1280x720, bold editorial style, photographic with cinematic lighting.

Use the man in image 1 as the only person. Keep his face, beard, glasses, hairstyle, skin tone and identity exactly identical to image 1. Change only his pose, expression and clothing as described. He wears a deep indigo polo shirt (#31249F), same cut as in image 1, with an orange (#FFB400) inner collar trim. Remove every existing logo and text from his clothes, including the chest logo and the collar logo. On the left chest, add the logo from image 2, embroidered in white thread, small and perfectly legible, exact copy of the shapes in image 2.

Pose and expression: he stands on the left, waist-up, facing the camera, determined smile, slamming a big rubber stamp down onto a white web page document floating in front of him. The page shows the title "Catalogue 2019" and blurred placeholder lines. The stamp leaves a big bold "410" mark in bright orange ink (#FFB400), slightly rotated, with a small ink splash and a dramatic impact shadow.

Right side: a large white "404" in bold sans-serif, crossed out with a thick hand-drawn orange stroke (#FFB400), with the word "Pas" above it in white. Perfectly spelled, French.

Background: deep indigo gradient (#201A64 to #31249F), soft radial light behind the man, subtle depth.

Composition: three elements only (the man with the stamp, the stamped page, the crossed-out 404). Keep the bottom right corner free of important details. High contrast, readable at small size, crisp, premium, no other logos, no watermark, no extra text.
```

---

## C : « Toujours là ? », la page supprimée qui reste dans Google

**Hypothèse :** le spectateur se reconnaît dans son problème.

```
Professional YouTube thumbnail, 16:9, 1280x720, high-end tech channel style, photographic with subtle 3D elements.

Use the man in image 1 as the only person. Keep his face, beard, glasses, hairstyle, skin tone and identity exactly identical to image 1. Change only his pose, expression and clothing as described. He wears a deep indigo polo shirt (#31249F), same cut as in image 1, with an orange (#FFB400) inner collar trim. Remove every existing logo and text from his clothes, including the chest logo and the collar logo. On the left chest, add the logo from image 2, embroidered in white thread, small and perfectly legible, exact copy of the shapes in image 2.

Pose and expression: he stands on the right third, waist-up, holding an open laptop, looking from the screen toward the camera with a shocked, disbelieving expression (raised eyebrows, mouth slightly open). Studio key light, orange rim light (#FFB400).

Left side: a large floating search result card from a generic search engine (no logo, no brand colors), white, slightly tilted, showing the title "Catalogue 2019" in bold dark indigo. It is circled with a thick hand-drawn orange marker stroke (#FFB400). Next to it, a small white trash bin icon with an orange check mark badge, meaning the page was already deleted.

Background: deep indigo gradient (#201A64 to #31249F), soft bokeh, subtle depth.

Text: top left, huge bold white sans-serif headline "Toujours là ?" with the question mark in orange, perfectly spelled with the accent on "là", French.

Composition: three elements only (the headline, the circled result, the man). Keep the bottom right corner free of important details. High contrast, readable at small size, crisp, premium, no watermark, no extra text.
```

---

## Avant de valider

- Comparer le visage de chaque miniature avec `patrick.png` : barbe, lunettes, forme du visage.
- Vérifier le logo du polo : « 410 », « GONE », les deux équerres, sans faute ni lettre inventée, et plus aucune trace de l'ancien logo.
- Regarder chaque miniature réduite à 320 x 180 : le sujet doit se comprendre sans lire le petit texte.
- Vérifier l'orthographe et les accents (« Dehors ! », « Pas 404 », « Toujours là ? ») et l'espace avant « ! » et « ? ».
- Vérifier qu'aucun logo ni aucune couleur de Google n'est apparu, et qu'aucun texte parasite n'a été ajouté.
- Faire valider les trois images par Patrick avant publication.
