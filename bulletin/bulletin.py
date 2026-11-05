#!/usr/bin/env python3
"""Daily whiteboard bulletin: turns one day's content into Google Slides edits.

The bulletin deck ("TODAY IS ____" in Zach's Drive) has two designed slides:
  bul_art   Art: date header, a Beginners card and an Advanced card, a footer strip.
  bul_avid  AVID 2: date header, an agenda card, an Important Dates card, a footer strip.
Every box has a fixed object ID (see ELEMENTS), so a daily update only swaps text,
the pill colour and the weekday background. Nothing here holds student data.

  python3 bulletin.py build  content.json                 -> requests that create both slides (one time)
  python3 bulletin.py update content.json deck.json       -> requests that refill them (every school day)
  python3 bulletin.py curriculum index.html [unit ...]    -> Teacher Book units/projects as JSON (for clues)

deck.json is a read_presentation result (raw, or the {"content": "..."} wrapper the app saves).
Output is {"requests": [...], "writeControl": {...}} for update_presentation; warnings go to stderr.

content.json:
{
  "day": "WEDNESDAY", "date": "NOVEMBER 4, 2026", "bg": "wed",
  "classes": {
    "beg": {"unit": "UNIT 2 · PEN + INK", "project": "Weighted Contour Line Still Life Drawing",
            "due": "DUE FRIDAY 11/6", "urgent": false, "agenda": "WORK DAY: Finish your shading"},
    "adv": {...}
  },
  "art_footer": "PHONES AWAY  ★  GRAB YOUR SUPPLIES  ★  GET TO WORK",
  "avid": {"title": "TUTORIAL DAY", "items": ["Drop off TRFs", "..."],
           "dates": ["FRI 11/13 — Binder check"], "footer": "..."}
}
"""
import json
import math
import re
import sys

EMU = 914400
BG_URL = "https://raw.githubusercontent.com/zjaylewis94/teacher_book/{ref}/bulletin/bg/bulletin_bg_{day}.jpg"
BG_REF = "main"

INK = "#1B1B1B"
WHITE = "#FFFFFF"
# Crayola colours. Each one means one thing on every slide.
BEG = "#FBE870"      # Beginners tab (yellow)
ADV = "#76D7EA"      # Advanced tab (sky blue)
AVID = "#C5E17A"     # AVID tab (yellow-green)
DATES = "#F7468A"    # Important Dates tab (pink)
DUE = "#FFFFFF"      # deadline pill, normal
URGENT = "#ED0A3F"   # deadline pill, due today or tomorrow (red)
SUB = "#555555"      # unit line

F_DISPLAY = "Luckiest Guy"
F_MARKER = "Permanent Marker"
F_HAND = "Patrick Hand"

# Width of an average glyph as a fraction of the font size, per font (measured roughly; errs wide).
EM = {F_DISPLAY: 0.62, F_MARKER: 0.75, F_HAND: 0.44}
# Line height as a multiple of the font size, matching the lineSpacing each font is given below.
LH = {F_DISPLAY: 1.15, F_MARKER: 1.12, F_HAND: 1.2}


