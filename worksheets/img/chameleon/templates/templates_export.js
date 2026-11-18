// Export every template in u03_chameleon_templates.html as a transparent 2040 x 2640 PNG (letter at 240 dpi).
//   node img/chameleon/templates/templates_export.js
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const src = 'file://' + path.resolve(__dirname, '../../../u03_chameleon_templates.html') + '?export';
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2.5 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto(src);
  for (const el of await p.$$('.page')) {
    const id = await el.getAttribute('id');
    await el.screenshot({ path: path.join(__dirname, `template_${id}.png`), omitBackground: true });
  }
  await b.close();
  if (errs.length) { console.error(errs); process.exit(1); }
  console.log('ok');
})();
