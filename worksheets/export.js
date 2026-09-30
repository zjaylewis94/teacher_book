// Export a worksheet to a print-ready letter PDF (and a PNG preview of its own page).
//   node export.js tunnel_book_scene.html --front img/tunnel_book_howto.webp --out pdf/tunnel_book
// --front puts an existing sheet (e.g. a hand-drawn how-to page) on page 1, so the PDF prints double-sided.
// Playwright is preinstalled in Claude's cloud sessions; locally: npm i playwright.
const path = require('path');
const { chromium } = require('playwright');

const args = process.argv.slice(2);
const src = path.resolve(__dirname, args[0]);
const opt = k => { const i = args.indexOf(k); return i > -1 ? args[i + 1] : null; };
const out = path.resolve(__dirname, opt('--out') || path.join('pdf', path.basename(src, '.html')));
const front = opt('--front');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2 });
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto('file://' + src);
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });

  const overflow = await page.evaluate(() => [...document.querySelectorAll('.frame')].map(f => f.scrollHeight - f.clientHeight));
  if (overflow.some(n => n > 0)) errors.push('content runs past the frame by ' + overflow.join(', ') + 'px');

  await page.screenshot({ path: out + '.png', clip: { x: 0, y: 0, width: 816, height: 1056 } });

  if (front) {
    const url = 'file://' + path.resolve(__dirname, front);
    await page.evaluate(url => {
      const d = document.createElement('div');
      d.className = 'page';
      d.style.padding = '0';
      d.innerHTML = `<img src="${url}" style="width:100%;height:100%;display:block;object-fit:contain">`;
      document.body.prepend(d);
      return new Promise(r => d.querySelector('img').complete ? r() : d.querySelector('img').onload = r);
    }, url);
  }
  await page.pdf({ path: out + '.pdf', format: 'Letter', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();

  if (errors.length) { console.error('Problems:\n- ' + errors.join('\n- ')); process.exit(1); }
  console.log('Wrote', path.relative(process.cwd(), out) + '.pdf', 'and .png');
})();
