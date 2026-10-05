// Rendu image par image : seek déterministe de la timeline GSAP + capture Chromium.
// Usage : node build/render.mjs stills t1,t2,...   |   node build/render.mjs video <worker> <workers>
import { chromium } from 'playwright-core';
import { spawn } from 'node:child_process';
import path from 'node:path';
const FPS = 30;
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const [mode, a, b] = process.argv.slice(2);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--allow-file-access-from-files', '--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e.message));
await page.goto('file://' + root + '/index.html?render');
await page.evaluate(() => window.ready);
const dur = await page.evaluate(() => window.DURATION);
if (mode === 'stills') {
  for (const t of a.split(',').map(Number)) {
    await page.evaluate(t => window.seek(t), t);
    await page.screenshot({ path: `${root}/build/stills/t${String(t).padStart(6, '0')}.png` });
  }
} else {
  const w = +a, n = +b, total = Math.ceil(dur * FPS);
  const from = Math.floor(total * w / n), to = Math.floor(total * (w + 1) / n);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', `${root}/build/part${w}.mp4`], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = from; f < to; f++) {
    await page.evaluate(t => window.seek(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 300 === 0) console.log(`worker ${w}: ${f}/${to}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
}
await browser.close();
