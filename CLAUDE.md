# Teacher Book

Mr. Lewis's high school art curriculum book: Drawing & Painting, two levels.
**Top priority in the library** (order: Teacher → Coaching → Ramination and Codex, tied).
Public repo, and the site is served at https://zjaylewis94.github.io/teacher_book/ once `index.html` exists.

## Privacy rule
This repo is public. **Never add student names, grades, rosters or photos of student work** that
identify a student. Curriculum, lessons, worksheets and teacher-made examples are fine.

## Curriculum structure
From Zach's plan snapshot (Drive screenshot dated Aug 26, 2026). Semester 2 is still being written.

Every unit has three tiers, **T1 / T2 / T3**, plus a **Wild Card project**. T1 opens with an intro worksheet;
in the advanced course it's "Intro Worksheet+".

| | DP 1-2 (intro) | DP 3-4 (advanced) |
|---|---|---|
| **Semester 1** | 1 Pencil · 2 Pen & Ink · 3 Tempera · 4 Water Color | 11 Adv Pencil · 12 Adv Pen & Ink · 13 Acrylic · 14 Adv Water Color |
| **Semester 2** | 5 Colored Pencil · 6 Charcoal · 7 Pastel · 8 Scratchboard · 9 Animation · 10 Masterpiece | 15 Adv Colored Pencil · 16 Adv Charcoal · 17 Adv Pastel · 18 Lino Prints · 19 Adv Animation · 20 Masterpiece |

Examples of what's filled in so far (the text came from reading the screenshot, so some wording may be off):
Unit 1: Pencil Intro Worksheet, Value Practice, Shading with Forms, 1 Point Perspective Room.
Unit 11: Advanced Gradients, Constructing + Editing Form, Cast Shadow Studies, Surrealist Forms Landscape.
Wild cards include Tunnel Book, Food Truck, Inktober Sketchbook, Halloween Masks, Disco Ball Painting, Holiday Project (TBD).
Most Semester 2 units list only a T1 intro worksheet so far.

## Reference material (Google Drive)
`The Library/Educator/teacher_book/`
- `teacher_book.html`: the current book app (480 KB). Not in this repo yet.
- `ramhaus/UNIT 1 PENCIL/`, `ramhaus/UNIT 11 ADV PENCIL/`: worksheets, how-to images, source PSDs.
- `ramhaus/VISCOM 1.pdf`
- `MrLewis-Regular.ttf` / `.otf` and `Mr_Lewis_Font.png`: Zach's own handwriting font. It's the candidate
  for the shared library theme and cover pages.
- The plan snapshot screenshot.

PSDs and full-resolution PNGs stay in Drive. GitHub rejects files over 100 MB, so only web-size exports
the book actually displays go in this repo.

## How we work
- `index.html` is the whole book: a single self-contained HTML file, vanilla JS, no build step.
- Work on a branch and open a PR. Zach merges from his phone. Don't push to `main`.
- Before opening a PR, check the page in headless Chromium (Playwright is installed) at 390px and 1280px
  wide, with no page errors.
- If a change alters the shape of the book's saved data, bump its localStorage key version.
