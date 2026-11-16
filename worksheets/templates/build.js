// Layout guides for Photoshop. Each template is a transparent 2550 x 3300 px PNG (US Letter at 300 dpi):
// blue guide boxes inside a dashed 0.25 in print-safe line. Put it on a top layer, build the page by hand
// underneath, then hide the layer before printing. Run: node build.js
const path = require('path');
const { chromium } = require('playwright');
const H = [0, 0, 8, 1.2, 'TITLE  ·  unit line'];           // header used by most templates
// Zones are [x, y, w, h, label] in inches, measured from the print-safe corner (safe area = 8 x 10.5 in).
const T = {
  '01_stacked_sections': ['Stacked sections', 'Wordy, straightforward instructions', [H, [0, 1.35, 8, 0.9, 'intro: what + why'],
    [0, 2.4, 8, 2.6, '01 section'], [0, 5.15, 8, 2.6, '02 section'], [0, 7.9, 8, 2.6, '03 section']]],
  '02_text_left_art_right': ['Text left, art right', 'One big demonstration with steps beside it', [H,
    [0, 1.35, 3.3, 2.9, 'step 1'], [0, 4.4, 3.3, 2.9, 'step 2'], [0, 7.45, 3.3, 3.05, 'step 3'], [3.45, 1.35, 4.55, 9.15, 'BIG DEMO / ART']]],
  '03_hero_with_notes': ['Hero with notes around it', 'Rules or tips pointing at one drawing', [H, [2.1, 1.4, 3.8, 5.7, 'HERO DRAWING'],
    ...[0, 1, 2, 3].flatMap(i => [[0, 1.4 + i * 1.45, 1.95, 1.3, 'note'], [6.05, 1.4 + i * 1.45, 1.95, 1.3, 'note']]),
    ...[0, 1, 2, 3].map(i => [i * 2.04, 7.3, 1.88, 1.4, 'note']), [0, 8.9, 8, 1.6, 'kit / reminder strip']]],
  '04_step_strip_practice': ['Step strip + practice', 'Show it in 4 steps, then they try it', [H, [0, 1.35, 8, 0.75, 'intro'],
    ...[0, 1, 2, 3].map(i => [i * 2.04, 2.25, 1.88, 2.7, 'step ' + (i + 1)]), [0, 5.1, 8, 5.4, 'STUDENT WORKSPACE']]],
  '05_comic_panels': ['Comic panels', 'A process told as a story, uneven panels', [[0, 0, 8, 0.9, 'TITLE'],
    [0, 1.05, 4.8, 3, 'panel 1'], [4.95, 1.05, 3.05, 3, 'panel 2'], [0, 4.2, 2.6, 3, 'panel 3'], [2.75, 4.2, 5.25, 3, 'panel 4'], [0, 7.35, 8, 3.15, 'panel 5: the payoff']]],
  '06_know_your_tool': ['Know your tool', 'Unit intro: the kit, how it behaves, vocab', [[0, 0, 6.2, 1.2, 'TITLE  ·  unit line'], [6.35, 0, 1.65, 1.2, 'icon'],
    [0, 1.35, 8, 0.75, 'intro'], ...[0, 1, 2, 3, 4, 5].map(i => [(i % 3) * 2.72, 2.25 + Math.floor(i / 3) * 1.15, 2.56, 1, 'tool']),
    ...[0, 1, 2, 3].map(i => [i * 2.04, 4.7, 1.88, 1.9, 'how it behaves']), [0, 6.75, 8, 0.8, 'golden rule'],
    [0, 7.7, 8, 0.9, 'example strip'], [0, 8.75, 3.9, 1.75, 'vocab'], [4.1, 8.75, 3.9, 1.75, 'vocab']]],
  '07_practice_page': ['Practice page', 'Mostly workspace, a little instruction', [H, [0, 1.35, 8, 1.1, 'what to do'],
    [0, 2.6, 8, 6.4, 'STUDENT WORKSPACE'], [0, 9.15, 8, 1.35, 'reflection lines']]],
  '08_cover_page': ['Cover page', 'Project cover: big title, one image', [[0, 0, 8, 2.2, 'BIG TITLE'], [0.5, 2.4, 7, 5.6, 'HERO IMAGE'],
    ...[0, 1, 2].map(i => [i * 2.72, 8.2, 2.56, 1.1, ['unit', 'tier', 'points'][i]]), [0, 9.45, 8, 1.05, 'one-line hook']]],
  '09_project_page': ['Project page', 'What it looks like, rules, steps, grading', [H, [0, 1.35, 3, 3.2, 'example'],
    ...[0, 1, 2, 3].map(i => [3.15 + (i % 2) * 2.5, 1.35 + Math.floor(i / 2) * 1.68, 2.35, 1.52, 'idea']),
    [0, 4.7, 4.6, 2, 'the rules'], [4.75, 4.7, 3.25, 2, 'callout'], ...[0, 1, 2, 3, 4].map(i => [i * 1.63, 6.85, 1.48, 1.5, 'step ' + (i + 1)]), [0, 8.5, 8, 2, 'how it is graded']]],
  '10_compare': ['Do / don\'t', 'Right vs wrong, then a close-up, then try it', [H, [0, 1.35, 3.9, 4, 'DO'], [4.1, 1.35, 3.9, 4, 'DON\'T'],
    ...[0, 1, 2].map(i => [i * 2.72, 5.5, 2.56, 2.2, 'close-up']), [0, 7.85, 8, 2.65, 'STUDENT WORKSPACE']]]
};
const page = (name, [title, use, zones], bg) => `<!doctype html><html><body style="margin:0;background:${bg}">
<svg xmlns="http://www.w3.org/2000/svg" width="816" height="1056" viewBox="0 0 8.5 11" font-family="Arial, Helvetica, sans-serif">
  <rect x=".25" y=".25" width="8" height="10.5" fill="none" stroke="#E6007E" stroke-width=".012" stroke-dasharray=".08 .06"/>
  <path d="M4.25 .1 V.22 M4.25 10.78 V10.9 M.1 5.5 H.22 M8.28 5.5 H8.4" stroke="#E6007E" stroke-width=".012"/>
  ${zones.map(([x, y, w, h, l]) => `<rect x="${(x + .25).toFixed(3)}" y="${(y + .25).toFixed(3)}" width="${w}" height="${h}" rx=".06" fill="#1F9BD8" fill-opacity=".06" stroke="#1F9BD8" stroke-width=".014"/>
    <text x="${(x + .25 + .07).toFixed(3)}" y="${(y + .25 + .17).toFixed(3)}" font-size=".11" fill="#1F9BD8">${l}</text>`).join('')}
  <text x=".25" y=".19" font-size=".1" fill="#E6007E">${name.slice(0, 2)}  ${title}: ${use}  ·  dashed line = 0.25 in print-safe edge  ·  hide this layer before printing</text>
</svg></body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 3.125 });
  for (const [name, t] of Object.entries(T)) {
    await p.setContent(page(name, t, 'transparent'));
    await p.screenshot({ path: path.join(__dirname, name + '.png'), omitBackground: true });
  }
  // contact sheet for a quick look
  const q = await b.newPage({ viewport: { width: 5 * 280 + 40, height: 2 * 372 + 40 }, deviceScaleFactor: 1.5 });
  await q.setContent(`<body style="margin:20px;background:#eee;display:grid;grid-template-columns:repeat(5,270px);gap:10px">${Object.entries(T).map(([n, t]) =>
    `<div style="background:#fff;box-shadow:0 1px 4px #0003;width:270px;height:349px;overflow:hidden"><div style="transform:scale(.3309);transform-origin:0 0;width:816px;height:1056px">${page(n, t, '#fff').replace(/<\/?(html|body)[^>]*>|<!doctype html>/g, '')}</div></div>`).join('')}</body>`);
  await q.screenshot({ path: path.join(__dirname, 'contact_sheet.png') });
  // one PDF of all ten, on white, with an index page, to keep in Drive
  const r = await b.newPage();
  const idx = `<div style="width:8.5in;height:11in;padding:.6in;box-sizing:border-box;font-family:Arial,Helvetica,sans-serif;page-break-after:always">
    <h1 style="font-size:30px;margin:0 0 6px">Mr. Lewis worksheet layout guides</h1>
    <p style="font-size:14px;line-height:1.45;margin:0 0 18px">Ten letter-size guides for building worksheets by hand in Photoshop. Open the matching PNG (2550 × 3300 px, 300 dpi,
      transparent) as the top layer, build the page underneath, then hide the layer before printing. Blue boxes are zones. The dashed pink line is the 0.25 in print-safe edge.</p>
    <table style="border-collapse:collapse;font-size:14px;width:100%">${Object.entries(T).map(([n, [title, use]]) =>
      `<tr><td style="border-bottom:1px solid #ccc;padding:7px 8px;width:36px"><b>${n.slice(0, 2)}</b></td><td style="border-bottom:1px solid #ccc;padding:7px 8px;width:210px"><b>${title}</b></td><td style="border-bottom:1px solid #ccc;padding:7px 8px">${use}</td><td style="border-bottom:1px solid #ccc;padding:7px 8px;color:#777;font-size:12px">${n}.png</td></tr>`).join('')}</table>
    <p style="font-size:13px;color:#555;margin-top:18px">First draft, Nov 16, 2026. Based on the layouts already used and common worksheet and comic structures. Add to it as you collect references.</p></div>`;
  await r.setContent(`<style>@page{size:letter;margin:0}body{margin:0}</style>` + idx + Object.entries(T).map(([n, t]) =>
    `<div style="width:8.5in;height:11in;page-break-after:always">${page(n, t, '#fff').replace(/<\/?(html|body)[^>]*>|<!doctype html>/g, '')}</div>`).join(''));
  await r.pdf({ path: path.join(__dirname, 'layout_guides.pdf'), format: 'Letter', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close(); console.log('built', Object.keys(T).length, 'templates');
})();