def card(prefix, x, tab_text, tab_fill):
    """Elements of one class card whose left edge is x (inches)."""
    w = 4.25
    return [
        dict(id=f"{prefix}_card", kind="ROUND_RECTANGLE", x=x, y=1.78, w=w, h=2.67, fill=WHITE, line=3),
        dict(id=f"{prefix}_tab", kind="ROUND_RECTANGLE", x=x + 0.2, y=1.6, w=3.5, h=0.44, fill=tab_fill, line=2.5,
             text=tab_text, font=F_DISPLAY, sizes=[18, 16, 14], color=INK, align="CENTER", valign="MIDDLE"),
        dict(id=f"{prefix}_unit", kind="TEXT_BOX", x=x + 0.15, y=2.05, w=w - 0.3, h=0.33,
             key="unit", font=F_HAND, sizes=[17, 15, 14], color=SUB, align="START"),
        dict(id=f"{prefix}_proj", kind="TEXT_BOX", x=x + 0.15, y=2.34, w=w - 0.3, h=0.94,
             key="project", font=F_MARKER, sizes=[26, 24, 22, 20, 18, 16], color=INK, align="START", valign="MIDDLE"),
        dict(id=f"{prefix}_due", kind="ROUND_RECTANGLE", x=x + 0.2, y=3.32, w=2.75, h=0.42, fill=DUE, line=2.5,
             key="due", font=F_DISPLAY, sizes=[18, 16, 14], color=INK, align="CENTER", valign="MIDDLE"),
        dict(id=f"{prefix}_agenda", kind="TEXT_BOX", x=x + 0.15, y=3.76, w=w - 0.3, h=0.66,
             key="agenda", font=F_HAND, sizes=[18, 17, 16, 15, 14], color=INK, align="START", bold_before=":"),
    ]


def header(prefix):
    return [
        dict(id=f"{prefix}_day", kind="TEXT_BOX", x=2.35, y=0.44, w=5.3, h=0.68, key="day_line",
             font=F_DISPLAY, sizes=[36, 34, 32, 30], color=INK, align="CENTER", valign="MIDDLE"),
        dict(id=f"{prefix}_date", kind="TEXT_BOX", x=2.35, y=1.06, w=5.3, h=0.46, key="date",
             font=F_MARKER, sizes=[22, 20, 18], color=INK, align="CENTER", valign="MIDDLE"),
    ]


def footer(prefix):
    return [dict(id=f"{prefix}_foot", kind="ROUND_RECTANGLE", x=1.45, y=4.6, w=7.1, h=0.48, fill=INK, line=0,
                 key="footer", font=F_DISPLAY, sizes=[18, 16, 15, 14], color=WHITE, align="CENTER", valign="MIDDLE")]


SLIDES = {
    "bul_art": header("art") + card("beg", 0.6, "BEGINNERS · DP 1-2", BEG)
               + card("adv", 5.15, "ADVANCED · DP 3-4", ADV) + footer("art"),
    "bul_avid": header("avid") + [
        dict(id="avid_card", kind="ROUND_RECTANGLE", x=0.6, y=1.78, w=5.55, h=2.67, fill=WHITE, line=3),
        dict(id="avid_tab", kind="ROUND_RECTANGLE", x=0.8, y=1.6, w=3.3, h=0.44, fill=AVID, line=2.5,
             text="AVID 2 · SOPHOMORES", font=F_DISPLAY, sizes=[18, 16], color=INK, align="CENTER", valign="MIDDLE"),
        dict(id="avid_title", kind="TEXT_BOX", x=0.75, y=2.08, w=5.25, h=0.46, key="avid_title",
             font=F_MARKER, sizes=[22, 20, 18], color=INK, align="START", valign="MIDDLE"),
        dict(id="avid_list", kind="TEXT_BOX", x=0.75, y=2.54, w=5.25, h=1.86, key="avid_items",
             font=F_HAND, sizes=[19, 18, 17, 16, 15, 14], color=INK, align="START", numbered=True),
        dict(id="dates_card", kind="ROUND_RECTANGLE", x=6.35, y=1.78, w=3.05, h=2.67, fill=WHITE, line=3),
        dict(id="dates_tab", kind="ROUND_RECTANGLE", x=6.5, y=1.6, w=2.75, h=0.44, fill=DATES, line=2.5,
             text="IMPORTANT DATES", font=F_DISPLAY, sizes=[18, 16], color=INK, align="CENTER", valign="MIDDLE"),
        dict(id="dates_list", kind="TEXT_BOX", x=6.45, y=2.1, w=2.85, h=2.3, key="avid_dates",
             font=F_HAND, sizes=[18, 17, 16, 15, 14], color=INK, align="START", bold_before="—"),
    ] + footer("avid"),
}
ORDER = ["bul_art", "bul_avid"]


