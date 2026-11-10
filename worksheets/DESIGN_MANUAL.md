# Mr. Lewis Worksheet Design Manual

The rules for every worksheet, practice sheet, project handout and classroom resource made for Mr. Lewis.
Written from Zach's spec of Nov 10, 2026. It replaces the Oct 14 style guide. Where the two disagree, this wins.

Read this before building or restyling a sheet. `README.md` in this folder covers the code (theme file, export script, helpers).

---

## 1. Core visual philosophy

**A skilled art teacher designed and drew this by hand.** Every sheet should feel hand-drawn, organized, functional,
slightly imperfect and memorable. It must never look like a glossy, generic AI infographic.

Three ideas decide every choice:

1. **The page teaches.** Layout, drawing and color exist to make a skill easier to learn. Anything that doesn't teach comes off.
2. **Design around the information.** The content decides the layout. Never pour content into a fixed template.
3. **One collection, many layouts.** Type, line, color and tone stay the same on every sheet, so they read as one set.
   The arrangement changes with the lesson.

**Influences:** Jay Conley, Proko, JeyRam, The Etherington Brothers, Jadokar, Skilltopus. Take what they do well:
visual teaching, anatomical accuracy, appealing linework, clear demonstrations, graphic storytelling.
Never copy an individual artist's work.

---

## 2. Mandatory rules

### Page
- US Letter, portrait, unless the content needs otherwise.
- 0.25 in outer margin.
- A bold rounded outer border, about 10 pt, when it suits the sheet.
- Rounded corners on any border that is needed.

### Structure
- Strong visual hierarchy: title, then numbered sections, then body.
- Numbered sections with clear instructional headings.
- Unit, Tier and Points appear when Zach supplies them. Never invent them.
- Section headings may sit in a container or on a colored background.
- **Body paragraphs are not boxed.**
- Generous white space wherever students draw, write or practice.
- No excess panels, no containers inside containers, no decoration for its own sake.

### Never
- Rammy on a worksheet, packet or handout (see Mascot).
- Speed lines, radiating strokes, starbursts, attention bursts or other "excitement" marks.
- Decorative expression marks, clip art, random visual filler.
- Shrinking text or work areas to make content fit. Redesign or add a page.
- Invented grading criteria, point values, materials or extra assignments.

### Mascot
Rammy is reserved for classroom posters, animated shorts and special character-based content.
He does not appear on ordinary worksheets, lesson packets or instructional handouts.

---

## 3. Typography

| Role | Font | Size |
|---|---|---|
| Title, outlined display lettering | KC PaintedHand | 24 pt or larger |
| Section headings | KC PaintedHand or Papernotes Bold | about 16 pt |
| Body text, readable lowercase | Papernotes | about 12 pt, adjusted for legibility |
| Thin accents only (small header line, labels) | KC Beebosloth | as needed |

- KC Beebosloth has letters, digits and periods only. Keep unsupported punctuation out of it.
- **Readability beats the font.** If a decorative face hurts legibility at print size, switch to Papernotes.
- Line weights: three levels, about **10 / 8 / 5 pt**, used where they help (outer border, main shapes, detail).

### Font licensing
The KC fonts and Papernotes are licensed desktop fonts with limited seats.
- Never distribute the font files.
- Never put them in a public repository. They live in `fonts/licensed/`, which git ignores.
- Never embed them against the license. Every PDF from this folder is rebuilt from page images, and `pdffonts` must list none.
- When they can't be used legitimately, use a properly licensed alternative and say so.

---

## 4. Color

**Color communicates. It does not decorate.**

- Black and white is the foundation.
- Crayola-inspired palette only.
- Use color for emphasis, annotations, comparisons, corrections and instructional examples.
- Color may lead when the lesson is about color.
- A repeated color keeps the same value and the same job across the sheet and across the set.
- Solid, clean fills. No blotchy artifacts.
- Every sheet must still make sense in grayscale. Check the black-and-white print before delivery.
- If color doesn't improve learning or hierarchy, leave it out.

---

## 5. Illustration

**Illustrations must teach accurately.**

Use:
- Confident, hand-drawn contours.
- Correct perspective and proportion.
- A clear line-weight hierarchy.
- Accurate overlaps, shadows and construction.
- Simple but convincing demonstrations.
- Carefully chosen reference photographs when a real object or material has to be identified.

Avoid:
- Generic clip art.
- Unnecessary gradients or textures.
- Misleading diagrams and distorted objects.
- Decorative expression marks, speed lines, radiating strokes, bursts.
- Any element that teaches nothing.

**Photographs:** when Zach asks for real photos, use genuinely photographed references with suitable usage rights.
Never pass off a generated photorealistic image as a photo. If one is used, label it as generated.

**Known limit:** drawings made in code are clean line art, not real pen draftsmanship. When a sheet needs a
hand-drawn illustration, the better route is Zach's own drawing (or other supplied art) placed into the layout.
Say so rather than faking it.

