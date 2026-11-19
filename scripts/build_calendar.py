"""Render the cohort calendar as markdown and as a branded PDF.

The dates come from calendar_plan.py, so the document cannot drift from the
schedule logic. Re-run after any change to intakes, durations or capacity.

    python3 scripts/build_calendar.py

Writes business/COHORT-CALENDAR.md and build/JDHA-cohort-calendar.pdf.
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from weasyprint import HTML  # noqa: E402

from brand import (  # noqa: E402
    AUTHOR,
    AUTHOR_TITLE,
    CREAM,
    GOLD_3,
    GOLD_DEEP,
    NAVY,
    ORG,
    ROOT as BRAND_ROOT,
    TAGLINE,
    YEAR,
    logo_lockup,
    theme_for,
)
from calendar_plan import (  # noqa: E402
    FACILITATORS,
    INTAKE_MONTHS,
    LADDER_WINDOW,
    MAX_INDIVIDUAL,
    MIN_TO_RUN,
    ROLLING,
    SELF_PACED,
    YEARS,
    build_schedule,
    contact_hours,
    ladder_check,
    slot_assignments,
    year_projection,
)
from catalogue import COURSES  # noqa: E402

FONTS = BRAND_ROOT / "assets" / "brand" / "fonts"
MD = ROOT / "business" / "COHORT-CALENDAR.md"
PDF = ROOT / "build" / "JDHA-cohort-calendar.pdf"

BY_SLUG = {c["slug"]: c for c in COURSES}


def _by_intake(schedule):
    out = defaultdict(list)
    for s in schedule:
        out[s.start].append(s)
    return out


def _intakes(schedule, year):
    return {d: v for d, v in _by_intake(schedule).items() if d.year == year}


def _table(group) -> str:
    rows = [
        "| Slot | Course | Code | Weeks | Ends | Enrolment closes |",
        "|---|---|---|---|---|---|",
    ]
    for s in sorted(group, key=lambda x: (x.slot, x.course["code"])):
        rows.append(
            f"| {s.slot_label} | {s.course['title']} | {s.course['code']} "
            f"| {s.weeks} | {s.end:%-d %b} | {s.enrol_closes:%-d %b} |"
        )
    return "\n".join(rows)


def markdown(schedule) -> str:
    intakes = _by_intake(schedule)
    dates = sorted(intakes)
    p26 = year_projection(schedule, MIN_TO_RUN, YEARS[0])
    p26f = year_projection(schedule, MAX_INDIVIDUAL, YEARS[0])
    p27 = year_projection(schedule, MIN_TO_RUN, YEARS[1])

    out = [
        "# Cohort Calendar",
        "",
        f"**{ORG}** · {AUTHOR}, {AUTHOR_TITLE} · Edition {YEAR}",
        "",
        "Four intakes a year, on a fixed rhythm. This is the document that turns",
        "the catalogue into a booking pipeline: every course has a date, every",
        "date has an enrolment window, and the AI ladder is scheduled so that",
        "the discount we promise can actually be delivered.",
        "",
        "---",
        "",
        "## The rhythm",
        "",
        f"Intakes start on the first Monday of February, May, August and November.",
        f"Consecutive intakes are 52 days apart, which is what makes the "
        f"{LADDER_WINDOW}-day",
        "ladder window work: finish any tier and the next one opens within",
        "the window, every time.",
        "",
        "| Intake | Starts | Enrolment opens | Enrolment closes |",
        "|---|---|---|---|",
    ]
    for d in dates:
        g = intakes[d]
        out.append(
            f"| {d:%B %Y} | Mon {d:%-d %b} | {g[0].enrol_opens:%-d %b} "
            f"| {g[0].enrol_closes:%-d %b} |"
        )

    out += [
        "",
        "Enrolment opens six weeks out and closes one week before the first",
        "session. That closing date is not bureaucratic: it is when you decide",
        "whether the cohort runs.",
        "",
        "---",
        "",
        "## The ladder promise",
        "",
        "The business manual offers 10 percent off the next tier for anyone who",
        f"enrols within {LADDER_WINDOW} days of finishing the previous one. That promise is",
        "only worth making if the next tier is actually running, so every AI",
        "tier appears at every intake.",
        "",
        "| AI-101 ends | AI-201 starts | Gap | Inside window |",
        "|---|---|---|---|",
    ]
    for s, nxt, gap, ok in ladder_check(schedule):
        if nxt is None:
            out.append(f"| {s.end:%-d %b %Y} | next calendar year | — | beyond horizon |")
            continue
        out.append(
            f"| {s.end:%-d %b %Y} | {nxt.start:%-d %b %Y} | {gap} days "
            f"| {'yes' if ok else '**no**'} |"
        )

    out += [
        "",
        "Running the tiers one per quarter instead would break the promise for",
        "three cohorts out of four. The schedule is built around this constraint,",
        "not around convenience.",
        "",
        "Higher tiers start only when graduates exist to fill them: AI-201 from",
        "the second intake, AI-301 from the third, AI-401 from the fourth.",
        "Scheduling AI-401 in February would create a class with nobody eligible.",
        "",
        "---",
        "",
    ]

    for year in YEARS:
        out += [f"## Intakes {year}", ""]
        for d, g in sorted(_intakes(schedule, year).items()):
            out += [
                f"### {d:%B} — starts Monday {d:%-d %B}",
                "",
                _table(g),
                "",
            ]

    hrs26 = sum(contact_hours(s.course) for s in schedule if s.start.year == YEARS[0])
    n26 = len([s for s in schedule if s.start.year == YEARS[0]])
    hrs27 = sum(contact_hours(s.course) for s in schedule if s.start.year == YEARS[1])
    n27 = len([s for s in schedule if s.start.year == YEARS[1]])

    out += [
        "---",
        "",
        "## Capacity",
        "",
        "One facilitator runs one room at a time. The calendar assumes",
        f"{FACILITATORS} facilitators and four slots per intake.",
        "",
        "| Year | Cohorts | Contact hours | Hours per facilitator |",
        "|---|---|---|---|",
        f"| {YEARS[0]} | {n26} | {hrs26} | {hrs26 // FACILITATORS} |",
        f"| {YEARS[1]} | {n27} | {hrs27} | {hrs27 // FACILITATORS} |",
        "",
        "That is a real but not impossible load. If you are alone, cut the",
        "rotating courses before the ladder: the ladder is what produces the",
        "AI-201, AI-301 and AI-401 enrolments that follow.",
        "",
        "---",
        "",
        "## What the calendar is worth",
        "",
        f"Assuming every cohort fills to {MIN_TO_RUN} learners and you facilitate",
        "yourself, using the cost lines in the business manual:",
        "",
        "| Year | Cohorts | Revenue | Contribution |",
        "|---|---|---|---|",
        f"| {YEARS[0]} | {p26['running']} | {p26['revenue']:,} | {p26['contribution']:,} |",
        f"| {YEARS[1]} | {p27['running']} | {p27['revenue']:,} | {p27['contribution']:,} |",
        "",
        f"At a full room of {MAX_INDIVIDUAL}, {YEARS[0]} contributes "
        f"{p26f['contribution']:,}.",
        "",
        "**Read these as a ceiling, not a forecast.** They assume every cohort",
        "reaches break-even, which will not happen in the first year. The",
        "useful number is the gap: at break-even you cover costs and earn a",
        "modest amount; the money is in filling rooms and in corporate work.",
        "",
        "---",
        "",
        "## When a cohort under-fills",
        "",
        f"Break-even is {MIN_TO_RUN}. Decide at the enrolment closing date, not on",
        "the first day of class.",
        "",
        "1. **Merge slots.** Two thin evening cohorts in the same week can share",
        "   a room if their levels are compatible. AI-101 and AI-201 cannot merge;",
        "   AI-101 and Digital Literacy can.",
        "2. **Defer to the next intake** and hold the deposit. Say so early and",
        "   offer a free seat at a workshop as an apology.",
        "3. **Run it anyway only if it is a loss-leader with a named purpose** —",
        "   a corporate client's staff, a school, a partner's referral. Write the",
        "   purpose down before you run it.",
        "",
        "Never quietly run a cohort of four. It trains learners to expect a",
        "small room, and it makes the next intake harder to sell.",
        "",
        "---",
        "",
        "## Rolling and self-paced",
        "",
        "**Rolling — start any Monday there are six enrolled:**",
        "",
    ]
    for slug in ROLLING:
        c = BY_SLUG[slug]
        out.append(f"- {c['title']} ({c['code']}) — {c['duration']}")
    out += [
        "",
        "**Self-paced — no cohort at all:**",
        "",
    ]
    for slug in SELF_PACED:
        c = BY_SLUG[slug]
        out.append(f"- {c['title']} ({c['code']}) — {c['duration']}")
    out += [
        "",
        "---",
        "",
        "## Marketing lead times",
        "",
        "The calendar only earns money if people know about it before the",
        "enrolment window closes.",
        "",
        "| When | What |",
        "|---|---|",
        "| Eight weeks out | Announce the intake. Dates, fees, the ladder discount. |",
        "| Six weeks out | Enrolment opens. Early-bird rate available. |",
        "| Four weeks out | Corporate outreach for that quarter's dates. |",
        "| Two weeks out | Early bird closes. Reminder to the mailing list. |",
        "| One week out | Enrolment closes. Decide which cohorts run. |",
        "| Day one | Register printed, books printed, accounts created. |",
        "",
        "---",
        "",
        f"*{ORG} · {TAGLINE}*",
        "",
        f"*{AUTHOR}, {AUTHOR_TITLE}*",
        "",
    ]
    return "\n".join(out)


def _face(fam: str, fn: str, weight: str = "100 900", style: str = "normal") -> str:
    return (
        "@font-face{font-family:'%s';src:url('file://%s') format('truetype');"
        "font-weight:%s;font-style:%s;font-display:block;}"
        % (fam, (FONTS / fn).as_posix(), weight, style)
    )


def pdf_css() -> str:
    return f"""
{_face('Jakarta','PlusJakartaSans.ttf')}
{_face('Bricolage','BricolageGrotesque.ttf')}
{_face('Code','JetBrainsMono-Regular.ttf','400')}
{_face('Code','JetBrainsMono-Bold.ttf','700')}
{_face('Serif','SourceSerif4.ttf')}
{_face('Serif','SourceSerif4-Italic.ttf','100 900','italic')}