def rgb(h):
    h = h.lstrip("#")
    return {"red": round(int(h[0:2], 16) / 255, 3), "green": round(int(h[2:4], 16) / 255, 3), "blue": round(int(h[4:6], 16) / 255, 3)}


def emu(v):
    return int(round(v * EMU))


def lines_needed(text, width_in, size, font):
    per_line = max(1, int((width_in - 0.2) * 72 / (size * EM[font])))
    n = 0
    for para in text.split("\n"):
        words, cur = para.split(), 0
        if not words:
            n += 1
            continue
        lines = 1
        for wd in words:
            add = len(wd) if cur == 0 else len(wd) + 1
            if cur + add > per_line and cur > 0:
                lines += 1
                cur = len(wd)
            else:
                cur += add
        n += lines
    return n


def fit(el, text, warn):
    """Largest size from el['sizes'] whose text fits the box."""
    h_avail = el["h"] - 0.1
    for s in el["sizes"]:
        if lines_needed(text, el["w"], s, el["font"]) * s * LH[el["font"]] / 72 <= h_avail + 0.02:
            return s
    s = el["sizes"][-1]
    warn.append(f"{el['id']}: text may overflow even at {s}pt: {text[:60]!r}")
    return s


def text_for(el, c):
    """The text an element shows for content c."""
    if "text" in el:
        return el["text"]
    k, pid = el["key"], el["id"]
    if k == "day_line":
        return f"TODAY IS {c['day'].upper()}"
    if k == "date":
        return c["date"].upper()
    if k == "footer":
        return c["avid"]["footer"] if pid.startswith("avid") else c["art_footer"]
    if k == "avid_title":
        return c["avid"]["title"].upper()
    if k == "avid_items":
        return "\n".join(c["avid"]["items"])
    if k == "avid_dates":
        return "\n".join(c["avid"].get("dates") or []) or "Nothing on the calendar yet"
    cls = c["classes"][pid.split("_")[0]]
    v = cls.get(k, "")
    if k in ("project", "due"):
        v = v.upper()
    return v


def style_requests(el, text, c, warn):
    oid = el["id"]
    out = []
    size = fit(el, text, warn)
    out.append({"insertText": {"objectId": oid, "text": text}})
    out.append({"updateTextStyle": {"objectId": oid, "textRange": {"type": "ALL"}, "style": {
        "fontFamily": el["font"], "fontSize": {"magnitude": size, "unit": "PT"}, "bold": False,
        "foregroundColor": {"opaqueColor": {"rgbColor": rgb(color_for(el, c))}}},
        "fields": "fontFamily,fontSize,bold,foregroundColor"}})
    out.append({"updateParagraphStyle": {"objectId": oid, "textRange": {"type": "ALL"},
                "style": {"alignment": el["align"], "lineSpacing": {F_DISPLAY: 95, F_MARKER: 90, F_HAND: 100}[el["font"]],
                          "spaceAbove": {"magnitude": 0, "unit": "PT"}, "spaceBelow": {"magnitude": 0, "unit": "PT"}},
                "fields": "alignment,lineSpacing,spaceAbove,spaceBelow"}})
    if el.get("bold_before"):
        pos = 0
        for line in text.split("\n"):
            if el["bold_before"] in line:
                head = line.split(el["bold_before"])[0]
                a = len(text[:pos].encode("utf-16-le")) // 2
                b = a + len(head.encode("utf-16-le")) // 2
                if b > a:
                    out.append({"updateTextStyle": {"objectId": oid, "textRange": {"type": "FIXED_RANGE",
                                "startIndex": a, "endIndex": b}, "style": {"bold": True}, "fields": "bold"}})
            pos += len(line) + 1
    if el.get("numbered"):
        out.append({"createParagraphBullets": {"objectId": oid, "textRange": {"type": "ALL"},
                                               "bulletPreset": "NUMBERED_DIGIT_ALPHA_ROMAN"}})
    return out


