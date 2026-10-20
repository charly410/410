// Captures « preuves » : pages réelles de la documentation Google, cadrées sur la phrase citée.
// Usage (depuis video/desindexation-rush) : node build/preuves.mjs
// Écrit assets/preuves/<nom>.png (1920 x 1080), assets/preuves/preuves.json et assets/preuves/preuves.js
// (window.PREUVES_BOX : cadre de la phrase en pixels de l'image, lu par compositions/preuves.html).
// Page affichée sur 1200 x 675 avec une densité de 1,6 : le texte sort assez gros pour être lu en vidéo.
import { chromium } from 'playwright-core';
import { writeFileSync } from 'node:fs';

const PREUVES = [
  { nom: 'noindex-robots', url: 'https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=fr', texte: 'ne doit pas' },
  { nom: 'suppressions-6-mois', url: 'https://support.google.com/webmasters/answer/9689846?hl=fr', texte: 'six mois' },
];

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const DPR = 1.6;
const p = await b.newPage({ viewport: { width: 1200, height: 675 }, deviceScaleFactor: DPR, locale: 'fr-FR' });
const sortie = {};
for (const q of PREUVES) {
  await p.goto(q.url, { waitUntil: 'networkidle', timeout: 90000 });
  // ferme les bandeaux de cookies éventuels
  for (const t of ['OK, j\'ai compris', 'Tout accepter', 'J\'accepte', 'OK']) {
    const bt = p.getByRole('button', { name: t }).first();
    if (await bt.isVisible().catch(() => false)) { await bt.click().catch(() => {}); break; }
  }
  // le plus petit bloc qui contient la phrase
  const h = await p.evaluateHandle((txt) => {
    const all = [...document.querySelectorAll('aside, p, li, td, div')].filter((e) => e.innerText && e.innerText.includes(txt));
    all.sort((a, c) => a.innerText.length - c.innerText.length);
    return all[0];
  }, q.texte);
  await h.evaluate((e) => e.scrollIntoView({ block: 'center' }));
  await p.waitForTimeout(800);
  const box = await h.boundingBox();
  await p.screenshot({ path: `assets/preuves/${q.nom}.png` });
  sortie[q.nom] = { url: q.url, texte: q.texte, x: Math.round(box.x * DPR), y: Math.round(box.y * DPR), w: Math.round(box.width * DPR), h: Math.round(box.height * DPR) };
  console.log(q.nom, sortie[q.nom]);
}
writeFileSync('assets/preuves/preuves.json', JSON.stringify(sortie, null, 2));
writeFileSync('assets/preuves/preuves.js', '// FICHIER GÉNÉRÉ par build/preuves.mjs\nwindow.PREUVES_BOX = ' + JSON.stringify(sortie) + ';\n');
await b.close();
