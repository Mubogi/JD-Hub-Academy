"""Build the printable rate card and the corporate proposal sheet as PDFs.

Both documents share the book typography so a rate card handed to a client
looks like it came from the same organisation as the course books.

Run:  python3 scripts/build_rate_card.py
Out:  build/JDHA-rate-card.pdf
      build/JDHA-corporate-proposal-sheet.pdf
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from weasyprint import HTML  # noqa: E402

from brand import (  # noqa: E402
    AUTHOR,
    AUTHOR_TITLE,
    CREAM,
    GOLD,
    GOLD_3,
    GOLD_DEEP,
    NAVY,
    ORG,
    ROOT as BRAND_ROOT,
    TAGLINE,
    YEAR,
    logo_lockup,
)

FONTS = BRAND_ROOT / "assets" / "brand" / "fonts"
OUT = ROOT / "build"


def _face(fam: str, fn: str, weight: str = "100 900", style: str = "normal") -> str:
    return (
        "@font-face{font-family:'%s';src:url('file://%s') format('truetype');"
        "font-weight:%s;font-style:%s;font-display:block;}"
        % (fam, (FONTS / fn).as_posix(), weight, style)
    )


def base_css() -> str:
    return f"""
{_face('Jakarta','PlusJakartaSans.ttf')}
{_face('Bricolage','BricolageGrotesque.ttf')}
{_face('Code','JetBrainsMono-Regular.ttf','400')}
{_face('Code','JetBrainsMono-Bold.ttf','700')}
{_face('Serif','SourceSerif4.ttf')}
{_face('Serif','SourceSerif4-Italic.ttf','100 900','italic')}

@page {{
  size: A4;
  margin: 16mm 15mm 14mm 15mm;
}}

* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: #ffffff; color: {NAVY};
  font-family: 'Serif'; font-size: 9.4pt; line-height: 1.42;
}}

.head {{
  display: flex; align-items: flex-end; justify-content: space-between;
  border-bottom: 2.5pt solid {NAVY}; padding-bottom: 5mm; margin-bottom: 6mm;
}}
.eyebrow {{
  font-family: 'Code'; font-size: 6.6pt; letter-spacing: .26em;
  text-transform: uppercase; color: {GOLD_3};
}}
h1 {{
  font-family: 'Bricolage'; font-weight: 800; font-size: 21pt;
  letter-spacing: -.025em; margin: 1.5mm 0 0; line-height: 1.05;
}}
.lede {{
  font-family: 'Serif'; font-style: italic; font-size: 10pt;
  color: #3a4256; margin: 0 0 6mm; max-width: 150mm;
}}

h2 {{
  font-family: 'Bricolage'; font-weight: 700; font-size: 11pt;
  letter-spacing: -.01em; margin: 6mm 0 2.5mm;
  padding-bottom: 1.2mm; border-bottom: .6pt solid #d5d9e2;
}}
h2 .n {{
  font-family: 'Code'; font-size: 7pt; color: {GOLD_DEEP};
  letter-spacing: .18em; margin-right: 2.5mm;
}}