@page {{
  size: A4; margin: 16mm 14mm 20mm 14mm;
  @bottom-center {{
    content: counter(page) " / " counter(pages);
    font-family: 'Code'; font-size: 6.4pt; color: #8b93a4;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; font-family: 'Serif'; font-size: 9.2pt;
  line-height: 1.4; color: {NAVY};
  padding-bottom: 8mm;  /* keeps the last table row clear of the fixed footer */
}}
.head {{
  display: flex; align-items: flex-end; justify-content: space-between;
  border-bottom: 2.5pt solid {NAVY}; padding-bottom: 4.5mm; margin-bottom: 5mm;
}}
.eyebrow {{
  font-family: 'Code'; font-size: 6.4pt; letter-spacing: .24em;
  text-transform: uppercase; color: {GOLD_3};
}}
h1 {{
  font-family: 'Bricolage'; font-weight: 800; font-size: 20pt;
  letter-spacing: -.025em; margin: 1.4mm 0 0; line-height: 1.05;
}}
.lede {{
  font-style: italic; font-size: 9.6pt; color: #3a4256;
  margin: 0 0 5mm; max-width: 152mm;
}}
h2 {{
  font-family: 'Bricolage'; font-weight: 700; font-size: 11.5pt;
  margin: 5mm 0 2mm; padding-bottom: 1.1mm;
  border-bottom: .6pt solid #d5d9e2;
}}
h2 .n {{
  font-family: 'Code'; font-size: 6.8pt; color: {GOLD_DEEP};
  letter-spacing: .18em; margin-right: 2.4mm;
}}
h3 {{
  font-family: 'Bricolage'; font-weight: 700; font-size: 9.6pt;
  margin: 4mm 0 1.6mm; color: {NAVY};
}}
h3 .sub {{
  font-family: 'Code'; font-size: 6.4pt; letter-spacing: .12em;
  color: {GOLD_3}; text-transform: uppercase; font-weight: 400;
}}
table {{ width: 100%; border-collapse: collapse; margin-bottom: 1.5mm; }}
th {{
  font-family: 'Code'; font-size: 6pt; letter-spacing: .11em;
  text-transform: uppercase; color: {GOLD_3}; text-align: left;
  padding: 1.3mm 1.5mm; border-bottom: .8pt solid {NAVY};
}}
td {{
  padding: 1.15mm 1.5mm; border-bottom: .4pt solid #e3e6ec;
  vertical-align: top; font-size: 8.4pt;
}}
td.code {{ font-family: 'Code'; font-size: 7.6pt; }}
tr.ai td {{ background: {CREAM}; }}
.note {{
  background: {CREAM}; border-left: 2.5pt solid {GOLD_DEEP};
  padding: 2.2mm 2.8mm; font-size: 8.2pt; margin: 2.5mm 0;
}}
.foot {{
  position: fixed; bottom: 0; left: 0; right: 0;
  font-family: 'Code'; font-size: 5.8pt; letter-spacing: .13em;
  color: #8b93a4; border-top: .4pt solid #e3e6ec; padding-top: 1.6mm;
  display: flex; justify-content: space-between;
}}
"""


def pdf_html(schedule) -> str:
    intakes = _by_intake(schedule)
    p26 = year_projection(schedule, MIN_TO_RUN, YEARS[0])
    p27 = year_projection(schedule, MIN_TO_RUN, YEARS[1])

    blocks = []
    for year in YEARS:
        rows = []
        for d, g in sorted(_intakes(schedule, year).items()):
            rows.append(
                f'<h3>{d:%B} <span class="sub">starts Mon {d:%-d %b}</span></h3>'
                '<table><tr><th>Slot</th><th>Course</th><th>Code</th>'
                '<th>Weeks</th><th>Ends</th><th>Closes</th></tr>'
            )
            for s in sorted(g, key=lambda x: (x.slot, x.course["code"])):
                cls = ' class="ai"' if s.track == "ai-ladder" else ""
                rows.append(
                    f"<tr{cls}><td>{s.slot_label}</td><td>{s.course['title']}</td>"
                    f'<td class="code">{s.course["code"]}</td><td>{s.weeks}</td>'
                    f"<td>{s.end:%-d %b}</td><td>{s.enrol_closes:%-d %b}</td></tr>"
                )
            rows.append("</table>")
        blocks.append(f"<h2><span class=\"n\">0{year - 2024}</span>{year}</h2>" + "".join(rows))

    ladder_rows = []
    for s, nxt, gap, ok in ladder_check(schedule):
        if nxt is None:
            continue
        ladder_rows.append(
            f"<tr><td>{s.end:%-d %b %Y}</td><td>{nxt.start:%-d %b %Y}</td>"
            f"<td>{gap} days</td><td>{'yes' if ok else 'NO'}</td></tr>"
        )

    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{pdf_css()}</style></head><body>

<div class="head">
  <div>
    <div class="eyebrow">Intakes &amp; Dates · {YEARS[0]}–{YEARS[1]}</div>
    <h1>Cohort Calendar</h1>
  </div>
  <div>{logo_lockup(44, dark=False, show_rule=False)}</div>
</div>

<p class="lede">Four intakes a year on a fixed rhythm. Every course has a date,
every date has an enrolment window, and the AI ladder is scheduled so the
discount we promise can actually be delivered.</p>

<h2><span class="n">01</span>The rhythm</h2>
<p>Intakes start on the first Monday of February, May, August and November.
Consecutive intakes are 52 days apart — that is what makes the
{LADDER_WINDOW}-day ladder window work, every time.</p>
<div class="note"><b>Enrolment opens six weeks out, closes one week before the
first session.</b> The closing date is when you decide whether the cohort runs,
not when you start chasing people.</div>

<h2><span class="n">02</span>The ladder promise</h2>
<table><tr><th>AI-101 ends</th><th>AI-201 starts</th><th>Gap</th><th>Inside window</th></tr>
{''.join(ladder_rows)}
</table>
<p>Every AI tier appears at every intake. Running them one per quarter instead
would break the promise for three cohorts out of four. Higher tiers start only
once graduates exist: AI-201 from the second intake, AI-301 from the third,
AI-401 from the fourth.</p>

{''.join(blocks)}

<h2><span class="n">03</span>What it is worth</h2>
<p>Assuming every cohort fills to {MIN_TO_RUN} and you facilitate yourself:</p>
<table><tr><th>Year</th><th>Cohorts</th><th>Revenue (UGX)</th><th>Contribution (UGX)</th></tr>
<tr><td>{YEARS[0]}</td><td>{p26['running']}</td><td>{p26['revenue']:,}</td><td>{p26['contribution']:,}</td></tr>
<tr><td>{YEARS[1]}</td><td>{p27['running']}</td><td>{p27['revenue']:,}</td><td>{p27['contribution']:,}</td></tr>
</table>
<div class="note"><b>A ceiling, not a forecast.</b> These assume every cohort
reaches break-even, which will not happen in year one. The money is in filling
rooms and in corporate work, not in the number of dates.</div>

<h2><span class="n">04</span>When a cohort under-fills</h2>
<p><b>Decide at the closing date, not on day one.</b> Merge slots where levels
are compatible, or defer to the next intake and hold the deposit. Run an
under-sized cohort only when it is a loss-leader with a named purpose, written
down before you start. Never quietly run a cohort of four.</p>

<div class="foot">
  <span>{ORG} &nbsp;·&nbsp; {TAGLINE}</span>
  <span>{AUTHOR} &nbsp;·&nbsp; {AUTHOR_TITLE}</span>
</div>
</body></html>"""


def main() -> None:
    schedule, deferred = build_schedule()
    placed, unplaced = slot_assignments(schedule)
    if deferred or unplaced:
        print(f"warning: {len(deferred)} deferred, {len(unplaced)} unplaced")

    MD.write_text(markdown(placed), encoding="utf-8")
    print(f"wrote {MD.relative_to(ROOT)}")

    PDF.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=pdf_html(placed)).write_pdf(PDF)
    print(f"wrote {PDF.relative_to(ROOT)} ({PDF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
