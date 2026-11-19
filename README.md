# JD Hub Academy

**Practical courses for people who need to earn, not just learn.**

![JD Hub Academy](assets/brand/logo-card.png)

**Author and founder:** Mubogi Gastavas Jordan, President, JD Hub Tech
**Edition:** First, 2026 · Kampala, Uganda

---

## What this is

Nineteen complete course books, a facilitator handbook, a business manual and the
full visual identity for **JD Hub Academy** — the training arm of JD Hub Tech.

Every book is a complete, print-ready PDF. Every module ends with an exercise.
Every course ends with a capstone assessed against a published rubric. Every cover,
banner and illustration is generated from code in this repository, so the whole
library stays visually consistent and can be rebuilt at any time.

**410 pages of curriculum.** Nineteen courses. One coherent system.

---

## The library

### Artificial Intelligence — the four-tier ladder

| Code | Course | Tier | Weeks | Book |
|---|---|---|---|---|
| AI-101 | [AI in Everyday Life & Business](courses/ai-foundation/README.md) | Foundation | 6 | 36 pp |
| AI-201 | [AI Practitioner](courses/ai-practitioner/README.md) | Practitioner | 8 | 24 pp |
| AI-301 | [AI Builder](courses/ai-builder/README.md) | Builder | 8 | 19 pp |
| AI-401 | [AI Specialist & Advisor](courses/ai-specialist/README.md) | Specialist | 6 | 19 pp |

The ladder is the commercial heart of the Academy. Each tier's capstone is the
entry requirement for the next, and the final module of every book names the tier
above it. A learner who climbs it is worth four enrolments and refers others.

### Business, marketing and money

| Code | Course | Weeks | Book |
|---|---|---|---|
| LD-001 | [From Scratch to President](courses/leadership/README.md) | 52 | 68 pp |
| BZ-230 | [Business Growth & Sales Systems](courses/business-growth/README.md) | 8 | 19 pp |
| MK-220 | [Digital Marketing](courses/digital-marketing/README.md) | 8 | 20 pp |
| FN-150 | [Financial & SACCO Management](courses/financial-sacco/README.md) | 6 | 18 pp |

### Design, content and media

| Code | Course | Weeks | Book |
|---|---|---|---|
| DS-140 | [Graphic Design](courses/graphic-design/README.md) | 6 | 17 pp |
| DS-210 | [Content Creation & Storytelling](courses/content-creation/README.md) | 6 | 21 pp |

### Microsoft Office

| Code | Course | Weeks | Book |
|---|---|---|---|
| MS-160 | [Microsoft Word](courses/microsoft-word/README.md) | 2 | 16 pp |
| MS-170 | [Microsoft Excel](courses/microsoft-excel/README.md) | 2 | 18 pp |
| MS-180 | [Microsoft PowerPoint](courses/microsoft-powerpoint/README.md) | 2 | 16 pp |
| MS-190 | [Microsoft Access](courses/microsoft-access/README.md) | 2 | 17 pp |
| MS-195 | [Word + Excel Combo](courses/word-excel-combo/README.md) | 2 | 18 pp |
| MS-200 | [Microsoft Office Suite](courses/microsoft-office-suite/README.md) | 4 | 16 pp |

### Foundation and STEM

| Code | Course | Weeks | Book |
|---|---|---|---|
| SW-110 | [Scratch Coding](courses/scratch-coding/README.md) | 8 | 15 pp |
| SW-120 | [Basic Digital Literacy](courses/digital-literacy/README.md) | 4 | 17 pp |
| ST-130 | [Practical STEM](courses/practical-stem/README.md) | 10 | 16 pp |

Full details: **[CATALOGUE.md](CATALOGUE.md)**

---

## The flagship book

**From Scratch to President** is not a course. It is a fifty-two week manual:
one principle and one task per week, for building a life of consequence from
whatever you currently have.

The principles are mechanical, not motivational. Price your work properly. Know
your break-even. Document what you do. Say the difficult thing. Build the second
line. The tasks take a day each. Done in sequence, they produce a foundation.

It is the book to read alongside any other course in this library, and to re-read
every year.

[Read it →](courses/leadership/README.md)

---

## For facilitators and institutions

- **[Cohort Calendar](business/COHORT-CALENDAR.md)** — every intake, date, slot and enrolment window for 2026–2027, with the AI ladder checked against its own 60-day promise.
- **[AI-101 Delivery Plan](business/AI-101-DELIVERY-PLAN.md)** — the session-by-session teaching script: demos, lab tasks, exit tests, and what to watch for.
- **[Facilitator Handbook](business/FACILITATOR-HANDBOOK.md)** — session shapes, learner types, difficult conversations, cohort preparation.
- **[Business Manual](business/BUSINESS-MANUAL.md)** — pricing, unit economics, sales process, the AI ladder strategy, growth path, risk register.
- **[Enrolment Handbook](business/ENROLMENT-HANDBOOK.md)** — the learner-facing document, from enquiry to certificate.