table {{ width: 100%; border-collapse: collapse; margin-bottom: 1mm; }}
th {{
  font-family: 'Code'; font-size: 6.4pt; letter-spacing: .13em;
  text-transform: uppercase; color: {GOLD_3}; text-align: left;
  padding: 1.6mm 1.8mm; border-bottom: .8pt solid {NAVY};
}}
td {{
  padding: 1.5mm 1.8mm; border-bottom: .4pt solid #e3e6ec;
  vertical-align: top;
}}
td.num {{ font-family: 'Code'; font-size: 8.4pt; text-align: right; white-space: nowrap; }}
td.name {{ font-weight: 600; }}
tr.hi td {{ background: {CREAM}; }}
.small {{ font-size: 7.6pt; color: #5a6275; }}
.note {{
  background: {CREAM}; border-left: 2.5pt solid {GOLD_DEEP};
  padding: 2.5mm 3mm; font-size: 8.2pt; margin: 3mm 0;
}}
.foot {{
  position: fixed; bottom: 0; left: 0; right: 0;
  font-family: 'Code'; font-size: 6pt; letter-spacing: .14em;
  color: #8b93a4; border-top: .4pt solid #e3e6ec; padding-top: 1.8mm;
  display: flex; justify-content: space-between;
}}
.cols {{ display: flex; gap: 5mm; }}
.col {{ flex: 1; }}
"""


AI = [
    ("AI-101", "AI in Everyday Life & Business", "6 weeks", 350_000, 300_000),
    ("AI-201", "AI Practitioner", "8 weeks", 550_000, 480_000),
    ("AI-301", "AI Builder", "8 weeks", 750_000, 650_000),
    ("AI-401", "AI Specialist & Advisor", "6 weeks", 950_000, 850_000),
]

BUSINESS = [
    ("MK-220", "Digital Marketing", "8 weeks", 450_000, 390_000),
    ("BZ-230", "Business Growth & Sales Systems", "8 weeks", 450_000, 390_000),
    ("DS-210", "Content Creation & Storytelling", "6 weeks", 350_000, 300_000),
    ("DS-140", "Graphic Design", "6 weeks", 350_000, 300_000),
    ("FN-150", "Financial & SACCO Management", "6 weeks", 400_000, 350_000),
]

OFFICE = [
    ("MS-160", "Microsoft Word", "2 weeks", 150_000, 130_000),
    ("MS-170", "Microsoft Excel", "2 weeks", 150_000, 130_000),
    ("MS-180", "Microsoft PowerPoint", "2 weeks", 150_000, 130_000),
    ("MS-190", "Microsoft Access", "2 weeks", 180_000, 160_000),
    ("MS-195", "Word + Excel Combo", "2 weeks", 250_000, 220_000),
    ("MS-200", "Microsoft Office Suite", "4 weeks", 450_000, 390_000),
    ("SW-120", "Basic Digital Literacy", "4 weeks", 200_000, 170_000),
]

YOUTH = [
    ("SW-110", "Scratch Coding (per child)", "8 weeks", 200_000, 170_000),
    ("ST-130", "Practical STEM (per child)", "10 weeks", 250_000, 220_000),
]

CORPORATE = [
    ("Awareness session", "90 minutes, up to 30 staff, on site", 1_200_000),
    ("Department training", "2 days, up to 15 staff, on site", 4_500_000),
    ("Full programme", "5 days, up to 15 staff, plus a workflow build", 9_500_000),
    ("AI policy workshop", "1 day, produces a signed policy", 2_500_000),
    ("Advisory retainer", "Monthly review, updates, on-call", 1_500_000),
]

DIGITAL = [
    ("Single course book (PDF)", 60_000),
    ("AI ladder bundle — 4 books", 180_000),
    ("Office bundle — 6 books", 200_000),
    ("Business bundle — 3 books", 130_000),
    ("Full library — 19 books", 450_000),
    ("Facilitator licence, per course, per year", 1_500_000),
]


def _money(n: int) -> str:
    return f"{n:,}"


def _rows(items, cols: str) -> str:
    out = []
    for code, name, dur, std, early in items:
        out.append(
            f'<tr><td class="small">{code}</td><td class="name">{name}</td>'
            f'<td class="small">{dur}</td>'
            f'<td class="num">{_money(std)}</td><td class="num">{_money(early)}</td></tr>'
        )
    return "\n".join(out)


def rate_card_html() -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{base_css()}</style></head><body>

<div class="head">
  <div>
    <div class="eyebrow">Fees &amp; Packages · {YEAR}</div>
    <h1>Course Fees</h1>
  </div>
  <div>{logo_lockup(46, dark=False, show_rule=False)}</div>
</div>

<p class="lede">All fees in Ugandan shillings. Every enrolled learner receives the
full course book, the prompt and template library, 90 days of WhatsApp support
after the course, and a certificate on passing the rubric.</p>

<h2><span class="n">01</span>The AI ladder</h2>
<table>
<tr><th>Code</th><th>Course</th><th>Duration</th><th style="text-align:right">Standard</th><th style="text-align:right">Early bird</th></tr>
{_rows(AI, "")}
</table>
<div class="note"><b>Ladder discount.</b> Complete a tier and enrol in the next
within 60 days: 10 percent off. This is the cheapest way to go from beginner to
advisor, and the fastest route to earning from AI.</div>

<h2><span class="n">02</span>Business &amp; creative</h2>
<table>
<tr><th>Code</th><th>Course</th><th>Duration</th><th style="text-align:right">Standard</th><th style="text-align:right">Early bird</th></tr>
{_rows(BUSINESS, "")}
</table>

<h2><span class="n">03</span>Office &amp; digital skills</h2>
<table>
<tr><th>Code</th><th>Course</th><th>Duration</th><th style="text-align:right">Standard</th><th style="text-align:right">Early bird</th></tr>
{_rows(OFFICE, "")}
</table>

<h2><span class="n">04</span>Children &amp; youth</h2>
<table>
<tr><th>Code</th><th>Course</th><th>Duration</th><th style="text-align:right">Standard</th><th style="text-align:right">Early bird</th></tr>
{_rows(YOUTH, "")}
</table>

<h2><span class="n">05</span>Corporate &amp; institutional</h2>
<table>
<tr><th>Package</th><th>Contents</th><th style="text-align:right">Fee (UGX)</th></tr>
{''.join(f'<tr><td class="name">{n}</td><td class="small">{d}</td><td class="num">{_money(p)}</td></tr>' for n, d, p in CORPORATE)}
</table>
<p class="small">Corporate pricing is per engagement, not per head. Prices exclude
venue, devices, internet and travel outside Kampala.</p>

<div class="cols">
<div class="col">
<h2><span class="n">06</span>Digital products</h2>
<table>
<tr><th>Product</th><th style="text-align:right">Price</th></tr>
{''.join(f'<tr><td>{n}</td><td class="num">{_money(p)}</td></tr>' for n, p in DIGITAL)}
</table>
</div>
<div class="col">
<h2><span class="n">07</span>How to enrol</h2>
<p class="small"><b>1.</b> Choose your course and confirm the next intake date.<br>
<b>2.</b> Pay a 50 percent deposit to reserve your place.<br>
<b>3.</b> Attend, build your workflow, pass the rubric.<br>
<b>4.</b> Collect your certificate and your course book.</p>
<div class="note"><b>Group of three or more?</b> Each learner pays the early-bird
rate regardless of date. Bring a colleague.</div>
</div>
</div>

<div class="foot">
  <span>{ORG} &nbsp;·&nbsp; {TAGLINE}</span>
  <span>{AUTHOR} &nbsp;·&nbsp; {AUTHOR_TITLE}</span>
</div>
</body></html>"""


def proposal_sheet_html() -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{base_css()}</style></head><body>

<div class="head">
  <div>
    <div class="eyebrow">Corporate Training · {YEAR}</div>
    <h1>What We Deliver On Site</h1>
  </div>
  <div>{logo_lockup(46, dark=False, show_rule=False)}</div>
</div>

<p class="lede">One page for the person who signs. What we teach, who it is for,
what it costs, and what your staff can do the week after.</p>

<h2><span class="n">01</span>Programmes</h2>
<table>
<tr><th>Package</th><th>Contents</th><th style="text-align:right">Fee (UGX)</th></tr>
{''.join(f'<tr><td class="name">{n}</td><td class="small">{d}</td><td class="num">{_money(p)}</td></tr>' for n, d, p in CORPORATE)}
</table>

<h2><span class="n">02</span>What changes after the training</h2>
<table>
<tr><th>Function</th><th>Before</th><th>After</th></tr>
<tr><td class="name">Correspondence</td><td class="small">Two hours drafting a proposal</td><td class="small">Twenty minutes, edited not written</td></tr>
<tr><td class="name">Reporting</td><td class="small">Half a day consolidating figures</td><td class="small">An hour, with a checked total</td></tr>
<tr><td class="name">Customer replies</td><td class="small">Same questions answered from scratch</td><td class="small">A saved reply bank, edited per customer</td></tr>
<tr><td class="name">Content</td><td class="small">Posts written when someone remembers</td><td class="small">A week scheduled in one sitting</td></tr>
<tr><td class="name">Risk</td><td class="small">Staff pasting client data into public tools</td><td class="small">A signed one-page AI policy</td></tr>
</table>

<h2><span class="n">03</span>What is included</h2>
<div class="cols">
<div class="col">
<p class="small"><b>Included.</b> Facilitation by {AUTHOR}. A printed course book
for every participant. The prompt and template library. Certificates on passing
the rubric. 90 days of WhatsApp support after the final session. A short
pre-course survey to shape the sessions to your staff.</p>
</div>
<div class="col">
<p class="small"><b>Not included.</b> Venue hire, devices, internet, paid software
subscriptions, and travel outside Kampala. We train on your real documents, so
participants should bring work they are allowed to share.</p>
</div>
</div>

<h2><span class="n">04</span>Terms</h2>
<p class="small">Fees are per engagement, not per head. 50 percent on signing,
50 percent on completion. Proposal valid 30 days. Prices in Ugandan shillings and
exclude VAT where applicable. Maximum 15 participants for a two-day department
training; up to 30 for an awareness session.</p>

<div class="note"><b>To book.</b> Confirm the programme and dates, and we issue the
invoice and the pre-course survey the same week.</div>

<div class="foot">
  <span>{ORG} &nbsp;·&nbsp; {TAGLINE}</span>
  <span>{AUTHOR} &nbsp;·&nbsp; {AUTHOR_TITLE}</span>
</div>
</body></html>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [
        (rate_card_html(), OUT / "JDHA-rate-card.pdf", "rate card"),
        (proposal_sheet_html(), OUT / "JDHA-corporate-proposal-sheet.pdf", "proposal sheet"),
    ]
    for html, path, label in jobs:
        HTML(string=html).write_pdf(path)
        print(f"wrote {path.name} ({label}, {path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
