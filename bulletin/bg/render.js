const { chromium } = require('playwright');
const path = require('path');
const days = {
  mon: { a: '#ED0A3F,#FF8833,#FBE870', paper: '#FFF8E7', tex: '#F1E3C2', seed: 11 },
  tue: { a: '#0066FF,#76D7EA,#FBE870', paper: '#F3F8FF', tex: '#D9E6F7', seed: 23 },
  wed: { a: '#01A368,#C5E17A,#FF8833', paper: '#F5FBEF', tex: '#DCEBCC', seed: 37 },
  thu: { a: '#8359A3,#F7468A,#76D7EA', paper: '#FAF5FF', tex: '#E7DAF2', seed: 41 },
  fri: { a: '#FF8833,#F7468A,#01A368', paper: '#FFF5EC', tex: '#F3DDC8', seed: 53 },
};
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const [k, v] of Object.entries(days)) {
    const u = 'file://' + path.resolve('backgrounds.html') + '?' + new URLSearchParams(v);
    await p.goto(u); await p.waitForFunction(() => document.title === 'ready');
    await p.screenshot({ path: `bulletin_bg_${k}.png` });
    await p.screenshot({ path: `bulletin_bg_${k}.jpg`, type: 'jpeg', quality: 88 });
  }
  await b.close();
})();
