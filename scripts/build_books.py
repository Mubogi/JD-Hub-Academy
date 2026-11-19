"""Markdown -> print-ready PDF book pipeline.

Each course lives in `courses/<slug>/book.md` as ordinary Markdown. This module
wraps it in a branded template with a cover page, a title page, a copyright
page, an automatically numbered table of contents, running headers, page
numbers, and a closing colophon — then renders it with WeasyPrint.

Markdown conventions understood by the builder:

    # Heading            -> chapter (starts a new page, numbered)
    ## Heading           -> lesson
    ### Heading          -> sub-section
    ::: scripture        -> scripture / reflection callout (block until :::)
    ::: box              -> neutral callout
    ::: warn             -> caution callout
    ::: exercise         -> exercise callout
    ```prompt             -> monospace prompt block

Run:  python scripts/build_books.py [--only slug]
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import markdown
from weasyprint import HTML

from brand import (
    ACCENTS, AUTHOR, AUTHOR_TITLE, BLUE, CREAM, CYAN, GOLD, GOLD_2, GOLD_3,
    NAVY, NAVY_2, ORG, RED, WHITE, YEAR, ROOT,
)
from catalogue import COURSES

COURSES_DIR = ROOT / "courses"
BUILD_DIR = ROOT / "build"


# ---------------------------------------------------------------------------
# Markdown extension: ::: blocks
# ---------------------------------------------------------------------------
CALLOUTS = {"scripture", "box", "warn", "exercise", "note", "prayer", "story"}


def _callouts(text: str) -> str:
    """Convert ::: kind ... ::: fences into <div class="callout kind">."""
    out, stack = [], []
    for line in text.split("\n"):
        m = re.match(r"^:::\s*(\w+)\s*$", line.strip())
        if m and m.group(1) in CALLOUTS:
            out.append(f'<div class="callout {m.group(1)}">')
            stack.append(m.group(1))
            continue
        if line.strip() == ":::" and stack:
            out.append("</div>")
            stack.pop()
            continue
        out.append(line)
    while stack:
        out.append("</div>")
        stack.pop()
    return "\n".join(out)


def _md(text: str) -> str:
    return markdown.markdown(
        _callouts(text),
        extensions=["extra", "sane_lists", "toc", "attr_list", "def_list"],
        extension_configs={"toc": {"permalink": False}},
    )


# ---------------------------------------------------------------------------
# Typography
# ---------------------------------------------------------------------------
def print_css(course: dict) -> str:
    acc = ACCENTS.get(course["category"], ACCENTS["software"])
    main = acc["main"]

    return f"""
@font-face{{font-family:'Jakarta';src:url('file://{(ROOT / 'assets/brand/fonts/PlusJakartaSans.ttf').as_posix()}');
  font-weight:100 900;}}
@font-face{{font-family:'Bricolage';src:url('file://{(ROOT / 'assets/brand/fonts/BricolageGrotesque.ttf').as_posix()}');
  font-weight:100 900;}}
@font-face{{font-family:'Mono';src:url('file://{(ROOT / 'assets/brand/fonts/JetBrainsMono.ttf').as_posix()}');
  font-weight:100 900;}}

@page {{
  size: A4;
  margin: 22mm 20mm 20mm 20mm;
  @top-left {{
    content: "{ORG}";
    font-family:'Mono'; font-size:7.5pt; letter-spacing:.16em;
    color:{GOLD_3}; text-transform:uppercase; padding-bottom:3mm;
  }}
  @top-right {{
    content: "{course['title']}";
    font-family:'Jakarta'; font-size:7.5pt; color:#8b96ad; padding-bottom:3mm;
  }}
  @bottom-center {{
    content: counter(page);
    font-family:'Mono'; font-size:8pt; color:{GOLD_3};
  }}
}}
@page :first {{ margin:0; @top-left{{content:none}} @top-right{{content:none}} @bottom-center{{content:none}} }}
@page cover {{ margin:0; @top-left{{content:none}} @top-right{{content:none}} @bottom-center{{content:none}} }}
@page plain {{ @top-left{{content:none}} @top-right{{content:none}} @bottom-center{{content:none}} }}

