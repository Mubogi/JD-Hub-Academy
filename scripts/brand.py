"""JD Hub Academy design system.

Two layers:

1.  THE BRAND   — the JD Hub identity, fixed. Navy, gold, red, the real logo.
                 These never change between books.
2.  THE THEME   — a per-course palette. Every course carries its own hue so a
                 learner can identify a book by colour before reading the
                 title, and so nineteen books do not look like one book
                 printed nineteen times.

Change a value here, re-run the build scripts, and every cover, banner,
illustration and PDF in the repository updates.
"""

from __future__ import annotations

import base64
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BRAND = ASSETS / "brand"
FONTS = BRAND / "fonts"

# --------------------------------------------------------------------------
# Brand constants — from the JD Hub production stylesheet and the real logo
# file (marketing/JD Hub.png): gold #ffde59, red #ff3131.
# --------------------------------------------------------------------------
NAVY = "#060b18"
NAVY_2 = "#0b1730"
NAVY_3 = "#122043"
GOLD = "#ffde59"          # logo gold
GOLD_DEEP = "#e3a821"     # print-safe gold for rules and small type
GOLD_3 = "#8a6410"
RED = "#ff3131"           # logo red
RED_DEEP = "#c8102e"
INK = "#0d1220"
CREAM = "#fbf8f1"
PAPER = "#ffffff"

AUTHOR = "Mubogi Gastavas Jordan"
AUTHOR_TITLE = "President, JD Hub Tech"
ORG = "JD Hub Academy"
YEAR = "2026"
TAGLINE = "LEARN · BUILD · EARN"

# --------------------------------------------------------------------------
# Themes — one per course family. Each carries a full ramp so that covers,
# chapter rules, callouts and PDF accents all derive from a single source.
#
#   deep    page ground for covers
#   mid     secondary ground / gradient stop
#   accent  the signature hue — the "this book" colour
#   light   a tint for large type and glows
#   ink     body text colour on light pages
#   warm    paper tint for the interior pages
# --------------------------------------------------------------------------
def _t(label, deep, mid, accent, light, ink, warm, g1, g2) -> dict:
    return {
        "label": label, "deep": deep, "mid": mid, "accent": accent,
        "light": light, "ink": ink, "warm": warm, "grad": [g1, g2],
    }


