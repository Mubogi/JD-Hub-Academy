# JD Hub Academy — Course Catalogue

**Mubogi Gastavas Jordan**, President, JD Hub Tech
First Edition · 2026 · 19 courses · 410 printed pages

---

## The catalogue

| Course | Code | Level | Duration | Pages |
|---|---|---|---|---|
| [From Scratch to President](courses/leadership/README.md) | LD-001 | Everyone | 52 weeks | 68 |
| [AI in Everyday Life & Business](courses/ai-foundation/README.md) | AI-101 | Beginner | 6 weeks | 36 |
| [AI Practitioner](courses/ai-practitioner/README.md) | AI-201 | Intermediate | 8 weeks | 24 |
| [AI Builder](courses/ai-builder/README.md) | AI-301 | Advanced | 8 weeks | 19 |
| [AI Specialist & Advisor](courses/ai-specialist/README.md) | AI-401 | Professional | 6 weeks | 19 |
| [Scratch Coding](courses/scratch-coding/README.md) | SW-110 | Beginner | 8 weeks | 15 |
| [Basic Digital Literacy](courses/digital-literacy/README.md) | SW-120 | Beginner | 4 weeks | 17 |
| [Practical STEM](courses/practical-stem/README.md) | ST-130 | Beginner to Intermediate | 10 weeks | 16 |
| [Graphic Design](courses/graphic-design/README.md) | DS-140 | Beginner to Intermediate | 6 weeks | 17 |
| [Financial & SACCO Management](courses/financial-sacco/README.md) | FN-150 | Intermediate | 6 weeks | 18 |
| [Microsoft Word](courses/microsoft-word/README.md) | MS-160 | Beginner to Intermediate | 2 weeks | 16 |
| [Microsoft Excel](courses/microsoft-excel/README.md) | MS-170 | Beginner to Intermediate | 2 weeks | 18 |
| [Microsoft PowerPoint](courses/microsoft-powerpoint/README.md) | MS-180 | Beginner to Intermediate | 2 weeks | 16 |
| [Microsoft Access](courses/microsoft-access/README.md) | MS-190 | Intermediate to Advanced | 2 weeks | 17 |
| [Microsoft Word + Excel Combo](courses/word-excel-combo/README.md) | MS-195 | Beginner to Intermediate | 2 weeks | 18 |
| [Content Creation & Storytelling](courses/content-creation/README.md) | DS-210 | Beginner to Intermediate | 6 weeks | 21 |
| [Digital Marketing](courses/digital-marketing/README.md) | MK-220 | Beginner to Intermediate | 8 weeks | 20 |
| [Business Growth & Sales Systems](courses/business-growth/README.md) | BZ-230 | Intermediate | 8 weeks | 19 |
| [Microsoft Office Suite (All Tools)](courses/microsoft-office-suite/README.md) | MS-200 | Beginner to Advanced | 4 weeks | 16 |

---

## The AI ladder

The AI courses are designed as a ladder. Each tier has a capstone that becomes the
entry requirement for the next, so a learner who finishes one has a genuine reason
to return — and a genuine reason to be ready.

| # | Course | Tier | Duration | Book |
|---|---|---|---|---|
| 1 | **AI-101** AI in Everyday Life & Business | Foundation | 6 weeks · 12 sessions · 24 contact hours | [Open](courses/ai-foundation/README.md) |
| 2 | **AI-201** AI Practitioner | Practitioner | 8 weeks · 16 sessions · 32 contact hours | [Open](courses/ai-practitioner/README.md) |
| 3 | **AI-301** AI Builder | Builder | 8 weeks · 16 sessions · 32 contact hours | [Open](courses/ai-builder/README.md) |
| 4 | **AI-401** AI Specialist & Advisor | Specialist | 6 weeks · 12 sessions · 24 contact hours | [Open](courses/ai-specialist/README.md) |

**Why the ladder matters:** a learner who takes one course is worth one course. A
learner who climbs the ladder is worth four, refers others, and eventually becomes
a facilitator. The final module of every AI book names the next tier explicitly.

---

## What every course includes

- A complete course book (PDF, 410 pages across the library)
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

Copyright © 2026 Mubogi Gastavas Jordan, President, JD Hub Tech. All rights reserved.

See [LICENSE](LICENSE) for the full terms. In short: learners may print their own
copy, facilitators may print for their cohort, and nobody may resell or rebrand
the material.
