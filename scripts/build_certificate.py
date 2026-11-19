"""Generate a print-ready certificate of completion (A4 landscape).

Usage:
    python3 scripts/build_certificate.py \
        --name "Grace Nakato" \
        --course ai-foundation \
        --date 2026-03-14 \
        --number JDHA-AI101-2026-001 \
        [--attendance] \
        [--out build/certificates/grace-nakato.pdf]

Without --out the file lands in build/certificates/<slugified name>.pdf.
--attendance issues the attendance variant, which must never be used for a
learner who passed the rubric.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
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
from catalogue import COURSES  # noqa: E402

FONTS = BRAND_ROOT / "assets" / "brand" / "fonts"
OUT = ROOT / "build" / "certificates"


def _face(fam: str, fn: str, weight: str = "100 900", style: str = "normal") -> str:
    return (
        "@font-face{font-family:'%s';src:url('file://%s') format('truetype');"
        "font-weight:%s;font-style:%s;font-display:block;}"
        % (fam, (FONTS / fn).as_posix(), weight, style)
    )


def css() -> str:
    return f"""
{_face('Jakarta','PlusJakartaSans.ttf')}
{_face('Bricolage','BricolageGrotesque.ttf')}
{_face('Code','JetBrainsMono-Regular.ttf','400')}
{_face('Code','JetBrainsMono-Bold.ttf','700')}
{_face('Serif','SourceSerif4.ttf')}
{_face('Serif','SourceSerif4-Italic.ttf','100 900','italic')}

@page {{ size: A4 landscape; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  width: 297mm; height: 210mm; background: #ffffff;
  font-family: 'Serif'; color: {NAVY}; position: relative; overflow: hidden;
}}

/* Outer frame: hairline, then a heavier inner rule. Two rules read as
   "printed document" rather than "printout". */
.frame {{
  position: absolute; inset: 9mm;
  border: .5pt solid #cfd4de;
}}
.frame::after {{
  content: ""; position: absolute; inset: 3.5mm;
  border: 2.2pt solid {NAVY};
}}
.corner {{
  position: absolute; width: 16mm; height: 16mm;
  border-top: 3pt solid {GOLD_DEEP};
}}
.c1 {{ top: 3.5mm; left: 3.5mm; border-left: 3pt solid {GOLD_DEEP}; }}
.c2 {{ top: 3.5mm; right: 3.5mm; border-right: 3pt solid {GOLD_DEEP}; }}
.c3 {{ bottom: 3.5mm; left: 3.5mm; border-left: 3pt solid {GOLD_DEEP};
       border-top: 0; border-bottom: 3pt solid {GOLD_DEEP}; }}
.c4 {{ bottom: 3.5mm; right: 3.5mm; border-right: 3pt solid {GOLD_DEEP};
       border-top: 0; border-bottom: 3pt solid {GOLD_DEEP}; }}

.inner {{
  position: absolute; inset: 20mm 24mm;
  display: flex; flex-direction: column; align-items: center;
  text-align: center;
}}

.brand {{ margin-bottom: 9mm; }}
.eyebrow {{
  font-family: 'Code'; font-size: 7.4pt; letter-spacing: .42em;
  text-transform: uppercase; color: {GOLD_3}; margin-bottom: 3.5mm;
}}
h1 {{
  font-family: 'Bricolage'; font-weight: 800; font-size: 30pt;
  letter-spacing: -.03em; line-height: 1; color: {NAVY};
}}
h1 .thin {{ font-weight: 300; }}