# One entry per course. Family relationships are preserved — the four AI books
# step cyan to violet like a ladder, the six Office books use each product's
# real brand hue — but no two books share a palette.
THEMES: dict[str, dict] = {
    # ---- flagship -------------------------------------------------------
    "leadership": _t("Leadership & Legacy", "#05080f", "#0e1a33",
                     "#ffde59", "#ffe98a", "#0b1426", "#fdfaf0",
                     "#ffde59", "#ff3131"),

    # ---- the AI ladder: cyan -> azure -> indigo -> violet ----------------
    "ai-foundation": _t("AI · Foundation", "#04141c", "#072a38",
                        "#2fd6cd", "#8df5ee", "#0a2a33", "#f2fbfa",
                        "#2fd6cd", "#38bdf8"),
    "ai-practitioner": _t("AI · Practitioner", "#04121f", "#0a2540",
                          "#38bdf8", "#9ad9ff", "#0a2437", "#f2f9ff",
                          "#38bdf8", "#3b82f6"),
    "ai-builder": _t("AI · Builder", "#0a0a24", "#191a4a",
                     "#818cf8", "#c3c8ff", "#15163d", "#f5f5ff",
                     "#818cf8", "#4b7dff"),
    "ai-specialist": _t("AI · Specialist", "#120823", "#2a1149",
                        "#a78bfa", "#d8c7ff", "#22103d", "#faf6ff",
                        "#a78bfa", "#c084fc"),

    # ---- STEM & foundation ---------------------------------------------
    "scratch-coding": _t("Coding for Young Minds", "#1a0c02", "#3a1d05",
                         "#fb923c", "#ffd0a8", "#301404", "#fff8f0",
                         "#fb923c", "#ffde59"),
    "practical-stem": _t("STEM & Making", "#04140d", "#0a2b1c",
                         "#34d399", "#9df3c9", "#08281a", "#f2fdf8",
                         "#34d399", "#0ea5e9"),
    "digital-literacy": _t("Digital Foundations", "#061523", "#0e3050",
                           "#60a5fa", "#b7d8ff", "#0b2740", "#f3f9ff",
                           "#60a5fa", "#2fd6cd"),

    # ---- design & media -------------------------------------------------
    "graphic-design": _t("Design & Visual Craft", "#170519", "#3b0d3f",
                         "#f472b6", "#ffc2e2", "#31093a", "#fff5fb",
                         "#f472b6", "#c084fc"),
    "content-creation": _t("Content & Storytelling", "#1a0410", "#42102c",
                           "#fb7185", "#ffc0cb", "#3a0a1e", "#fff5f7",
                           "#fb7185", "#ff6b6b"),

    # ---- money ----------------------------------------------------------
    "financial-sacco": _t("Finance & Co-operatives", "#02120c", "#0a2e21",
                          "#10b981", "#8ee9c2", "#052a1e", "#f1fdf8",
                          "#10b981", "#34d399"),
    "business-growth": _t("Enterprise & Growth", "#150e01", "#33240a",
                          "#f59e0b", "#ffd89b", "#2b1d04", "#fffbf0",
                          "#f59e0b", "#ffde59"),

    # ---- marketing ------------------------------------------------------
    "digital-marketing": _t("Marketing & Growth", "#1a0507", "#3d0f14",
                            "#ff6b6b", "#ffb3b3", "#3a0d11", "#fff5f5",
                            "#ff6b6b", "#ffde59"),

    # ---- Microsoft Office: each product's real brand hue ----------------
    "microsoft-word": _t("Microsoft Word", "#050c1e", "#122a56",
                         "#4b8bf4", "#aecbff", "#0a1c3d", "#f4f8ff",
                         "#4b8bf4", "#2b579a"),
    "microsoft-excel": _t("Microsoft Excel", "#03140c", "#0b3323",
                          "#21a366", "#8fe0b8", "#04291b", "#f2fdf7",
                          "#21a366", "#217346"),
    "microsoft-powerpoint": _t("Microsoft PowerPoint", "#1a0703", "#3d1508",
                               "#f0672a", "#ffbc9c", "#351105", "#fff7f3",
                               "#f0672a", "#d24726"),
    "microsoft-access": _t("Microsoft Access", "#170406", "#3d0f13",
                           "#e0575b", "#ffb8ba", "#340d10", "#fff5f5",
                           "#e0575b", "#a4373a"),
    "word-excel-combo": _t("Word + Excel Workflow", "#08101f", "#1b2b52",
                           "#5b8def", "#b9cdff", "#0d1c3a", "#f4f7ff",
                           "#5b8def", "#21a366"),
    "microsoft-office-suite": _t("The Complete Office Suite", "#0d0722", "#251348",
                                 "#8b5cf6", "#cfbcff", "#1c0f38", "#f8f5ff",
                                 "#8b5cf6", "#4b8bf4"),
}

# Category-level fallbacks, for any course without its own entry.
CATEGORY_THEME = {
    "ai": "ai-foundation",
    "software": "microsoft-office-suite",
    "stem": "practical-stem",
    "financials": "business-growth",
    "design": "graphic-design",
    "marketing": "digital-marketing",
    "leadership": "leadership",
}

# Backwards-compatible alias used by older call sites.
ACCENTS = {
    k: {"main": v["accent"], "soft": v["mid"], "label": v["label"]}
    for k, v in THEMES.items()
}


def theme_for(course: dict) -> dict:
    """Resolve a course to its palette: slug first, then category."""
    slug = course.get("slug", "")
    if slug in THEMES:
        return THEMES[slug]
    cat = course.get("category", "software")
    return THEMES[CATEGORY_THEME.get(cat, "microsoft-office-suite")]


def theme(key: str) -> dict:
    """Resolve a theme by slug or category key."""
    if key in THEMES:
        return THEMES[key]
    return THEMES[CATEGORY_THEME.get(key, "microsoft-office-suite")]


def font_face_css() -> str:
    """@font-face rules for the vendored families."""
    faces = [
        ("Bricolage", "BricolageGrotesque.ttf", "100 900", "normal"),
        ("Jakarta", "PlusJakartaSans.ttf", "100 900", "normal"),
        ("Code", "JetBrainsMono-Regular.ttf", "400", "normal"),
        ("Code", "JetBrainsMono-Bold.ttf", "700", "normal"),
        ("Serif", "SourceSerif4.ttf", "100 900", "normal"),
        ("Serif", "SourceSerif4-Italic.ttf", "100 900", "italic"),
    ]
    return "\n".join(
        "@font-face{font-family:'%s';src:url('file://%s') format('truetype');"
        "font-weight:%s;font-style:%s;font-display:block;}"
        % (fam, (FONTS / fn).as_posix(), w, style)
        for fam, fn, w, style in faces
    )


