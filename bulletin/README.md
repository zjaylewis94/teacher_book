# Daily whiteboard bulletin

The "TODAY IS ____" Google Slides deck that goes on the projector each period. A scheduled Claude task refreshes
it every school morning (5:41am Pacific) from the **Bulletin Plan** Google Sheet. Both live in Zach's Drive, not here.
This folder holds only the code and the doodle backgrounds, with no student data.

## What's where
- **Deck**: the first two slides, `bul_art` (Beginners + Advanced cards) and `bul_avid` (AVID 2 agenda +
  Important Dates). Every box has a fixed object ID (see `SLIDES` in `bulletin.py`); the daily run only swaps text,
  the deadline pill colour and the background. Other slides in the deck are never touched.
- **Sheet** tabs: `Projects` (class, unit line, project, start, due, status), `Daily` (optional per-day overrides:
  WORK DAY, LECTURE, DEMO, DUE DAY, CRITIQUE, NO SCHOOL), `AVID Days` (weekly pattern), `AVID Dates`, `Days Off`.
- **Teacher Book**: when a project's due date passes and the Sheet lists nothing newer, `plan` takes the next project
  from `CURRICULUM` in `../index.html` (by the unit and tier in the unit line) and the run appends it to the Sheet as
  `Suggested`.

## Commands
```
python3 bulletin.py plan sheet.json 2026-11-05 ../index.html > content.json   # Sheet values -> one day's content
python3 bulletin.py update content.json deck.json [--ref BRANCH] > req.json   # refill the two slides
python3 bulletin.py build content.json [--ref BRANCH] > req.json              # recreate both slides from scratch
python3 bulletin.py curriculum ../index.html [unit ...]                       # Teacher Book units as JSON
```
`sheet.json` is `{"Projects": [[...rows]], "Daily": ..., "AVID Days": ..., "AVID Dates": ..., "Days Off": ...}` with
the values exactly as Sheets `get_values` returns them. `deck.json` is a `read_presentation` result.

## Gotchas (learned building it)
- Slides stores every shape at a 3,000,000 EMU base size and scales it. Never resize with
  `updatePageElementTransform` using scale 1; rebuild the slide instead (`build`).
- Slides has no shrink-to-fit. `fit()` picks a font size from each box's list using rough per-font glyph widths
  (`EM`); Permanent Marker is wide (0.75 em).
- Numbered lists use `NUMBERED_DIGIT_ALPHA_ROMAN` (`NUMBERED_DIGIT_PERIOD` is a Docs preset and fails in Slides).
- Backgrounds load from `raw.githubusercontent.com/.../{ref}/bulletin/bg/`. Slides copies the image when it's set,
  so the URL only has to work at update time.

## Backgrounds
`bg/bulletin_bg_{mon..fri}.jpg`, 1920×1080, one Crayola trio per weekday, black marker frame per the worksheet
style guide. To regenerate: `npm i roughjs@4.6.6` in `bg/`, then `node render.js` (Playwright).