.lead {{
  font-family: 'Serif'; font-style: italic; font-size: 10.5pt;
  color: #4a5266; margin: 6mm 0 2mm;
}}
.name {{
  font-family: 'Bricolage'; font-weight: 800; font-size: 27pt;
  letter-spacing: -.02em; color: {NAVY};
  border-bottom: 1.2pt solid {GOLD_DEEP}; padding: 0 6mm 2.5mm;
  margin-bottom: 6mm; min-width: 120mm;
}}
.body {{ font-size: 10.2pt; color: #3a4256; max-width: 175mm; line-height: 1.5; }}
.course {{
  font-family: 'Bricolage'; font-weight: 700; font-size: 15pt;
  color: {NAVY}; margin: 1.5mm 0;
}}
.course .code {{
  font-family: 'Code'; font-size: 8.6pt; letter-spacing: .16em;
  color: {GOLD_3}; font-weight: 400;
}}

.awarded {{
  font-family: 'Code'; font-size: 8pt; letter-spacing: .2em;
  text-transform: uppercase; color: #6b7387; margin-top: 7mm;
}}

.sigs {{
  position: absolute; bottom: 4mm; left: 0; right: 0;
  display: flex; justify-content: space-around; align-items: flex-end;
}}
.sig {{ width: 62mm; }}
.sig .line {{
  border-top: .9pt solid {NAVY}; margin-bottom: 2mm; height: 11mm;
}}
.sig .who {{ font-size: 8.6pt; font-weight: 600; color: {NAVY}; }}
.sig .role {{
  font-family: 'Code'; font-size: 6.4pt; letter-spacing: .13em;
  text-transform: uppercase; color: #7a8296; margin-top: .8mm;
}}

.serial {{
  position: absolute; bottom: -9mm; left: 0; right: 0;
  font-family: 'Code'; font-size: 6.6pt; letter-spacing: .16em;
  color: #98a0b0;
}}

.seal {{
  position: absolute; bottom: 30mm; left: 30mm;
  width: 24mm; height: 24mm; border-radius: 50%;
  border: 1.6pt solid {GOLD_DEEP};
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; transform: rotate(-8deg);
}}
.seal .t1 {{
  font-family: 'Bricolage'; font-weight: 800; font-size: 11pt;
  color: {GOLD_DEEP}; line-height: 1;
}}
.seal .t2 {{
  font-family: 'Code'; font-size: 4.4pt; letter-spacing: .16em;
  color: {GOLD_3}; margin-top: 1mm;
}}
"""


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def certificate_html(
    name: str,
    course: dict,
    issued: date,
    number: str,
    attendance: bool = False,
) -> str:
    kind = "Attendance" if attendance else "Completion"
    if attendance:
        body = (
            f"attended the {course['duration']} programme"
        )
        eyebrow = "Certificate of Attendance"
    else:
        body = (
            "has successfully completed this programme and has been assessed "
            "against the published rubric for the course"
        )
        eyebrow = "Certificate of Completion"

    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>{css()}</style></head><body>

<div class="frame">
  <span class="corner c1"></span><span class="corner c2"></span>
  <span class="corner c3"></span><span class="corner c4"></span>
</div>

<div class="inner">
  <div class="brand">{logo_lockup(40, dark=False, show_rule=False)}</div>

  <div class="eyebrow">{eyebrow}</div>
  <h1>{kind} <span class="thin">Certificate</span></h1>

  <div class="lead">This is to certify that</div>
  <div class="name">{name}</div>

  <div class="body">{body}</div>
  <div class="course">{course['title']}<br>
    <span class="code">{course['code']} &nbsp;·&nbsp; {course['level']}</span>
  </div>

  <div class="awarded">Awarded this {issued.strftime('%-d')} day of
    {issued.strftime('%B')}, {issued.year}</div>

  <div class="sigs">
    <div class="sig">
      <div class="line"></div>
      <div class="who">{AUTHOR}</div>
      <div class="role">{AUTHOR_TITLE}</div>
    </div>
    <div class="sig">
      <div class="line"></div>
      <div class="who">Assessor</div>
      <div class="role">JD Hub Academy</div>
    </div>
  </div>

  <div class="serial">Certificate number {number} &nbsp;·&nbsp;
    Verify with {ORG}</div>
</div>

<div class="seal">
  <div class="t1">{YEAR}</div>
  <div class="t2">JD HUB</div>
</div>

</body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate a JD Hub Academy certificate.")
    ap.add_argument("--name", required=True, help="learner full name")
    ap.add_argument("--course", required=True, help="course slug, e.g. ai-foundation")
    ap.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD")
    ap.add_argument("--number", default=None, help="certificate number")
    ap.add_argument("--attendance", action="store_true", help="attendance variant")
    ap.add_argument("--out", default=None, help="output PDF path")
    args = ap.parse_args()

    course = next((c for c in COURSES if c["slug"] == args.course), None)
    if course is None:
        slugs = ", ".join(c["slug"] for c in COURSES)
        sys.exit(f"unknown course '{args.course}'. Choose from: {slugs}")

    issued = date.fromisoformat(args.date)
    number = args.number or f"JDHA-{course['code'].replace('-','')}-{issued.year}-001"
    out = Path(args.out) if args.out else OUT / f"{_slug(args.name)}-{course['slug']}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)

    HTML(string=certificate_html(args.name, course, issued, number, args.attendance)).write_pdf(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