def base_css() -> str:
    """Reset and type utilities shared by every rendered page."""
    return f"""
{font_face_css()}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{-webkit-font-smoothing:antialiased;text-rendering:geometricPrecision;}}
body{{font-family:'Jakarta',sans-serif;background:{NAVY};color:{CREAM};
  width:100%;height:100%;overflow:hidden;}}
.display{{font-family:'Bricolage',sans-serif;font-weight:800;
  letter-spacing:-.028em;line-height:.94;}}
.mono{{font-family:'Code',monospace;letter-spacing:.16em;text-transform:uppercase;}}
.noise{{
  position:absolute;inset:0;opacity:.045;pointer-events:none;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");
}}
"""


# ---------------------------------------------------------------------------
# The logo lockup
#
# The real mark is a gold rounded frame enclosing red "JD" letterforms on a
# white ground. It is raster and white-backed, so it cannot be dropped onto a
# dark cover as-is. _mark_png knocks the white ground out once and caches the
# result; logo_lockup then sets it beside live type so the whole lockup scales
# as one object.
# ---------------------------------------------------------------------------
def _mark_png(dark: bool = True) -> Path:
    """A transparent-ground version of the real logo mark (cached)."""
    out = BRAND / ("logo-mark-dark.png" if dark else "logo-mark-light.png")
    if out.exists():
        return out
    src = BRAND / "logo-mark.png"
    if not src.exists():
        return src
    from PIL import Image

    im = Image.open(src).convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            if r > 232 and g > 232 and b > 232:
                px[x, y] = (r, g, b, 0)
    im.save(out, optimize=True)
    return out


def logo_mark(size: int = 96, dark: bool = True) -> str:
    """The JD monogram alone, transparent ground, as a data URI."""
    p = _mark_png(dark)
    data = base64.b64encode(p.read_bytes()).decode()
    return (
        f'<img src="data:image/png;base64,{data}" '
        f'style="width:{size}px;height:{size}px;object-fit:contain;display:block;" alt="JD Hub">'
    )


def logo_lockup(height: int = 56, dark: bool = True, show_rule: bool = True) -> str:
    """Mark + wordmark — the standard header on covers and banners."""
    mark = logo_mark(height, dark=dark)
    word_col = CREAM if dark else NAVY
    rule = (
        f'<span style="width:1px;height:{int(height*0.86)}px;'
        f'background:rgba(255,255,255,.26);display:block;"></span>'
        if show_rule and dark
        else ""
    )
    return f"""<div style="display:flex;align-items:center;gap:{int(height*0.34)}px;">
{mark}{rule}
<div style="display:flex;flex-direction:column;justify-content:center;">
  <div style="font-family:'Bricolage';font-weight:800;font-size:{int(height*0.40)}px;
    letter-spacing:-.03em;line-height:1;color:{word_col};white-space:nowrap;">
    JD Hub <span style="font-weight:500;opacity:.72;">Academy</span></div>
  <div style="font-family:'Code';font-size:{max(8,int(height*0.145))}px;
    letter-spacing:.30em;color:{GOLD};margin-top:{int(height*0.12)}px;">{TAGLINE}</div>
</div></div>"""


def render(html: str, out: Path, width: int, height: int, scale: float = 2.0) -> Path:
    """Render HTML to PNG with headless Chromium.

    Chromium is used because it reproduces real CSS gradients, blend modes,
    mask images and variable-font shaping — none of which a raster library
    matches at this quality.
    """
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(html, encoding="utf-8")
        cmd = [
            "chromium", "--headless=new", "--no-sandbox", "--disable-gpu",
            "--disable-dev-shm-usage", "--hide-scrollbars",
            "--default-background-color=00000000",
            f"--force-device-scale-factor={scale}",
            f"--window-size={width},{height}",
            f"--screenshot={out}",
            page.as_uri(),
        ]
        subprocess.run(cmd, capture_output=True, check=True, timeout=240)
    return out


def downscale(path: Path, target_width: int) -> None:
    from PIL import Image

    im = Image.open(path)
    if im.width > target_width:
        ratio = target_width / im.width
        im = im.convert("RGB").resize(
            (target_width, int(im.height * ratio)), Image.LANCZOS
        )
        im.save(path, optimize=True)
