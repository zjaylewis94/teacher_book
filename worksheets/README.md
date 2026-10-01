# Worksheets

Printable handouts for the Ramhaus units. Each one is a letter-size HTML page that links `worksheet.css`,
so every sheet shares one look. `export.js` turns a page into a print-ready PDF.

| Worksheet | Front | Back | PDF |
|---|---|---|---|
| Tunnel Book | `img/tunnel_book_howto.webp` (Zach's hand-drawn how-to) | `tunnel_book_scene.html` (building your scene) | `pdf/tunnel_book.pdf` |
| Unit 2 Pen + Ink Intro | `u02_pen_ink_intro.html` p1: Know your tool | p2: Ink warm-ups (T1, 2 pts) | `pdf/u02_pen_ink_intro.pdf` |
| Unit 2 Pen Shading Techniques | `u02_pen_shading.html` p1: value scales (hatch, crosshatch, stipple, scribble) | p2: apply to forms (T1, 2 pts) | `pdf/u02_pen_shading.pdf` |

## The theme (build on it; don't fork it)
Taken from Zach's hand-drawn how-to sheets:
- **Black marker line art on white.** It has to survive a black-and-white copier, so use gray fills sparingly
  and never rely on color alone.
- **A thick black frame on a light gray page.**
- **All caps in Zach's handwriting** (`fonts/MrLewis-Regular.ttf`, from Drive `05 FONTS & BRANDING`). It only has
  letters and basic punctuation, so digits and symbols fall back to Architects Daughter (OFL).
- **A big title with a marker underline**, and a small `(subtitle)` in parentheses beside it.
- **Readable on a copy:** MrLewis is a thin pen, so all text gets a marker stroke (`--w-body`, `--w-bold`, `--w-head`,
  `--w-title` in `worksheet.css`). Running text is 13px minimum, and headers are thick. If a page overflows, cut words
  before you shrink the text.
- **Circled step numbers** (`.step` + `.num`) and **starburst callouts** (`.burst`).
- **Drawings in inline SVG** using the `.ln / .thin / .dark / .mid / .white / .cut` classes and the `#wobble` filter,
  so the lines look hand-drawn. Diagonal hatching (`.cut`) always means "cut this away".
- **Value shows depth:** foreground is dark (`.dark`), midground is mid gray (`.mid`), background is outline only.

## Unit intro worksheets
Every unit opens with one, modeled on Zach's Pencil Intro Worksheet (Drive: `ramhaus/UNIT 01 PENCIL/PENCIL INTRO WORKSHEET`).
- Page 1, **Know your tool**: a short intro, then numbered sections (`01 02 03`): the tools of the medium, how it behaves,
  how to handle it plus a **Golden rule**, and vocab.
- Page 2, **Warm-ups** (Tier 1 · Skill builder · 2 points): five boxes that test the tool, not technique.
- Keep them about the medium. Technique gets its own T1 worksheet (e.g. Unit 2's Pen Shading Techniques and
  Line Quality + Line Weights), so don't teach it here.
- Files are named `uNN_<medium>_intro.html`; the advanced "+" version would be `uNN_<medium>_intro_plus.html`.

## Generated pen marks
`u02_pen_shading.html` draws its examples with code: `HATCH`, `XHATCH`, `STIPPLE` and `SCRIBBLE` take a box and a
`dark(x, y)` function (0 = white, 1 = black) and return SVG marks, seeded so they come out the same every time.
`FORMS` has a cube, cylinder, sphere and cone lit from the top left. Reuse them for any ink or value sheet.

## Making a new worksheet
1. Copy `tunnel_book_scene.html`, keep the `<svg><defs>` block (hatch, wobble, panel clip), and replace the content.
2. Export it: `node export.js my_sheet.html --out pdf/my_sheet` (add `--front img/front.webp` for a two-sided sheet).
   The export fails if the content runs past the frame, or if the page throws an error.
3. Check it at 390px and 1280px wide as well.

Only teacher-made material goes here. No student names or student work (the repo is public).