html {{ font-family:'Jakarta', sans-serif; }}
body {{ font-size:10.6pt; line-height:1.62; color:#1b2233; }}

/* ---------- cover ---------- */
.cover {{ page: cover; width:210mm; height:297mm; position:relative; overflow:hidden;
  background:{NAVY}; color:{CREAM}; page-break-after:always; }}
.cover img.full {{ width:100%; height:100%; object-fit:cover; display:block; }}

/* ---------- front matter ---------- */
.front {{ page: plain; page-break-after:always; }}
.titlepage {{ padding-top:44mm; }}
.titlepage .kicker {{ font-family:'Mono'; font-size:8.5pt; letter-spacing:.24em;
  color:{GOLD_3}; text-transform:uppercase; }}
.titlepage h1 {{ font-family:'Bricolage'; font-size:30pt; line-height:1.08;
  letter-spacing:-.025em; color:{NAVY}; margin:8mm 0 5mm; font-weight:800; }}
.titlepage .sub {{ font-size:13pt; color:#4a5568; line-height:1.45; }}
.titlepage .meta {{ margin-top:26mm; font-size:9.5pt; color:#4a5568; line-height:2; }}
.titlepage .meta b {{ color:{NAVY}; }}
.rule {{ height:3pt; width:44mm; background:{main}; margin:9mm 0; }}

.copyright {{ page: plain; page-break-after:always; font-size:8.6pt; color:#4a5568; line-height:1.72;
  padding-top:20mm; }}
.copyright h2 {{ font-family:'Bricolage'; font-size:12pt; color:{NAVY}; margin:0 0 5mm;
  font-weight:800; }}
.copyright p {{ margin-bottom:3.2mm; }}
.copyright .box {{ border:0.6pt solid #d8dde8; border-radius:2mm; padding:5mm; margin:6mm 0;
  background:#fafbfd; }}
.copyright .box p {{ margin-bottom:2mm; }}

/* ---------- toc ---------- */
.toc {{ page: plain; page-break-after:always; }}
.toc h2 {{ font-family:'Bricolage'; font-size:19pt; color:{NAVY}; margin:0 0 7mm; font-weight:800; }}
.toc ol {{ list-style:none; padding:0; margin:0; }}
.toc li {{ font-size:10pt; padding:2.1mm 0; border-bottom:0.4pt dotted #ccd3e0; color:#2d3748; }}
.toc li .n {{ font-family:'Mono'; font-size:8pt; color:{GOLD_3}; margin-right:3mm; }}

/* ---------- chapters ---------- */
.book h1 {{ page-break-before:always; font-family:'Bricolage'; font-size:21pt; font-weight:800;
  color:{NAVY}; letter-spacing:-.02em; line-height:1.14; margin:0 0 7mm;
  padding-bottom:4mm; border-bottom:2.5pt solid {main}; }}
.book h2 {{ font-family:'Bricolage'; font-size:13.4pt; font-weight:700; color:{NAVY};
  margin:8mm 0 3mm; page-break-after:avoid; }}
.book h3 {{ font-family:'Jakarta'; font-size:11pt; font-weight:700; color:#243b53;
  margin:6mm 0 2mm; page-break-after:avoid; }}
.book h4 {{ font-size:10.4pt; font-weight:700; color:#334155; margin:4mm 0 1.5mm;
  page-break-after:avoid; }}

p {{ margin:0 0 3.4mm; text-align:left; }}
ul, ol {{ margin:0 0 4mm; padding-left:6mm; }}
li {{ margin-bottom:1.6mm; }}
strong {{ color:#0f172a; }}
em {{ color:#334155; }}

table {{ width:100%; border-collapse:collapse; margin:4mm 0 5mm; font-size:9pt;
  page-break-inside:avoid; }}
th {{ background:{NAVY}; color:{CREAM}; text-align:left; padding:2.4mm 3mm;
  font-size:8.4pt; font-weight:700; letter-spacing:.03em; }}
td {{ padding:2.2mm 3mm; border-bottom:0.4pt solid #e2e8f0; vertical-align:top; }}
tr:nth-child(even) td {{ background:#f8fafc; }}

code {{ font-family:'Mono'; font-size:8.8pt; background:#eef2f9; padding:0.6mm 1.4mm;
  border-radius:1mm; color:#1e3a8a; }}
pre {{ font-family:'Mono'; font-size:8.6pt; background:#0f172a; color:#e2e8f0;
  padding:4mm; border-radius:2mm; line-height:1.5; page-break-inside:avoid;
  margin:4mm 0; overflow-wrap:break-word; white-space:pre-wrap; }}
pre code {{ background:none; color:inherit; padding:0; }}

blockquote {{ border-left:2.5pt solid {GOLD}; margin:4mm 0; padding:1mm 0 1mm 5mm;
  color:#4a5568; font-style:italic; }}

/* ---------- callouts ---------- */
.callout {{ margin:4.5mm 0; padding:4.2mm 5mm; border-radius:2mm; font-size:9.7pt;
  page-break-inside:avoid; }}
.callout p:last-child {{ margin-bottom:0; }}
.callout.scripture {{ background:#fdf8ec; border-left:3pt solid {GOLD};
  font-family:'Bricolage'; font-style:italic; color:#5c4a1e; }}
.callout.scripture p {{ font-size:10.2pt; line-height:1.55; }}
.callout.scripture .ref {{ display:block; margin-top:2.5mm; font-family:'Mono';
  font-style:normal; font-size:7.8pt; letter-spacing:.12em; color:{GOLD_3};
  text-transform:uppercase; }}
.callout.exercise {{ background:#eef4ff; border-left:3pt solid {BLUE}; }}
.callout.exercise::before {{ content:"EXERCISE"; display:block; font-family:'Mono';
  font-size:7.6pt; letter-spacing:.2em; color:{BLUE}; margin-bottom:2mm; }}
.callout.warn {{ background:#fef2f2; border-left:3pt solid {RED}; }}
.callout.warn::before {{ content:"CAUTION"; display:block; font-family:'Mono';
  font-size:7.6pt; letter-spacing:.2em; color:{RED}; margin-bottom:2mm; }}
.callout.box {{ background:#f4f7fb; border:0.5pt solid #d6deeb; }}
.callout.note {{ background:#f0fdfa; border-left:3pt solid #0d9488; }}
.callout.prayer {{ background:#f7f4ff; border-left:3pt solid #7c3aed; font-style:italic; }}
.callout.story {{ background:#fffdf5; border:0.5pt solid #ecdfb8; font-style:italic; }}

hr {{ border:none; border-top:0.5pt solid #d8dde8; margin:6mm 0; }}

/* ---------- colophon ---------- */
.colophon {{ page: plain; page-break-before:always; text-align:center; padding-top:60mm; }}
.colophon .mark {{ font-family:'Bricolage'; font-size:26pt; font-weight:800;
  color:{NAVY}; letter-spacing:-.03em; }}
.colophon .mark span {{ color:{BLUE}; }}
.colophon .tag {{ font-family:'Mono'; font-size:8pt; letter-spacing:.3em;
  color:{GOLD_3}; margin-top:5mm; }}
.colophon p {{ font-size:9pt; color:#4a5568; margin-top:12mm; line-height:1.7; }}
"""


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------
def _cover_uri(course: dict) -> str:
    p = ROOT / "assets" / "covers" / f"{course['slug']}.png"
    return p.as_uri() if p.exists() else ""


def _chapters(body_md: str) -> list[str]:
    """Split the Markdown into chapter titles for the table of contents."""
    return [m.group(1).strip() for m in re.finditer(r"^#\s+(.+)$", body_md, re.M)]


def build(course: dict) -> Path:
    src = COURSES_DIR / course["slug"] / "book.md"
    if not src.exists():
        raise FileNotFoundError(src)
    body_md = src.read_text(encoding="utf-8")

    chapters = _chapters(body_md)
    toc_rows = "\n".join(
        f'<li><span class="n">{i:02d}</span>{html_mod.escape(t)}</li>'
        for i, t in enumerate(chapters, 1)
    )

    cover_uri = _cover_uri(course)
    cover_block = (
        f'<div class="cover"><img class="full" src="{cover_uri}"></div>'
        if cover_uri
        else '<div class="cover"></div>'
    )

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<title>{html_mod.escape(course['title'])} — {ORG}</title>
<style>{print_css(course)}</style></head><body>

{cover_block}

<div class="front titlepage">
  <div class="kicker">{ORG} · {html_mod.escape(course['code'])}</div>
  <h1>{html_mod.escape(course['title'])}</h1>
  <div class="sub">{html_mod.escape(course['subtitle'])}</div>
  <div class="rule"></div>
  <div class="meta">
    <b>Author</b> &nbsp; {AUTHOR}<br>
    <b>Position</b> &nbsp; {AUTHOR_TITLE}<br>
    <b>Level</b> &nbsp; {html_mod.escape(course['level'])}<br>
    <b>Duration</b> &nbsp; {html_mod.escape(course['duration'])}<br>
    <b>Edition</b> &nbsp; First Edition, {YEAR}
  </div>
</div>

<div class="copyright">
  <h2>Copyright &amp; Terms of Use</h2>
  <p><b>{html_mod.escape(course['title'])}</b><br>
  {ORG} · Course code {html_mod.escape(course['code'])} · First Edition, {YEAR}</p>
  <p>Copyright &copy; {YEAR} {AUTHOR}, {AUTHOR_TITLE}. All rights reserved.</p>
  <p>This material is the intellectual property of {AUTHOR} and {ORG}. No part of
  this publication may be reproduced, distributed, resold, or transmitted in any
  form or by any means — electronic, mechanical, photocopying, recording, or
  otherwise — without the prior written permission of the copyright holder,
  except in the case of brief quotations embodied in reviews, teaching notes,
  or scholarly work with proper attribution.</p>
  <div class="box">
    <p><b>Permitted without asking</b></p>
    <p>Enrolled learners may print one copy for personal study. Facilitators
    delivering a licensed {ORG} cohort may print copies for that cohort. Quoting
    up to 200 words with the attribution “{AUTHOR}, {ORG}” is permitted.</p>
    <p><b>Not permitted without a written licence</b></p>
    <p>Reselling this document, removing the author's name, rebranding it as your
    own course, uploading it to a file-sharing site, or using it to deliver
    paid training outside a {ORG} licence.</p>
  </div>
  <p><b>Disclaimer.</b> This course is educational. It does not constitute legal,
  tax, medical, or investment advice. Artificial-intelligence tools change
  frequently; tool names, features and pricing described here were accurate at
  the time of writing and may change. Always verify current terms with the
  vendor before relying on a tool commercially.</p>
  <p><b>Scripture quotations.</b> Unless otherwise indicated, Scripture quotations
  are from the Holy Bible, New King James Version (NKJV), &copy; 1982 Thomas
  Nelson. Used for teaching and reflection purposes. Quotations are marked with
  their reference; readers should consult their own Bible for full context.</p>
  <p><b>Contact</b><br>
  {ORG}, {AUTHOR_TITLE}<br>
  JD Hub Tech · Kampala, Uganda</p>
  <p style="margin-top:8mm;font-family:'Mono';font-size:7.5pt;letter-spacing:.14em;color:{GOLD_3}">
  {ORG.upper()} · LEARN · BUILD · EARN</p>
</div>

<div class="toc">
  <h2>Contents</h2>
  <ol>{toc_rows}</ol>
</div>

<div class="book">
{_md(body_md)}
</div>

<div class="colophon">
  <div class="mark">JD Hub <span>Academy</span></div>
  <div class="tag">LEARN · BUILD · EARN</div>
  <p>
    <b>{AUTHOR}</b><br>{AUTHOR_TITLE}<br><br>
    {html_mod.escape(course['title'])} · {html_mod.escape(course['code'])}<br>
    First Edition · {YEAR}<br><br>
    “Whatever you do, do it heartily, as to the Lord and not to men.”<br>
    Colossians 3:23
  </p>
</div>

</body></html>"""

    out = BUILD_DIR / f"{course['code']}-{course['slug']}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=doc, base_url=str(ROOT)).write_pdf(out)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="build a single course slug")
    args = ap.parse_args()

    built = 0
    for c in COURSES:
        if args.only and c["slug"] != args.only:
            continue
        src = COURSES_DIR / c["slug"] / "book.md"
        if not src.exists():
            print(f"  skip  {c['slug']:28s} (no book.md yet)")
            continue
        out = build(c)
        size = out.stat().st_size / 1024
        print(f"  built {out.name:52s} {size:7.0f} KB")
        built += 1
    print(f"\n{built} book(s) written to {BUILD_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
