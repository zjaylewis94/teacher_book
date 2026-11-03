// Brush strokes for the Unit 12 Sumi-e sheets.
// A stroke is a curve (start, bend, end) with a width at the start, middle and end,
// so it can press and lift like a real brush. Fills are grays that survive a B&W copier.
const SUMI = (() => {
  const INK = { burnt: '#111', dark: '#3a3a3a', mid: '#6e6e6e', light: '#a8a8a8', clear: '#d4d4d4' };

  // Point and slope on a quadratic curve at t
  function at(p0, p1, p2, t) {
    const u = 1 - t;
    return {
      x: u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
      y: u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1],
      dx: 2 * u * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
      dy: 2 * u * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]),
    };
  }
  // Width along the stroke: eases between start, middle and end widths
  function width(w, t) {
    const [a, b, c] = w;
    return t < 0.5 ? a + (b - a) * Math.sin(t * Math.PI) : c + (b - c) * Math.sin(t * Math.PI);
  }

  // One brush stroke as a filled path. `fill` is a color or a url(#gradient).
  function stroke(p0, p1, p2, w, fill = INK.burnt, extra = '') {
    const n = 28, L = [], R = [];
    for (let i = 0; i <= n; i++) {
      const t = i / n, p = at(p0, p1, p2, t), len = Math.hypot(p.dx, p.dy) || 1;
      const h = width(w, t) / 2, nx = -p.dy / len * h, ny = p.dx / len * h;
      L.push(`${(p.x + nx).toFixed(1)} ${(p.y + ny).toFixed(1)}`);
      R.push(`${(p.x - nx).toFixed(1)} ${(p.y - ny).toFixed(1)}`);
    }
    return `<path d="M${L.join(' L')} L${R.reverse().join(' L')} Z" fill="${fill}" ${extra}/>`;
  }

  // A gradient that runs along a stroke, dark tip to light belly (a "loaded" brush)
  function loaded(id, p0, p2, from = INK.burnt, to = INK.light) {
    return `<linearGradient id="${id}" gradientUnits="userSpaceOnUse" x1="${p0[0]}" y1="${p0[1]}" x2="${p2[0]}" y2="${p2[1]}">
      <stop offset="0" stop-color="${from}"/><stop offset="1" stop-color="${to}"/></linearGradient>`;
  }

  // Bamboo: stalk segments with node marks, two branches, and a few leaves
  function bamboo(ox = 0, oy = 0, s = 1) {
    const P = (x, y) => [ox + x * s, oy + y * s];
    let defs = '', out = '';
    const segs = [[250, 214], [214, 168], [168, 118], [118, 76]];
    segs.forEach(([y1, y2], i) => {
      const id = `bam-seg-${ox}-${i}`, x = 70 - i * 3;
      defs += loaded(id, P(x, y1), P(x, y2), INK.mid, INK.light);
      out += stroke(P(x, y1 - 3), P(x - 2, (y1 + y2) / 2), P(x - 3, y2 + 3), [13 * s, 11 * s, 13 * s], `url(#${id})`);
      out += stroke(P(x - 8, y2 + 1), P(x - 2, y2 - 3), P(x + 6, y2 + 1), [1.5 * s, 3.5 * s, 1.5 * s], INK.burnt);
    });
    out += stroke(P(64, 118), P(90, 96), P(118, 88), [2.5 * s, 2 * s, 0.8 * s], INK.dark);
    out += stroke(P(66, 168), P(40, 150), P(22, 146), [2.5 * s, 2 * s, 0.8 * s], INK.dark);
    const leaf = (a, b, c, wd, f) => stroke(P(...a), P(...b), P(...c), [1 * s, wd * s, 0.2 * s], f);
    out += leaf([118, 88], [140, 70], [168, 74], 11, INK.burnt);
    out += leaf([116, 90], [138, 96], [158, 114], 10, INK.dark);
    out += leaf([110, 92], [122, 110], [126, 136], 9, INK.mid);
    out += leaf([22, 146], [4, 128], [-6, 106], 10, INK.burnt);
    out += leaf([24, 148], [6, 156], [-12, 170], 9, INK.mid);
    out += leaf([68, 78], [86, 50], [104, 40], 10, INK.dark);
    out += leaf([66, 80], [52, 54], [56, 28], 9, INK.burnt);
    return { defs, out };
  }

  return { INK, stroke, loaded, bamboo };
})();