def color_for(el, c):
    if el["id"].endswith("_due"):
        cls = c["classes"][el["id"].split("_")[0]]
        return WHITE if cls.get("urgent") else INK
    return el["color"]


def fill_for(el, c):
    if el["id"].endswith("_due"):
        cls = c["classes"][el["id"].split("_")[0]]
        return URGENT if cls.get("urgent") else DUE
    return el.get("fill")


def shape_props(el, c):
    props, fields = {}, []
    f = fill_for(el, c)
    if f:
        props["shapeBackgroundFill"] = {"solidFill": {"color": {"rgbColor": rgb(f)}}}
        fields.append("shapeBackgroundFill.solidFill.color")
    if el["kind"] != "TEXT_BOX":
        if el.get("line"):
            props["outline"] = {"outlineFill": {"solidFill": {"color": {"rgbColor": rgb(INK)}}},
                                "weight": {"magnitude": el["line"], "unit": "PT"}, "propertyState": "RENDERED"}
            fields += ["outline.outlineFill.solidFill.color", "outline.weight", "outline.propertyState"]
        else:
            props["outline"] = {"propertyState": "NOT_RENDERED"}
            fields.append("outline.propertyState")
    if el.get("valign"):
        props["contentAlignment"] = el["valign"]
        fields.append("contentAlignment")
    if not fields:
        return []
    return [{"updateShapeProperties": {"objectId": el["id"], "shapeProperties": props, "fields": ",".join(fields)}}]


def background(slide, c, ref):
    url = BG_URL.format(ref=ref, day=c.get("bg", "mon"))
    return {"updatePageProperties": {"objectId": slide, "pageProperties": {
        "pageBackgroundFill": {"stretchedPictureFill": {"contentUrl": url}}}, "fields": "pageBackgroundFill"}}


def load_json(path):
    raw = json.load(open(path))
    if isinstance(raw, list):
        raw = raw[0]["text"]
    if isinstance(raw, dict) and isinstance(raw.get("content"), str):
        raw = json.loads(raw["content"])
    if isinstance(raw, str):
        raw = json.loads(raw)
    return raw.get("content", raw) if isinstance(raw.get("content"), dict) else raw


def cmd_build(content, ref, index=0):
    c, warn, reqs = json.load(open(content)), [], []
    for i, sid in enumerate(ORDER):
        reqs.append({"createSlide": {"objectId": sid, "insertionIndex": index + i,
                                     "slideLayoutReference": {"predefinedLayout": "BLANK"}}})
        reqs.append(background(sid, c, ref))
        for el in SLIDES[sid]:
            reqs.append({"createShape": {"objectId": el["id"], "shapeType": el["kind"], "elementProperties": {
                "pageObjectId": sid,
                "size": {"width": {"magnitude": emu(el["w"]), "unit": "EMU"}, "height": {"magnitude": emu(el["h"]), "unit": "EMU"}},
                "transform": {"scaleX": 1, "scaleY": 1, "translateX": emu(el["x"]), "translateY": emu(el["y"]), "unit": "EMU"}}}})
            reqs += shape_props(el, c)
            if "font" in el:
                reqs += style_requests(el, text_for(el, c), c, warn)
    return {"requests": reqs}, warn


