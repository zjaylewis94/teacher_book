# Worksheets

Printable handouts for the Ramhaus units. Each one is a letter-size HTML page that links `worksheet.css`,
so every sheet shares one look. `export.js` turns a page into a print-ready PDF.

| Worksheet | Front | Back | PDF |
|---|---|---|---|
| Tunnel Book | `img/tunnel_book_howto.webp` (Zach's hand-drawn how-to) | `tunnel_book_scene.html` (building your scene) | `pdf/tunnel_book.pdf` |
| Unit 2 Pen + Ink Intro | `u02_pen_ink_intro.html` p1: Know your tool | p2: Ink warm-ups (T1, 2 pts) | `pdf/u02_pen_ink_intro.pdf` |
| Unit 2 Pen Shading Techniques | `u02_pen_shading.html` front: contour lines first + hatching | back: crosshatching, stippling, scumbling (T1, 2 pts) | `pdf/u02_pen_shading.pdf` |
| Unit 2 Line Quality + Line Weights | `u02_line_quality.html` p1: line qualities, flat vs weighted, when to go thick | p2: line practice; p3: six weight challenges (T1, 2 pts) | `pdf/u02_line_quality.pdf` |
| Life & Death (sub-week wild card, 4 pts) | `life_and_death.html` front: instruction page (two examples, rules, 4 steps, rubric) | back: work page (list 5, final truck). Sub plan: `life_and_death_sub_note.html` | `pdf/life_and_death.pdf`, color: `pdf/life_and_death_color.pdf`, `pdf/life_and_death_sub_note.pdf` |
| Unit 12 Sumi-e (Tier 3, 8 pts): instructions | `u12_sumi_e.html`: what it looks like, rules (brush only, 25 strokes max, 1/3 empty, red seal), 5 steps, 4×2 rubric | (one page) | `pdf/u12_sumi_e.pdf`, color: `pdf/u12_sumi_e_color.pdf` |
| Unit 12 Sumi-e prelim | `u12_sumi_e_prelim.html` p1: load the brush, ink tones, 6 stroke drills | p2: Plan it (subject, 3 thumbnails, stroke order, rehearsal log) | `pdf/u12_sumi_e_prelim.pdf`, color: `pdf/u12_sumi_e_prelim_color.pdf` |
| Urban Sketching handout (Unit 4 + 14 and the Insight workshop; not graded) | `u04_urban_sketching.html` p1: Da Rules (Zach's 12 rules around one sketch of a historic house with orange trees; numbers in the sketch show each rule) | p2: Center Out (story moment hunt, 4-step build that doubles as the demo, watercolor in 3 moves, time plan). `?insight` swaps the header; `?bw` drops the watercolor for the copier | `pdf/u04_urban_sketching.pdf`, `pdf/insight_urban_sketching.pdf`, B&W: `pdf/insight_urban_sketching_bw.pdf` |

## The theme (build on it; don't fork it)
This is the **print** look: black and white for the copier. Color versions for Google Classroom and screens
follow the digital rules in the Worksheet style guide in `../CLAUDE.md` (Zach's call, Oct 15, 2026).
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

## Instruction-sheet look (no frame)
Zach's reference for how-to pages is Jay Conley's hand-drawn instruction sheets (Nov 10, 2026: "more like this style").
`u04_urban_sketching.html` is the first sheet built that way; copy it for the next how-to page:
- **No frame and no boxes.** White page, big pictures, notes placed around the art.
- **Type is the digital set, in print too.** Zach dropped the MrLewis handwriting font on Nov 10 ("I actually hate it"):
  KC PaintedHand for titles and headings, Papernotes for text, KC Beebosloth for the small header line.
  The older sheets still use MrLewis until he asks for them to be converted.
- **Title** (`title()`): KC PaintedHand, outlined, with a drop shadow and a watercolor wash inside the letters.
- **Watercolor** (`#wcf` for washes, `#wcs` for small dabs; class `wc`): three Crayola colors at most, loose and a little
  outside the lines, with paper left white. It goes on the finished sketch only, so the steps before it stay ink.
- **Pen textures, not gray fills:** hatching `#hd`, vertical lines `#hv`, crosshatch `#hx`, stipple `#stip`.
- **Ribbon banners and a scroll** (`ribbon()`, `scroll()`) for subtitles and word lists; **fat hatched arrows**
  (`blockArrow()`) between steps.
- The scene is drawn in layers (`L[0]`…`L[3]`, then `WASH`) in the order a student draws it, so the step panels reuse it.
- The page is one 816 × 1056 SVG layer plus absolutely placed text blocks, so `export.js` can't detect overflow here.
  Look at the PNG.
- Every version uses the licensed fonts, so **rebuild each PDF from its PNGs** (the `convert` line under Color versions)
  and check `pdffonts` shows none. `?bw` hides the watercolor for the black-and-white copier.

## Unit intro worksheets
Every unit opens with one, modeled on Zach's Pencil Intro Worksheet (Drive: `ramhaus/UNIT 01 PENCIL/PENCIL INTRO WORKSHEET`).
- Page 1, **Know your tool**: a short intro, then numbered sections (`01 02 03`): the tools of the medium, how it behaves,
  how to handle it plus a **Golden rule**, and vocab.
- Page 2, **Warm-ups** (Tier 1 · Skill builder · 2 points): five boxes that test the tool, not technique.
- Keep them about the medium. Technique gets its own T1 worksheet (e.g. Unit 2's Pen Shading Techniques and
  Line Quality + Line Weights), so don't teach it here.
- Files are named `uNN_<medium>_intro.html`; the advanced "+" version would be `uNN_<medium>_intro_plus.html`.

## Color versions (Google Classroom)
A sheet gets its color copy from the same file: open it with `?color` and it switches to the digital style
(KC PaintedHand titles, outlined KC PaintedHand headings, Papernotes text, KC Beebosloth labels, Crayola colors).
`life_and_death.html` is the first one; copy its `.digital` block for the next.
- The KC and Papernotes fonts are **licensed desktop fonts (2 users)**, so they never go in this public repo.
  Download them from Drive `05 FONTS & BRANDING/` into `worksheets/fonts/licensed/` (ignored by git) before exporting.
- KC Beebosloth only has letters, digits and periods; its other punctuation is a placeholder, so the page falls back
  to Papernotes for those characters.
- Export: `node export.js 'my_sheet.html?color' --out pdf/my_sheet_color`, then rebuild the PDF from the PNGs so no
  font files are embedded in it (see the Life & Death commit for the one-liner).

## Generated pen marks
Code that draws real hatching, crosshatching, stippling and scribbling (`HATCH`, `XHATCH`, `STIPPLE`, `SCRIBBLE`, plus
lit cube/cylinder/sphere/cone `FORMS`) lives in git history: `git show 6992a8f:worksheets/u02_pen_shading.html`.
That draft was replaced by Zach's contour-lines version, but the mark code is reusable for any ink or value sheet.

## Brush strokes (ink painting)
`sumi_brush.js` draws pressed-and-lifted brush strokes (a curve with a start, middle and end width), loaded-brush
gradients and a 17-stroke bamboo. The Unit 12 Sumi-e sheets use it; reuse it for any ink-wash or brush sheet.

## Making a new worksheet
1. Copy `tunnel_book_scene.html`, keep the `<svg><defs>` block (hatch, wobble, panel clip), and replace the content.
2. Export it: `node export.js my_sheet.html --out pdf/my_sheet` (add `--front img/front.webp` for a two-sided sheet).
   The export fails if the content runs past the frame, or if the page throws an error.
3. Check it at 390px and 1280px wide as well.

Only teacher-made material goes here. No student names or student work (the repo is public).