---

## 6. Instructional design

Every worksheet answers five questions for the student:

1. What am I learning?
2. Why does it matter?
3. What does successful work look like?
4. What steps do I follow?
5. What do I have to complete myself?

- Prefer a visual demonstration to a long explanation.
- Use comparisons, sequences, enlarged details, annotations and before/after examples when they make the idea clearer.
- Match the amount of content to the complexity of the assignment.
- Practice sheets put usable workspace first.

### Layout templates
Starting points, not molds. Adapt each to the subject.

**A. Unit intro ("Know your tool")**: 2 pages.
- Page 1: title, short intro, numbered sections: the tools, how the medium behaves, handling it plus one Golden rule, vocabulary.
- Page 2: warm-ups. About five tasks that test the tool, each with a short instruction and a large empty box.
- Example: `u03_tempera_intro.html`.

**B. Technique or skill sheet**: 1 to 3 pages.
- A demonstration strip showing the skill done right (and wrong, when the contrast teaches).
- Guided practice, then independent practice. Workspace grows as guidance shrinks.

**C. Project instruction page**: 1 page.
- What it looks like, the rules, the steps in order, and how it's graded if Zach supplied a rubric.
- Example: `u12_sumi_e.html`.

**D. Planning / prelim sheet**: 1 to 2 pages.
- Drills first, then planning boxes: subject, thumbnails, order of work, a log.
- Example: `u12_sumi_e_prelim.html`.

**E. Workshop or reference handout**: 1 to 2 pages.
- One central demonstration with short notes around it, then a step-by-step build.
- A border is optional here.

### Benchmark: the Sumi-e sheets
Zach approved `u12_sumi_e.html` and `u12_sumi_e_prelim.html` as the reference for this system. Keep what works in them:
- Strong title hierarchy.
- Numbered instructional sections.
- Selective color accents.
- Accurate brushstroke demonstrations.
- Clear separation between instructions and practice.
- Generous student workspace.
- Coordinated styling across pages.
- Minimal decoration.

Don't copy their layout mechanically. Adapt the system to the subject.

---

## 7. Content preservation

**A style revision and a content revision are two different jobs.** Never mix them without being asked.

When restyling an existing worksheet:
- Keep every instruction and requirement unless Zach authorizes a change.
- Keep the educational purpose.
- Keep the numbering and sequence unless he asks for restructuring.
- Don't invent grading criteria, point values, materials or extra assignments.
- Don't silently drop an activity to make the layout fit.
- Don't reword terminology without naming the proposed change.
- Improve clarity and presentation without changing the lesson.

If a content change would help, list it separately as a proposal and leave the content as it was.

---

## 8. Production and print quality

- Proofread every heading and instruction.
- Check alignment, spacing and margins.
- Check for overlapping shapes, bad fills and clipping.
- Confirm every diagram shows the skill correctly.
- Check text is readable at actual print size.
- Confirm student work areas are large enough to use.
- Confirm the color version works in black and white.
- Output high-resolution, print-ready files.
- Prefer editable, vector text and graphics where the font license allows. Here it doesn't allow embedded KC or
  Papernotes text, so PDFs are built from high-resolution page images (192 dpi or better).
- **Look at a rendered preview before delivering.** Never ship a page unseen.
- If it can't reasonably fit, redesign the layout or add a page.

---

## 9. Final checklist

Run this on every sheet before it goes to Zach.

**Identity**
- [ ] Looks hand-made and organized, not like a generic infographic.
- [ ] Belongs with the rest of the set: same fonts, line weights, palette and tone.
- [ ] No Rammy.
- [ ] No bursts, speed lines, expression marks, clip art or filler.

**Layout**
- [ ] US Letter portrait, 0.25 in margin.
- [ ] Clear hierarchy: title, numbered sections, body.
- [ ] Unit, Tier and Points shown only as supplied.
- [ ] Body paragraphs not boxed. No containers inside containers.
- [ ] Work areas are generous.

**Type and color**
- [ ] KC PaintedHand titles, Papernotes text, KC Beebosloth accents only.
- [ ] Body about 12 pt and readable at print size.
- [ ] Color carries meaning and is consistent.
- [ ] Reads correctly in grayscale.

**Teaching**
- [ ] A student can tell what, why, what good looks like, the steps and what to complete.
- [ ] Every diagram is accurate.
- [ ] Demonstrations do the explaining wherever they can.

**Content**
- [ ] Nothing removed, added or reworded without Zach's say-so.
- [ ] Any proposed content change is listed separately.

**Production**
- [ ] Proofread.
- [ ] No overlaps, clipping or stray fills.
- [ ] Rendered preview inspected, in color and in black and white.
- [ ] PDF is print-ready and embeds no licensed font.
- [ ] No licensed font files, student names or student work in the repo.