def cmd_update(content, deck_path, ref):
    c, warn, reqs = json.load(open(content)), [], []
    deck = load_json(deck_path)
    have = {}
    for s in deck.get("slides", []):
        for pe in s.get("pageElements", []):
            tes = (pe.get("shape", {}).get("text") or {}).get("textElements", [])
            have[pe["objectId"]] = "".join(t.get("textRun", {}).get("content", "") for t in tes)
    slides = {s["objectId"] for s in deck.get("slides", [])}
    missing = [sid for sid in ORDER if sid not in slides] + \
              [el["id"] for sid in ORDER for el in SLIDES[sid] if el["id"] not in have]
    if missing:
        sys.exit("MISSING " + " ".join(missing) + "\nThe bulletin slides were changed by hand. Delete bul_art and "
                 "bul_avid and run 'build' again (it recreates both from content.json).")
    for sid in ORDER:
        reqs.append(background(sid, c, ref))
        for el in SLIDES[sid]:
            if "font" not in el or "text" in el:   # cards and fixed tabs never change
                continue
            if el["id"].endswith("_due"):
                reqs += shape_props(el, c)
            if have[el["id"]].strip("\n"):
                # Bullets go with the deleted text (deleteParagraphBullets on an emptied box is an error);
                # style_requests re-adds them for numbered lists.
                reqs.append({"deleteText": {"objectId": el["id"], "textRange": {"type": "ALL"}}})
            reqs += style_requests(el, text_for(el, c), c, warn)
    out = {"requests": reqs}
    if deck.get("revisionId"):
        out["writeControl"] = {"requiredRevisionId": deck["revisionId"]}
    return out, warn


def cmd_curriculum(path, units):
    src = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"\{ id:'(u\d+)',num:(\d+),title:'((?:[^'\\]|\\.)*)'.*?projects:\[(.*?)\n\s*\]\}", src, re.S):
        uid, num, title, body = m.group(1), int(m.group(2)), m.group(3).replace("\\'", "'"), m.group(4)
        if units and str(num) not in units:
            continue
        projs = [{"id": p[0], "tier": p[1], "name": p[2].replace("\\'", "'"), "pts": None if p[3] == "null" else int(p[3]),
                  "desc": p[4].replace("\\'", "'")}
                 for p in re.findall(r"\{id:'([^']+)',tier:'([^']+)',name:'((?:[^'\\]|\\.)*)',pts:(null|\d+),desc:'((?:[^'\\]|\\.)*)'", body)]
        out.append({"id": uid, "num": num, "title": title, "projects": projs})
    return out


# ---------------------------------------------------------------- plan: Sheet -> content.json

ART_CLASSES = {"beg": "Beginners", "adv": "Advanced"}   # Beginners take Units 1-10, Advanced 11-20
DEFAULT_AGENDA = {
    "WORK DAY": "Grab your supplies and keep working on your project.",
    "LECTURE": "Sketchbook out. Eyes up front for today's lesson.",
    "DEMO": "New project! Eyes up front for the demo, then get started.",
    "DUE DAY": "Finish up and turn it in before the bell.",
    "CRITIQUE": "Work out on the table. Today we give each other feedback.",
}
ART_FOOTER = "PHONES AWAY  ★  GRAB YOUR SUPPLIES  ★  GET TO WORK"
LECTURE_FOOTER = "PHONES AWAY  ★  SKETCHBOOKS OUT  ★  EYES UP FRONT"
WEEKDAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
MONTHS = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER",
          "OCTOBER", "NOVEMBER", "DECEMBER"]


def parse_date(s):
    """'Fri 11/6/2026', '11/6/2026', '2026-11-06' or '11/6' (this school year) -> date, else None."""
    import datetime as dt
    s = (s or "").strip()
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.search(r"(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?", s)
    if not m:
        return None
    mo, d, y = int(m.group(1)), int(m.group(2)), m.group(3)
    if y is None:
        y = PLAN_TODAY.year + (1 if PLAN_TODAY.month >= 7 and mo < 7 else 0)
    y = int(y)
    return dt.date(y + 2000 if y < 100 else y, mo, d)


PLAN_TODAY = None


