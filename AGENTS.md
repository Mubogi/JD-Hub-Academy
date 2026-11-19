# AGENTS.md — JD Hub Academy

Repository-specific knowledge for future sessions.

## What this repo is

The complete curriculum library for **JD Hub Academy**, the training arm of JD Hub
Tech (Kampala, Uganda). Owner and author: **Mubogi Gastavas Jordan, President, JD
Hub Tech** — credited on every document, every cover, every PDF copyright page.

Commercial product, not open source. See `LICENSE`.

## The one rule that matters

**`scripts/catalogue.py` is the single source of truth.** Every course, cover,
banner, illustration, PDF and README derives from the `COURSES` list there. To add
a course: add a dict, create `courses/<slug>/book.md`, run the three build scripts.
Nothing else needs editing.

## Build commands

```bash
python scripts/build_assets.py            # covers, banners, illustrations (~10 min, needs chromium)
python scripts/build_books.py             # 19 PDFs via WeasyPrint (~2 min)
python scripts/build_index.py             # CATALOGUE.md + per-course READMEs

# single item
python scripts/build_assets.py --only ai-foundation
python scripts/build_books.py  --only ai-foundation
```

Dependencies: `weasyprint markdown pymdown-extensions pypdf Pillow numpy pymupdf`
plus a chromium binary for the asset renderer.

## Brand system

`scripts/brand.py` holds the palette, fonts and renderer. It mirrors the real
`--jd-*` custom properties from the JD Hub website — do not invent new colours.

| Token | Value | Use |
|---|---|---|
| ink | `#060b18` | Page ground |
| gold | `#e3a821` / `#ffd166` | Primary accent |
| blue | `#1d4fd6` | Secondary accent |
| cyan | `#2fd6cd` | Tertiary accent |
| red | `#c8102e` | Emphasis / rules |

Fonts: Bricolage Grotesque (display), Plus Jakarta Sans (body), JetBrains Mono
(code). Vendored in `assets/brand/fonts/`.

Logo files: `logo.svg`, `logo-light.svg`, `logo-mark.png`, `logo-card.png`. Copied
from the `Mubogi/jd-hub` source repo — regenerate from there if the brand changes.

## Book conventions

`book.md` uses a small set of custom callout blocks parsed by `build_books.py`:

```
::: scripture    cream callout, for Scripture with "— Reference"
::: exercise     blue callout, the lab at the end of every module
::: warn         red-tinted caution
::: box          neutral
::: note / prayer / story
```

Structure: `# ` = module (starts a new page), `## ` = lesson. Every module ends
with an exercise. Every course ends with a capstone and a rubric.

**Every book must include Scripture references where applicable** — this is a hard
requirement from the owner, not decoration. Keep them relevant, not preachy.

## Known constraints

- WeasyPrint scopes chapter `h1` styles to `.book` — this stops the title page
  from breaking. Do not remove that scope.
- Page 1 of every PDF is a full-bleed cover image with a 6px bleed. `get_text()`
  returns empty for it; that is expected, not a bug.
- `build_index.py` resolves the PDF path from `ROOT`, not CWD. It previously had a
  bug where it reported "in build" — do not reintroduce a CWD-relative check.
- Asset generation is slow (~10 min for 57 images). Run it in the background with
  `nohup` and poll the log; foreground commands are capped at ~1080s.
- Access database guidance in `FN-150`/`MS-190` deliberately warns against shared
  cloud folders — that is a real corruption cause, not filler.

## Verification habits that caught real bugs

- Scan all PDFs for text blocks beyond margins, filtering page numbers in the
  footer zone (`y > 800`), or you get 313 false positives.
- For banner text bounds, filter to near-white pixels (`min>190`, `max-min<40`);
  otherwise the cyan accent strip reads as "text" and every banner looks clipped.
- Check cover footers end by `y=1500` and artwork stays above `y=1300`.

## Commercial context

`business/BUSINESS-MANUAL.md` holds pricing, unit economics and the AI-ladder
retention strategy. The ladder (AI-101 → 201 → 301 → 401) is the commercial heart:
each tier's capstone gates the next, and the final module of every AI book names
the tier above. Preserve that cross-reference when editing AI books.

Break-even cohort is 7 learners. Never run below it.

## Git

Remote: `Mubogi/JD-Hub-Academy` (public). Default branch `master`. Authenticated as
the `Mubogi` account via `GH_TOKEN`.
