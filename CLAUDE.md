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

## The app
- `index.html` is the book (uploaded as `teacher_book.html` on Sep 27, 2026). Saved data: localStorage `teacher_book_v2`
  (v1 until Sep 28; on first load a v1 book is copied forward once and v1 is left in place as a fallback).
- **A saved book keeps its own copy of the curriculum**, so editing `SEED`/`CURRICULUM` alone never reaches Zach's
  devices. To ship new seeded content: raise `SEED.contentVersion` (now 3) and add a `migrateToVn()` step that
  `migrateContent()` calls; it runs first in `hydrateState()`. Move old material to **Old Drafts** (sidebar group
  `parent:'archive'`, or the Curriculum tab's `old-drafts` course); don't delete it.
- Loading (`initState`): a fresh device starts from `SEED` with `_ts: 0` and stores nothing until the first edit. An upgraded
  book is stored **without** bumping `_ts`. Both keep a newer copy on GitHub winning when Sync compares timestamps.
- The file was forked from a life-planner app. On Sep 28, 2026 the unreachable leftovers were removed: the home tab,
  calendar, brain dump and auto-sort, fitness, cookbook, lists, tasks and projects, the retired right sidebar, and a
  second structured unit viewer. The Teacher Book has one box (`teaching`). Don't bring those back by copying code
  from the other books.
- Navigation: `openChapter()`, `openSection('notes'|'curriculum')` and `findChapter()`. Sidebar groups live in `CHAPTER_GROUPS`.
  Page tools (rename, move, delete) are the ⋮ after the page tabs; chapter tools are the ⋮ on each sidebar row.
- GitHub Sync saves `teacher_book_data.json` to the **private `subroutine-data` repo**, which is the default. Any device still set to the
  public `SUBROUTINE` repo gets switched automatically. Its settings slot is `teacher_book_gh_cfg`.
- Every book shares one address (zjaylewis94.github.io), so they share one browser storage space of about 5 MB.
  Keys must be unique per book, and big attachments in one book eat into the others' room.

## Reference material (Google Drive)
`The Library/Educator/teacher_book/`
- **`ramhaus/` is this school year's curriculum: everything Zach uses as an art teacher.**
- `ramhaus/UNIT 1 PENCIL/`, `ramhaus/UNIT 11 ADV PENCIL/`: worksheets, how-to images, source PSDs.
- `ramhaus/VISCOM 1.pdf`
- `MrLewis-Regular.ttf` / `.otf` and `Mr_Lewis_Font.png`: Zach's own handwriting font. It's the candidate
  for the shared library theme and cover pages.
- The plan snapshot screenshot.

PSDs and full-resolution PNGs stay in Drive. GitHub rejects files over 100 MB, so only web-size exports
the book actually displays go in this repo.

## How we work
- The whole book is `index.html`: a single self-contained HTML file, vanilla JS, no build step.
- Work on a branch and open a PR. Zach merges from his phone. Don't push to `main`.
- Before opening a PR, check the page in headless Chromium (Playwright is installed) at 390px and 1280px
  wide, with no page errors.
- If a change alters the shape of the book's saved data, bump its localStorage key version.
- **Synced with the UNIT GUIDES doc on Sep 28, 2026** (content version 2):
  - The **Curriculum** tab (`CURRICULUM`) holds Draw + Paint 1–4, Units 1–20. Each project has its name, description,
    points and `suggested:true` where the doc says "(suggested)". Tier 2 is 4 pts, there's one Tier 3, and wild cards show as `WILD CARD`.
  - Carried-over write-ups: U1 Value Practice, Shading with Forms and 1 Point Perspective Room (from the old Ramhaus Unit 1),
    and U5 Koons Dog (from last year). Every other project says "Not written yet".
  - Last year's Draw & Paint 2 and 4 stay at the bottom of the Curriculum tab (`archived:true`, ids `ly-…`), with their master studies.
  - Syllabus → Project Overview and Year at a Glance were rewritten from the doc. The Sub Guide and Official Syllabus now say Tier 2 = 4 pts.
  - The old medium-by-medium unit chapters and the old syllabus pages are under the **Old Drafts** sidebar group.
    The old Ramhaus Unit 1 (with its steps and rubrics) is the **Old Drafts** course at the bottom of the Curriculum tab.
  - **Open question for Zach:** the syllabus letter grades (A = 15–20) assume a 20-point unit. Doc units now total
    20–28 points (e.g. Unit 3 is 2×2 + 4×4 + 8 = 28). Don't change the scale without him.
  - When the doc changes, re-read it and regenerate `CURRICULUM` from it rather than hand-editing (the Sep 28 build
    parsed the doc tabs and wrote the block programmatically), then bump the content version.

## UNIT GUIDES Google Doc (filled Sep 28, 2026)
Google Doc **UNIT GUIDES** (Drive: `The Library/Educator/teacher_book/ramhaus/`,
id `1nRdwH9gzSa28y3aqIjDO2Qss1KrGboYcNqXNJF6yIXA`). Edit it **in place with the Google Docs connector**.
Zach chose this over a second doc; if the connector is missing, stop and ask, and don't create a copy.

**Structure: one tab per page, all top-level.** `SAMPLE ONE` (last year's Unit 5, left untouched), then
`---DRAW PAINT 1---`, Units 1–4, `---DRAW PAINT 2---`, Units 5–10, `---DRAW PAINT 3---`, Units 11–14,
`---DRAW PAINT 4---`, Units 15–20. Each DRAW PAINT tab has a title, a short semester overview, and a 5-column
at-a-glance table (Unit · Tier 1 · Tier 2 · Tier 3 · Wild Card).
Each unit tab copies the sample: TITLE heading, OVERVIEW, PROJECT LIST as a 6×2 zigzag table (merged description
cells; tier colors yellow `#FFF2CC`, blue `#C9DAF8`, red `#F4CCCC`), checkbox project names (bold 10pt, indent 18/36),
8pt descriptions (indent 36/36), then a WILD CARD list under the table. Deadlines read `DEADLINE: TBD`.
Suggestions carry a small italic "(suggested)" after the name. Zach removes the label when he keeps one.
API gotchas learned doing it: apply `namedStyleType` before run styles (it wipes them), and create checkbox bullets
*before* indenting, because Docs reads an existing indent as a deeper list level.
One correction to the snapshot: "Barton Morris" is written as **Burton Morris** (the Pop artist).

**Section mapping:** DP1 = Units 1–4 (intro, semester 1) · DP2 = Units 5–10 (intro, semester 2) ·
DP3 = Units 11–14 (advanced, semester 1) · DP4 = Units 15–20 (advanced, semester 2).
Each section starts with a project overview (every unit's T1/T2/T3/Wild Card at a glance), then one guide per unit.

**Every unit guide copies the sample's format exactly:** `UNIT n: NAME` · **OVERVIEW** (3–4 sentences, second
person, ending on what the student will be able to do) · **PROJECT LIST** table:
Tier 1 – Skill Builders (1–2 days each · 2 pts each) · Tier 2 – Practice Projects (4–6 days · **4 pts each**, raised from 3 on Sep 28) ·
Tier 3 – Major Project (1–2 weeks · 8 pts; **exactly one per unit**, and **no master studies** anywhere, Zach's rule
for this school year, set Sep 28). Each project gets a **BOLD CAPS NAME** plus a one-sentence description.
Add a Wild Card line per unit. **Deadlines: TBD** (Zach's call, for now).
Advanced units (11–20) push harder than their intro partners (the "+" worksheets); their T3 is more open-ended.
Zach's 3 N's arc (Teacher Book syllabus): T1 Narrative, T2 Novelty, T3 Nuance.

**Rule for empty slots:** fill them with suggested projects that fit the medium and level, and **label each
one "(suggested)"** so Zach can tell them from his own plan. Tiers 1 and 2 get 2–4 projects each; Tier 3 gets one.

**Zach's plan** (from his Aug 26 snapshot; Claude settled the lines the screenshot scrambled, and Zach approved):

| Unit | T1 | T2 | T3 | Wild Card |
|---|---|---|---|---|
| 1 Pencil | Pencil Intro Worksheet · Value Practice · Shading with Forms | Mad Scientist Light Logic · Extruding 101 | 1 Point Perspective Room | Tunnel Book · Food Truck |
| 11 Adv Pencil | Pencil Intro Worksheet+ · Advanced Gradients | Fruit Studies · Constructing + Editing Form · Cast Shadow Studies | Surrealist Forms Landscape | Tunnel Book · Food Truck |
| 2 Pen & Ink | Pen + Ink Intro Worksheet · Pen Shading Techniques · Line Quality + Line Weights | Contour Line Hands · Zen Doodle w/ Emphasis | Weighted Contour Line Still Life Drawing | Inktober Sketchbook · Halloween Masks |
| 12 Adv Pen & Ink | Pen + Ink Intro Worksheet+ · Pen Shading Techniques · Line Quality + Line Weights | Contour Line Forms/Objects · Ink Wash Blockout / Pen Texture | Ink Wash (Sumi-e) | Inktober Sketchbook · Halloween Masks |
| 3 Tempera | Tempera Intro Worksheet · Color Theory Worksheet | Blending Tubes (Smooth + Segmented) · Sparkmatik Blobs · Impossible Shape Painting · 2D Mecca Chameleon | Burton Morris Product Painting | Digital Painting (TBD) · Disco Ball Painting |
| 13 Acrylic | Acrylic Intro Worksheet · Color Theory / Value Scales Worksheet+ | That's a Wrap! · Sparkmatik Blobs · 3D Mecca Chameleon | Candy Box | Digital Painting (TBD) · Vector Painting |
| 4 Water Color | Water Color Worksheet | Object Study Painting | Urban Sketching Final | Holiday Project (TBD) |
| 14 Adv Water Color | Water Color Worksheet+ | Sweet Treats Painting (layered watercolor + colored pencil details) · Still Life Practice | Urban Sketching Final | Holiday Project (TBD) |
| 5 Colored Pencil | Colored Pencil Intro Worksheet | Koons Dog | Half Face Celeb (Color Edition) | — |
| 15 Adv Colored Pencil | Colored Pencil Intro Worksheet+ | Colored Pencil Candy Drawing | Full Face Celeb (Color Edition) | — |
| 6 Charcoal | Charcoal Intro Worksheet | Charcoal Water Droplet · Still Life Practice | Figure Drawing | — |
| 16 Adv Charcoal | Charcoal Intro Worksheet+ | Still Life Practice · Tim Burton Portrait | Figure Drawing | — |
| 7 Pastel / 17 Adv Pastel | Intro Worksheet / Intro Worksheet+ | — | — | — |
| 8 Scratchboard / 18 Lino Prints | Intro Worksheet / Intro Worksheet+ | — | Scratchboard Animal / Lino Block Print | — |
| 9 Animation / 19 Adv Animation | Intro Worksheet / Intro Worksheet+ | — | — | — |
| 10 Masterpiece / 20 Masterpiece | Intro Worksheet / Intro Worksheet+ | — | — | — |

"—" means empty, so fill it with suggestions. Animation (9/19) can tie into Raminations (Rammy, short animated lessons).
Tie-breaks Claude made (Zach can override): Tim Burton Portrait → U16 T2 · Sweet Treats → U14 T2 ·
Koons Dog → U5 · Candy Drawing → U15 · Burton Morris → U3 T3 · 3D Mecca Chameleon → U13 T2 ·
2D Mecca Chameleon → U3 T2 (moved from T3 to keep one T3; it mirrors the 3D chameleon, a T2 in U13).
Tier 3 picks for units the snapshot left empty (all still labeled suggested): U7 Bold Still Life · U17 Expressive Color
Composition · U9 10-Second Short · U19 Animated Short · U10 and U20 Final Masterpiece. The master-study T2s were swapped
for Composition Study (U10) and Layered Stroke Study (U17).
Useful detail lives in `index.html` under Old Drafts (search "PROJECT BANK", "3 N's ARC"): project banks from old
boards, and the old Unit 1 steps and materials.
When editing later, re-read the doc and check every unit keeps its three tiers plus wild card, exactly one Tier 3, and each suggestion stays labeled.
`SAMPLE ONE` is last year's page and still shows the old rules (MASTER STUDY [BANKSY], Tier 2 at 3 pts); leave it unless Zach asks.