def rows(sheet, name):
    """Data rows of one tab as dicts keyed by the header's first word (lowercased)."""
    vals = sheet.get(name) or []
    if not vals:
        return []
    keys = [re.sub(r"[^a-z]", "", (h.split() or [""])[0].lower()) for h in vals[0]]
    out = []
    for r in vals[1:]:
        if any(str(c).strip() for c in r):
            out.append({k: (str(r[i]).strip() if i < len(r) else "") for i, k in enumerate(keys)})
    return out


def md(d):
    return f"{d.month}/{d.day}"


def due_text(due, today):
    if not due:
        return "DUE DATE: TBA", False
    days = (due - today).days
    if days < 0:
        return f"WAS DUE {md(due)}", True
    if days == 0:
        return f"DUE TODAY! {md(due)}", True
    if days == 1:
        return f"DUE TOMORROW {md(due)}", True
    if days <= 6:
        return f"DUE {WEEKDAYS[due.weekday()]} {md(due)}", False
    return f"DUE {WEEKDAYS[due.weekday()][:3]} {md(due)}", False


def next_from_curriculum(curr, unit_line, current_name, cls):
    """The Teacher Book project after the current one.

    The unit line ("Unit 12 · Adv Pen + Ink · Tier 3") names the unit and tier. Within that unit the
    current project is the closest name match among projects of that tier; the next project follows it,
    and after a unit's last project comes the first project of the next unit (Beginners 1-10, Advanced 11-20).
    """
    words = lambda s: set(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())
    lo, hi = (1, 10) if cls == "beg" else (11, 20)
    m = re.search(r"unit\s*(\d+)", unit_line, re.I)
    if not m:
        return None
    num = int(m.group(1))
    t = re.search(r"tier\s*(\d)", unit_line, re.I)
    by_num = {u["num"]: u for u in curr}
    unit = by_num.get(num)
    if not unit:
        return None
    plist = [p for p in unit["projects"] if p["tier"] != "WILD CARD"]
    pool = [p for p in plist if t and p["tier"] == f"TIER {t.group(1)}"] or plist
    cur = words(current_name)
    best = max(pool, key=lambda p: len(cur & words(p["name"])) / max(1, len(cur | words(p["name"]))), default=None)
    if best is not None:
        i = plist.index(best)
        if i + 1 < len(plist):
            return unit, plist[i + 1]
    for n in range(num + 1, hi + 1):
        if n in by_num:
            nxt = [p for p in by_num[n]["projects"] if p["tier"] != "WILD CARD"]
            if nxt:
                return by_num[n], nxt[0]
    return None


