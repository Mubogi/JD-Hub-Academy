"""Generate the catalogue index and the per-course README files.

Run:  python scripts/build_index.py

Produces:
  CATALOGUE.md                  — the full course catalogue
  courses/<slug>/README.md      — a landing page for each course
  assets/covers/INDEX.md        — a visual index of all covers
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from brand import ACCENTS, AUTHOR, AUTHOR_TITLE, ORG, ROOT, YEAR
from catalogue import COURSES

COURSES_DIR = ROOT / "courses"


def _rel(from_dir: Path, target: Path) -> str:
    return Path(target).relative_to(from_dir).as_posix()


def catalogue_md() -> str:
    total_pages = 0
    build = ROOT / "build"
    rows = []
    for c in COURSES:
        pdf = build / f"{c['code']}-{c['slug']}.pdf"
        pages = ""
        if pdf.exists():
            try:
                from pypdf import PdfReader

                pages = str(len(PdfReader(pdf).pages))
                total_pages += int(pages)
            except Exception:
                pages = "—"
        rows.append(
            f"| [{c['title']}](courses/{c['slug']}/README.md) | {c['code']} | "
            f"{c['level'].split('—')[0].strip()} | {c['duration'].split('·')[0].strip()} | {pages} |"
        )

    ai = [c for c in COURSES if c["category"] == "ai"]
    ladder = "\n".join(
        f"| {i} | **{c['code']}** {c['title']} | {c['tier']} | {c['duration']} | "
        f"[Open](courses/{c['slug']}/README.md) |"
        for i, c in enumerate(ai, 1)
    )

    return f"""# {ORG} — Course Catalogue

**{AUTHOR}**, {AUTHOR_TITLE}
First Edition · {YEAR} · {len(COURSES)} courses · {total_pages} printed pages

---

## The catalogue

| Course | Code | Level | Duration | Pages |
|---|---|---|---|---|
{chr(10).join(rows)}

---

## The AI ladder

The AI courses are designed as a ladder. Each tier has a capstone that becomes the
entry requirement for the next, so a learner who finishes one has a genuine reason
to return — and a genuine reason to be ready.

| # | Course | Tier | Duration | Book |
|---|---|---|---|---|
{ladder}

**Why the ladder matters:** a learner who takes one course is worth one course. A
learner who climbs the ladder is worth four, refers others, and eventually becomes
a facilitator. The final module of every AI book names the next tier explicitly.

---

## What every course includes

- A complete course book (PDF, {total_pages} pages across the library)
- Module-by-module lessons with an exercise at the end of each
- A capstone project assessed against a published rubric
- A prompt or template library
- Scripture and reflection where applicable
- A certificate stating contact hours, tools covered, and capstone title

---

## How the books are built

Every book in this repository is generated from Markdown source in `courses/`.
Covers, banners and illustrations are generated from code in `scripts/`. Nothing
is hand-assembled, which means the whole library can be rebuilt, restyled or
re-branded by changing a few values in `scripts/brand.py`.

```
scripts/brand.py       brand palette, fonts, renderer
scripts/art.py         vector icons and illustrations
scripts/catalogue.py   the course list — the single source of truth
scripts/build_assets.py  covers, banners, illustrations
scripts/build_books.py   Markdown to print-ready PDF
scripts/build_index.py   this catalogue and the per-course READMEs
```

To add a course: add one entry to `scripts/catalogue.py`, create
`courses/<slug>/book.md`, and run both build scripts.

---

## Copyright

Copyright © {YEAR} {AUTHOR}, {AUTHOR_TITLE}. All rights reserved.

See [LICENSE](LICENSE) for the full terms. In short: learners may print their own
copy, facilitators may print for their cohort, and nobody may resell or rebrand
the material.
"""


def course_readme(c: dict) -> str:
    acc = ACCENTS.get(c["category"], ACCENTS["software"])
    here = COURSES_DIR / c["slug"]
    cover = Path("..") / ".." / "assets" / "covers" / f"{c['slug']}.png"
    banner = Path("..") / ".." / "assets" / "covers" / f"{c['slug']}-wide.png"
    illus = Path("..") / ".." / "assets" / "illustrations" / f"{c['slug']}.png"
    pdf = Path("..") / ".." / "build" / f"{c['code']}-{c['slug']}.pdf"

    pages = ""
    real_pdf = ROOT / "build" / f"{c['code']}-{c['slug']}.pdf"
    if real_pdf.exists():
        try:
            from pypdf import PdfReader

            pages = f"{len(PdfReader(real_pdf).pages)} pages"
        except Exception:
            pass

    outcomes = "\n".join(f"- {o}" for o in c["outcomes"])

    # Extract module and lesson headings for the contents list.
    book = here / "book.md"
    toc = []
    if book.exists():
        for line in book.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                toc.append(f"- **{line[2:].strip()}**")
            elif line.startswith("## "):
                toc.append(f"  - {line[3:].strip()}")
    toc_md = "\n".join(toc) if toc else "_Content in production._"

    return f"""# {c['title']}

> {c['subtitle']}

![{c['title']} cover]({cover.as_posix()})

**Course code:** {c['code']} &nbsp;·&nbsp; **Level:** {c['level']}
&nbsp;·&nbsp; **Duration:** {c['duration']}
&nbsp;·&nbsp; **Book:** {pages or 'in build'}

**Author:** {AUTHOR}, {AUTHOR_TITLE} · {ORG}

---

## What this course is

{c['summary']}

**Who it is for:** {c['audience']}

**Prerequisites:** {c['prereqs']}

**Next step:** {c['next']}

---

## What you will be able to do

{outcomes}

---

## Contents

{toc_md}

---

## The book

- [Download the PDF]({pdf.as_posix()}) — complete course book, print-ready
- [Cover image]({cover.as_posix()})
- [Wide banner]({banner.as_posix()})
- [Concept illustration]({illus.as_posix()})

---

## Assessment

Every course in this library is assessed against a published rubric, printed in
the final module of the book. The pass mark is 60 percent, and the practical
component is mandatory regardless of total score.

The certificate states the learner's name, the course title, contact hours, tools
covered, the capstone title, and the date.

---

Copyright © {YEAR} {AUTHOR}, {AUTHOR_TITLE}. All rights reserved.
See [LICENSE](../../LICENSE).
"""


def main() -> None:
    (ROOT / "CATALOGUE.md").write_text(catalogue_md(), encoding="utf-8")
    print("wrote CATALOGUE.md")

    for c in COURSES:
        d = COURSES_DIR / c["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "README.md").write_text(course_readme(c), encoding="utf-8")
    print(f"wrote {len(COURSES)} course READMEs")


if __name__ == "__main__":
    main()
