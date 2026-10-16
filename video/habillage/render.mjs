// Rendu de l'habillage 410 Gone (ouverture et écran de fin), même principe que build/render.mjs.
// Usage :
//   node habillage/render.mjs open "Titre de la vidéo" "Sous-titre" sortie.mp4 [tenue en secondes]
//   node habillage/render.mjs fin sortie.mp4
//   node habillage/render.mjs stills open|fin t1,t2,... [guides]
import { chromium } from 'playwright-core';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import path from 'node:path';
const FPS = 30;
const dir = path.dirname(new URL(import.meta.url).pathname);
const args = process.argv.slice(2);
let mode, params = new URLSearchParams({ render: '' }), out, times;
if (args[0] === 'stills') {
  [, mode] = args; times = args[2].split(',').map(Number);
  if (args[3] === 'guides') params.set('guides', '');
} else if (args[0] === 'open') {
  mode = 'open'; params.set('titre', args[1]); params.set('sous', args[2] || ''); out = args[3];
  if (args[4]) params.set('tenue', args[4]);
} else {
  mode = 'fin'; out = args[1];
}
params.set('mode', mode);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--allow-file-access-from-files', '--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e.message));
await page.goto('file://' + dir + '/habillage.html?' + params.toString());
await page.evaluate(() => window.ready);
if (times) {
  mkdirSync(dir + '/stills', { recursive: true });
  for (const t of times) {
    await page.evaluate(t => window.seek(t), t);
    await page.screenshot({ path: `${dir}/stills/${mode}-${t}.png` });
  }
} else {
  const total = Math.round(await page.evaluate(() => window.DURATION) * FPS);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.seek(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
}
await browser.close();