### Client documents

Print-ready and fill-in-the-blank, in `templates/`:

| Document | Use |
|---|---|
| [Proposal](templates/PROPOSAL-TEMPLATE.md) | Send within 24 hours of a corporate conversation |
| [Invoice](templates/INVOICE-TEMPLATE.md) | Issue the day the client confirms |
| [Certificate](templates/CERTIFICATE-TEMPLATE.md) | Issued on passing the rubric, not attendance |
| [Register & feedback](templates/REGISTER-AND-FEEDBACK.md) | Print both; paper beats a link in the room |

Generated PDFs:

- `build/JDHA-cohort-calendar.pdf` — the intake calendar, branded, for staff and partners.
- `build/JDHA-rate-card.pdf` — the full fee schedule, two pages, branded.
- `build/JDHA-corporate-proposal-sheet.pdf` — one page for the person who signs.

```bash
python scripts/build_rate_card.py

python scripts/build_certificate.py \
  --name "Grace Nakato" --course ai-foundation \
  --date 2026-03-14 --number JDHA-AI101-2026-001
```

Add `--attendance` for the attendance variant. Never use it for a learner who
passed the rubric — the value of the completion certificate depends on the
distinction.

---

## The visual system

The brand follows JD Hub Tech exactly: midnight navy ground, gold and cobalt
accents, brand red for calls to action, using the production logo and the real
`--jd-*` palette from the main website.

| Asset | Count | Location |
|---|---|---|
| Book covers (1080 × 1528) | 19 | `assets/covers/` |
| Wide banners (1600 × 900) | 19 | `assets/covers/` |
| Concept illustrations (1600 × 1200) | 19 | `assets/illustrations/` |
| Logo card (1080 × 1080) | 1 | `assets/brand/` |
| Vector logo (light + dark) | 2 | `assets/brand/` |

Every image is generated from code. To restyle the entire library, change the
palette in `scripts/brand.py` and re-run the build.

---

## Building it yourself

```bash
pip install weasyprint markdown pymdown-extensions pypdf Pillow numpy pymupdf

# Generate all covers, banners and illustrations (requires chromium)
python scripts/build_assets.py

# Generate all 19 PDF books
python scripts/build_books.py

# Regenerate the catalogue and per-course READMEs
python scripts/build_index.py

# Fee schedule and corporate proposal sheet
python scripts/build_rate_card.py

# Cohort calendar (markdown + PDF), generated from calendar_plan.py
python scripts/build_calendar.py
```

Individual items:

```bash
python scripts/build_assets.py --only ai-foundation
python scripts/build_books.py  --only ai-foundation
```

### Repository structure

```
assets/brand/          logo, fonts, logo card
assets/covers/         book covers and wide banners
assets/illustrations/  concept illustrations
business/              business manual, handbooks, delivery plan, cohort calendar
templates/             proposal, invoice, certificate, register and feedback
courses/<slug>/        book.md source + README.md for each course
build/                 generated PDFs
scripts/               the entire build system
CATALOGUE.md           the full catalogue
```

### Adding a course

1. Add one dict to `scripts/catalogue.py`.
2. Create `courses/<slug>/book.md` in Markdown.
3. Run `build_assets.py`, `build_books.py`, `build_index.py`.

Cover, banner, illustration, PDF, catalogue entry and README are all produced
automatically.

### Markdown conventions

```markdown
# Module heading          -> chapter, starts a new page
## Lesson heading         -> lesson
::: scripture             -> Scripture callout (with — Reference)
::: exercise              -> exercise callout
::: warn                  -> caution callout
::: box                   -> neutral callout
::: note / prayer / story -> further callout styles
```prompt ... ```          -> monospace prompt block
```

---

## Copyright and licence

Copyright © 2026 **Mubogi Gastavas Jordan**, President, JD Hub Tech. All rights
reserved.

This is proprietary commercial curriculum, not open source. See [LICENSE](LICENSE).

- **Permitted:** enrolled learners printing one copy; facilitators printing for
  their licensed cohort; quoting up to 200 words with attribution.
- **Not permitted:** reselling, rebranding, removing the author's name, or
  delivering paid training outside a JD Hub Academy licence.

Licensing enquiries: JD Hub Academy, JD Hub Tech, Kampala.

---

*"Whatever your hand finds to do, do it with your might."*
— Ecclesiastes 9:10
