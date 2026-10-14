// Rendu des miniatures du test A/B/C « Retirer une page de Google » (1280x720).
// Usage, depuis n'importe où :
//   node video/miniatures-desindexation/render.mjs          (rend a, b et c)
//   node video/miniatures-desindexation/render.mjs b        (rend une seule miniature)
// Sortie : miniature-a.png, miniature-b.png, miniature-c.png à côté des fichiers HTML.
// Chaque PNG doit rester sous 2 Mo (limite YouTube) : le script le vérifie.
import { chromium } from 'playwright-core';
import { statSync } from 'node:fs';
import path from 'node:path';

const dir = path.dirname(new URL(import.meta.url).pathname);
const lettres = process.argv.slice(2).length ? process.argv.slice(2) : ['a', 'b', 'c'];
const LIMITE = 2 * 1024 * 1024;

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--allow-file-access-from-files', '--font-render-hinting=none'],
});
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('ERREUR PAGE', e.message));
page.on('requestfailed', r => console.error('RESSOURCE MANQUANTE', r.url()));

let echec = false;
for (const l of lettres) {
  await page.goto('file://' + path.join(dir, `miniature-${l}.html`));
  await page.evaluate(() => (window.ready || Promise.resolve()).then(() => document.fonts.ready));
  const sortie = path.join(dir, `miniature-${l}.png`);
  await page.screenshot({ path: sortie });
  const taille = statSync(sortie).size;
  const ok = taille < LIMITE;
  if (!ok) echec = true;
  console.log(`${path.basename(sortie)} : ${(taille / 1024).toFixed(0)} Ko ${ok ? 'OK' : 'TROP LOURD (limite 2 Mo)'}`);
}
await browser.close();
process.exit(echec ? 1 : 0);
