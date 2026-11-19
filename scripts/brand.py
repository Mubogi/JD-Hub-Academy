"""JD Hub Academy brand system: palette, fonts, and HTML-to-PNG rendering.

Every visual asset in this repository is generated from this module so that the
whole library stays visually consistent. Change a value here, re-run
`python scripts/build_assets.py`, and every cover and illustration updates.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BRAND = ASSETS / "brand"
FONTS = BRAND / "fonts"

# --------------------------------------------------------------------------
# Palette — taken verbatim from the JD Hub production stylesheet
# (hub/static/hub/css/style.css, --jd-* custom properties).
# --------------------------------------------------------------------------
NAVY = "#060b18"
NAVY_2 = "#0b1730"
NAVY_3 = "#122043"
GOLD = "#e3a821"
GOLD_2 = "#ffd166"
GOLD_3 = "#b07c0f"
BLUE = "#1d4fd6"
BLUE_2 = "#4b7dff"
CYAN = "#2fd6cd"
RED = "#c8102e"
RED_2 = "#ef2b4a"
INK = "#14101f"
MUTED = "#6b6350"
CREAM = "#faf6ec"
WHITE = "#ffffff"

AUTHOR = "Mubogi Gastavas Jordan"
AUTHOR_TITLE = "President, JD Hub Tech"
ORG = "JD Hub Academy"
YEAR = "2026"

# Category accent colours. Each course family gets its own hue so that a
# learner can identify a course by colour before reading the title.
ACCENTS = {
    "ai": {"main": CYAN, "soft": "#0d3b45", "label": "Artificial Intelligence"},
    "software": {"main": BLUE_2, "soft": "#0f2454", "label": "Software & Productivity"},
    "stem": {"main": "#7ee787", "soft": "#0e3320", "label": "STEM & Making"},
    "financials": {"main": GOLD_2, "soft": "#3a2a06", "label": "Finance & Enterprise"},
    "design": {"main": "#c084fc", "soft": "#2b1145", "label": "Design & Media"},
}


def font_face_css() -> str:
    """@font-face rules pointing at the vendored variable fonts."""
    def face(family: str, filename: str, weight: str = "100 900") -> str:
        return (
            "@font-face{font-family:'%s';src:url('file://%s') format('truetype');"
            "font-weight:%s;font-display:block;}"
            % (family, (FONTS / filename).as_posix(), weight)
        )

    return "\n".join(
        [
            face("Bricolage", "BricolageGrotesque.ttf"),
            face("Jakarta", "PlusJakartaSans.ttf"),
            face("Mono", "JetBrainsMono.ttf"),
        ]
    )


def base_css() -> str:
    """Shared reset, type scale and utility classes for all rendered pages."""
    return f"""
{font_face_css()}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{-webkit-font-smoothing:antialiased;}}
body{{
  font-family:'Jakarta',sans-serif;color:{CREAM};background:{NAVY};
  width:100%;height:100%;overflow:hidden;
}}
.display{{font-family:'Bricolage',sans-serif;font-weight:800;letter-spacing:-.02em;line-height:.98;}}
.mono{{font-family:'Mono',monospace;letter-spacing:.14em;text-transform:uppercase;}}
.gold{{color:{GOLD_2};}}
.grad-gold{{
  background:linear-gradient(100deg,{GOLD_2} 0%,{GOLD} 45%,{GOLD_3} 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;
}}
.noise{{
  position:absolute;inset:0;opacity:.05;pointer-events:none;mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='140' height='140' filter='url(%23n)'/></svg>");
}}
"""


def logo_img(height: int = 46, light: bool = True) -> str:
    """Inline the JD Hub wordmark SVG at a given pixel height."""
    name = "logo-light.svg" if light else "logo.svg"
    svg = (BRAND / name).read_text(encoding="utf-8")
    # viewBox is 380x64; force an explicit height and keep aspect ratio.
    svg = svg.replace('width="380" height="64"', f'height="{height}" width="{int(height * 380 / 64)}"')
    return svg


def logo_mark_img(size: int = 96) -> str:
    """Inline the transparent JD monogram mark as a data URI."""
    import base64

    data = base64.b64encode((BRAND / "logo-mark.png").read_bytes()).decode()
    return (
        f'<img src="data:image/png;base64,{data}" '
        f'style="width:{size}px;height:{size}px;object-fit:contain;" alt="JD Hub">'
    )


def render(html: str, out: Path, width: int, height: int, scale: float = 2.0) -> Path:
    """Render an HTML string to a PNG using headless Chromium.

    Chromium is the renderer because it gives us real CSS gradients, blend
    modes and font shaping — none of which a raster library reproduces
    faithfully at this quality.
    """
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "page.html"
        page.write_text(html, encoding="utf-8")
        cmd = [
            "chromium",
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--hide-scrollbars",
            "--default-background-color=00000000",
            f"--force-device-scale-factor={scale}",
            f"--window-size={width},{height}",
            f"--screenshot={out}",
            page.as_uri(),
        ]
        subprocess.run(cmd, capture_output=True, check=True, timeout=180)
    return out


def downscale(path: Path, target_width: int) -> None:
    """Chromium renders at `scale`; shrink to the intended pixel size."""
    from PIL import Image

    im = Image.open(path)
    if im.width > target_width:
        ratio = target_width / im.width
        im = im.convert("RGB").resize(
            (target_width, int(im.height * ratio)), Image.LANCZOS
        )
        im.save(path, optimize=True)