def cmd_plan(sheet_path, date_str, curr_path):
    import datetime as dt
    global PLAN_TODAY
    today = dt.date.fromisoformat(date_str)
    PLAN_TODAY = today
    sheet = json.load(open(sheet_path))
    if today.weekday() >= 5:
        return {"skip": "weekend"}
    for r in rows(sheet, "Days Off"):
        a, b = parse_date(r.get("first", "")), parse_date(r.get("last", ""))
        if a and a <= today <= (b or a):
            return {"skip": r.get("name") or "day off"}
    daily = [r for r in rows(sheet, "Daily") if parse_date(r.get("date")) == today]
    if any(r.get("day", "").upper() == "NO SCHOOL" for r in daily):
        return {"skip": "NO SCHOOL row in Daily"}

    curr = cmd_curriculum(curr_path, []) if curr_path else []
    projects = rows(sheet, "Projects")
    content = {"day": WEEKDAYS[today.weekday()], "date": f"{MONTHS[today.month - 1]} {today.day}, {today.year}",
               "bg": ["mon", "tue", "wed", "thu", "fri"][today.weekday()], "classes": {}, "add_rows": [], "notes": []}
    types = []
    for key, cls in ART_CLASSES.items():
        mine = [(i, r) for i, r in enumerate(projects)
                if r.get("class", "").lower() == cls.lower() and r.get("status", "").lower() != "done"]
        started = [(parse_date(r.get("start")) or dt.date.min, i, r) for i, r in mine
                   if (parse_date(r.get("start")) or dt.date.min) <= today]
        if not started:
            content["notes"].append(f"{cls}: no project in the sheet has started yet")
            cur = {"unit": "", "project": "Project coming soon", "start": None, "due": None}
        else:
            start, _, r = max(started, key=lambda t: (t[0], t[1]))
            cur = {"unit": r.get("unit", ""), "project": r.get("project", ""),
                   "start": None if start == dt.date.min else start, "due": parse_date(r.get("due"))}
        # Past due with nothing newer: take the next Teacher Book project as a suggestion.
        if cur["due"] and cur["due"] < today and curr:
            nxt = next_from_curriculum(curr, cur["unit"], cur["project"], key)
            if nxt:
                u, p = nxt
                unit = f"Unit {u['num']} · {u['title']} · {p['tier'].title()}"
                content["add_rows"].append([cls, unit, p["name"], today.strftime("%-m/%-d/%Y"), "", "Suggested",
                                            "Added by the bulletin from the Teacher Book. Fix it or set a due date."])
                cur = {"unit": unit, "project": p["name"], "start": today, "due": None}
            else:
                content["notes"].append(f"{cls}: {cur['project']} is past due and the Teacher Book has nothing after it")
        row = next((r for r in daily if r.get("class", "").lower() in (cls.lower(), "both")), None)
        typ = (row or {}).get("day", "").upper()
        if not typ:
            typ = "DUE DAY" if cur["due"] == today else "DEMO" if cur["start"] == today else "WORK DAY"
        note = (row or {}).get("agenda", "") or DEFAULT_AGENDA.get(typ, "")
        types.append(typ)
        due, urgent = due_text(cur["due"], today)
        content["classes"][key] = {"unit": cur["unit"].upper(), "project": cur["project"], "due": due,
                                   "urgent": urgent, "agenda": f"{typ}: {note}" if note else typ}
    content["art_footer"] = LECTURE_FOOTER if all(t in ("LECTURE", "DEMO") for t in types) else ART_FOOTER

    pattern = {r.get("weekday", "").upper(): r for r in rows(sheet, "AVID Days")}
    p = pattern.get(WEEKDAYS[today.weekday()], {})
    arow = next((r for r in daily if r.get("class", "").upper() == "AVID"), None)
    title = ((arow or {}).get("day") or p.get("title") or "AVID").upper()
    steps = (arow or {}).get("agenda") or p.get("steps", "")
    dates = []
    for r in rows(sheet, "AVID Dates"):
        d = parse_date(r.get("date"))
        if d and 0 <= (d - today).days <= 21 and r.get("whats"):
            dates.append((d, f"{WEEKDAYS[d.weekday()][:3]} {md(d)} — {r['whats']}"))
    content["avid"] = {"title": title, "items": [s.strip() for s in steps.split("/") if s.strip()] or ["See the board"],
                       "dates": [t for _, t in sorted(dates)[:5]],
                       "footer": p.get("bottom", "") or "PHONES AWAY  ★  BE READY TO WORK"}
    return content


def main(argv):
    ref = BG_REF
    if "--ref" in argv:
        i = argv.index("--ref")
        ref = argv[i + 1]
        del argv[i:i + 2]
    if len(argv) < 2 or argv[0] not in ("build", "update", "curriculum", "plan"):
        sys.exit(__doc__)
    if argv[0] == "curriculum":
        print(json.dumps(cmd_curriculum(argv[1], argv[2:]), indent=1, ensure_ascii=False))
        return
    if argv[0] == "plan":
        print(json.dumps(cmd_plan(argv[1], argv[2], argv[3] if len(argv) > 3 else None), indent=1, ensure_ascii=False))
        return
    out, warn = cmd_build(argv[1], ref) if argv[0] == "build" else cmd_update(argv[1], argv[2], ref)
    print(json.dumps(out, ensure_ascii=False))
    for w in warn:
        print("WARNING: " + w, file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:])
