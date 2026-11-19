"""Generate every cover, banner and illustration in the repository.

Run:  python scripts/build_assets.py [--only slug]

Outputs:
  assets/covers/<slug>.png          1080x1528 book cover
  assets/covers/<slug>-wide.png     1600x900  web / slide banner
  assets/illustrations/<slug>.png   1600x1200 interior figure
  assets/brand/logo-card.png        square logo card for social
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import art
from brand import (
    AUTHOR, AUTHOR_TITLE, CREAM, GOLD, GOLD_DEEP, ORG, RED, TAGLINE, YEAR,
    base_css, downscale, logo_lockup, logo_mark, render, ROOT, theme_for,
)
from catalogue import COURSES


def _esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _wrap(text: str, limit: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if len(trial) <= limit:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _fit_title(title: str, max_lines: int = 3) -> tuple[list[str], int]:
    """Pick the wrap width that fills the block without overflowing.

    The title column is 660px wide, so the character budget shrinks as the
    type grows. Try the widest setting first and step down until the title
    fits in `max_lines`.
    """
    for limit in range(15, 7, -1):
        lines = _wrap(title, limit)
        if len(lines) <= max_lines:
            break
    n = len(lines)
    size = {1: 104, 2: 90, 3: 76, 4: 64}.get(n, 58)
    return lines, size


# ---------------------------------------------------------------------------
# Book cover — 1080 x 1528. Print-safe, Instagram-safe, WhatsApp-preview-safe.
#
# Composition is a deliberate hierarchy:
#   top bar    brand rule, gold to red
#   header     logo lockup, course code, tier chip
#   title      the dominant element, three lines maximum
#   artwork    bleeds off the right edge, sits behind the title
#   spec strip three facts a buyer scans before reading
#   footer     author, imprint
# ---------------------------------------------------------------------------
def cover_html(course: dict) -> str:
    t = theme_for(course)
    acc, light, deep, mid = t["accent"], t["light"], t["deep"], t["mid"]
    g1, g2 = t["grad"]
    lines, size = _fit_title(course["title"])
    title_html = "<br>".join(_esc(l) for l in lines)

    tier = course.get("tier") or ""
    chip = (
        f'<span style="background:{acc};color:{deep};padding:8px 18px;border-radius:999px;'
        f'font-size:14px;font-weight:800;letter-spacing:.10em;text-transform:uppercase;'
        f'white-space:nowrap;">{_esc(tier)} Tier</span>'
        if tier
        else f'<span style="border:1.5px solid {acc}77;color:{acc};padding:8px 18px;'
        f'border-radius:999px;font-size:14px;font-weight:700;letter-spacing:.06em;'
        f'white-space:nowrap;">{_esc(t["label"])}</span>'
    )

    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1080px;height:1528px;overflow:hidden;
  background:
    radial-gradient(1100px 780px at 88% -6%, {acc}26 0%, transparent 62%),
    radial-gradient(900px 700px at -12% 104%, {g2}1f 0%, transparent 66%),
    linear-gradient(168deg, {deep} 0%, {mid} 58%, {deep} 100%);}}
/* --- brand rules ------------------------------------------------------- */
.bar-top{{position:absolute;left:0;right:0;top:0;height:9px;
  background:linear-gradient(90deg,{acc} 0%,{GOLD} 52%,{RED} 100%);z-index:6;}}
.bar-bot{{position:absolute;left:0;right:0;bottom:0;height:5px;
  background:linear-gradient(90deg,{RED} 0%,{GOLD} 48%,{acc} 100%);opacity:.9;z-index:6;}}
/* --- artwork: right panel, clear of the type column -------------------- */
.art{{position:absolute;right:-104px;top:414px;width:760px;opacity:.95;z-index:1;
  filter:drop-shadow(0 40px 90px {acc}3d);}}
.art svg{{width:100%;height:auto;}}
/* a soft column edge keeps type and art on separate planes */
.veil{{position:absolute;inset:0;z-index:2;pointer-events:none;
  background:linear-gradient(100deg,{deep}fa 0%,{deep}e0 44%,{deep}22 62%,transparent 72%);}}
/* --- content ----------------------------------------------------------- */
.wrap{{position:absolute;inset:0;z-index:4;padding:74px 82px 0;
  display:flex;flex-direction:column;}}
.head{{display:flex;justify-content:space-between;align-items:flex-start;}}
.code{{font-family:'Code';font-size:13px;letter-spacing:.22em;color:{GOLD};
  text-align:right;line-height:1.9;opacity:.92;}}
.mid{{margin-top:auto;margin-bottom:auto;padding-top:34px;width:660px;}}
.rule{{width:76px;height:4px;border-radius:2px;margin-bottom:26px;
  background:linear-gradient(90deg,{acc},{GOLD});}}
.title{{font-family:'Bricolage';font-weight:800;font-size:{size}px;line-height:.96;
  letter-spacing:-.035em;color:{CREAM};margin-bottom:26px;}}
.title em{{font-style:normal;
  background:linear-gradient(96deg,{light} 0%,{acc} 55%,{GOLD} 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent;}}
.sub{{font-family:'Serif';font-size:24px;line-height:1.46;color:#c3cbdd;
  max-width:640px;font-weight:400;}}
/* --- spec strip -------------------------------------------------------- */
.specs{{display:flex;gap:12px;margin-top:36px;width:660px;}}
.spec{{flex:1;border:1px solid rgba(255,255,255,.14);border-radius:13px;
  padding:15px 14px;background:rgba(255,255,255,.05);}}
.spec .k{{font-family:'Code';font-size:10.5px;letter-spacing:.17em;color:{acc};
  margin-bottom:8px;}}
.spec .v{{font-size:17px;font-weight:700;color:{CREAM};line-height:1.24;}}
/* --- footer ------------------------------------------------------------ */
.foot{{display:flex;justify-content:space-between;align-items:flex-end;
  padding:30px 0 58px;border-top:1px solid rgba(255,255,255,.10);margin-top:30px;}}
.author{{font-size:22px;font-weight:700;color:{CREAM};letter-spacing:-.01em;}}
.role{{font-family:'Code';font-size:12px;color:{GOLD};letter-spacing:.15em;margin-top:8px;}}
.meta{{text-align:right;font-family:'Code';font-size:11.5px;color:#8791a6;line-height:1.95;}}
</style></head><body><div class="page">
<div class="art">{art.art(course['slug'], 760, 570, g1, g2)}</div>
<div class="veil"></div><div class="noise"></div>
<div class="bar-top"></div><div class="bar-bot"></div>
<div class="wrap">
  <div class="head">
    {logo_lockup(58)}
    <div class="code">{_esc(course['code'])}<br>{YEAR}</div>
  </div>
  <div class="mid">
    <div style="margin-bottom:26px;">{chip}</div>
    <div class="rule"></div>
    <div class="title">{title_html}</div>
    <div class="sub">{_esc(course['subtitle'])}</div>
    <div class="specs">
      <div class="spec"><div class="k">LEVEL</div><div class="v">{_esc(course['level'].split('—')[0].strip())}</div></div>
      <div class="spec"><div class="k">DURATION</div><div class="v">{_esc(course['duration'].split('·')[0].strip())}</div></div>
      <div class="spec"><div class="k">FORMAT</div><div class="v">Facilitated</div></div>
    </div>
  </div>
  <div class="foot">
    <div>
      <div class="author">{AUTHOR}</div>
      <div class="role">{AUTHOR_TITLE.upper()}</div>
    </div>
    <div class="meta">{ORG.upper()}<br>KAMPALA · UGANDA</div>
  </div>
</div>
</div></body></html>"""


# ---------------------------------------------------------------------------
# Wide banner — 1600 x 900, for slides, web headers and WhatsApp previews.
# Left-weighted so text survives cropping in a link preview.
# ---------------------------------------------------------------------------
def wide_html(course: dict) -> str:
    t = theme_for(course)
    acc, deep, mid = t["accent"], t["deep"], t["mid"]
    g1, g2 = t["grad"]
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1600px;height:900px;overflow:hidden;
  background:
    radial-gradient(1000px 760px at 84% 12%, {acc}2e 0%, transparent 64%),
    linear-gradient(122deg,{deep} 0%,{mid} 62%,{deep} 100%);}}
.edge{{position:absolute;left:0;top:0;bottom:0;width:11px;
  background:linear-gradient(180deg,{acc},{GOLD},{RED});}}
.art{{position:absolute;right:-70px;top:50%;transform:translateY(-50%);
  width:720px;opacity:.9;filter:drop-shadow(0 30px 70px {acc}33);}}
.art svg{{width:100%;height:auto;}}
.veil{{position:absolute;inset:0;
  background:linear-gradient(96deg,{deep}f5 0%,{deep}b8 46%,transparent 72%);}}
.wrap{{position:relative;z-index:3;height:100%;padding:76px 88px;
  display:flex;flex-direction:column;justify-content:center;max-width:980px;}}
h1{{font-family:'Bricolage';font-weight:800;font-size:78px;line-height:.98;
  letter-spacing:-.035em;color:{CREAM};margin:30px 0 22px;text-wrap:balance;}}
p{{font-family:'Serif';font-size:27px;line-height:1.45;color:#c3cbdd;
  max-width:790px;}}
.by{{display:flex;align-items:center;gap:14px;margin-top:44px;font-size:19px;
  color:#8791a6;font-family:'Jakarta';}}
.by b{{color:{CREAM};font-weight:700;}}
.pill{{display:inline-flex;align-items:center;gap:10px;margin-top:26px;
  border:1px solid {acc}66;border-radius:999px;padding:9px 20px;
  font-family:'Code';font-size:13px;letter-spacing:.18em;color:{acc};}}
</style></head><body><div class="page">
<div class="art">{art.art(course['slug'], 720, 540, g1, g2)}</div>
<div class="veil"></div><div class="noise"></div><div class="edge"></div>
<div class="wrap">
  {logo_lockup(52)}
  <h1>{_esc(course['title'])}</h1>
  <p>{_esc(course['subtitle'])}</p>
  <div class="pill">{_esc(course['code'])} &nbsp;·&nbsp; {_esc(course['duration'].split('·')[0].strip())}</div>
  <div class="by"><b>{AUTHOR}</b> · {AUTHOR_TITLE}</div>
</div>
</div></body></html>"""


# ---------------------------------------------------------------------------
# Interior illustration — 1600 x 1200, the hero figure inside each book.
# ---------------------------------------------------------------------------
def illustration_html(course: dict) -> str:
    t = theme_for(course)
    acc, deep, mid = t["accent"], t["deep"], t["mid"]
    g1, g2 = t["grad"]
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1600px;height:1200px;overflow:hidden;
  background:
    radial-gradient(760px 760px at 50% 40%, {mid} 0%, {deep} 74%);
  display:grid;place-items:center;}}
.grid{{position:absolute;inset:0;opacity:.14;
  background-image:linear-gradient({acc}55 1px,transparent 1px),
                   linear-gradient(90deg,{acc}55 1px,transparent 1px);
  background-size:66px 66px;
  mask-image:radial-gradient(circle at 50% 46%,#000 26%,transparent 72%);
  -webkit-mask-image:radial-gradient(circle at 50% 46%,#000 26%,transparent 72%);}}
.ring{{position:absolute;width:880px;height:880px;border-radius:50%;
  border:1px solid {acc}33;}}
.ring2{{position:absolute;width:1160px;height:1160px;border-radius:50%;
  border:1px solid {GOLD}1c;}}
.art{{position:relative;z-index:3;width:800px;
  filter:drop-shadow(0 34px 80px {acc}4a);}}
.art svg{{width:100%;height:auto;}}
.cap{{position:absolute;left:0;right:0;bottom:76px;text-align:center;z-index:4;}}
.cap .t{{font-family:'Bricolage';font-weight:800;font-size:46px;color:{CREAM};
  letter-spacing:-.025em;}}
.cap .s{{font-family:'Code';font-size:14px;letter-spacing:.24em;color:{GOLD};
  margin-top:18px;}}
</style></head><body><div class="page">
<div class="grid"></div><div class="ring"></div><div class="ring2"></div>
<div class="noise"></div>
<div class="art">{art.art(course['slug'], 800, 600, g1, g2)}</div>
<div class="cap"><div class="t">{_esc(course['title'])}</div>
<div class="s">{ORG.upper()} &nbsp;·&nbsp; {_esc(course['code'])}</div></div>
</div></body></html>"""


def logo_card_html() -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1080px;height:1080px;overflow:hidden;
  background:radial-gradient(circle at 32% 24%,#122043 0%,#060b18 64%);
  display:grid;place-items:center;}}
.glow{{position:absolute;width:940px;height:940px;border-radius:50%;
  background:radial-gradient(circle,{GOLD}2b 0%,transparent 66%);}}
.inner{{position:relative;z-index:3;text-align:center;}}
.mark{{margin-bottom:46px;display:flex;justify-content:center;
  filter:drop-shadow(0 20px 46px rgba(0,0,0,.55));}}
.word{{font-family:'Bricolage';font-weight:800;font-size:86px;
  letter-spacing:-.038em;color:{CREAM};}}
.word span{{font-weight:500;opacity:.72;}}
.tag{{font-family:'Code';font-size:17px;letter-spacing:.36em;color:{GOLD};
  margin-top:26px;}}
.rule{{width:190px;height:4px;margin:42px auto 0;border-radius:2px;
  background:linear-gradient(90deg,{GOLD},{RED});}}
.sub{{font-family:'Serif';font-size:19px;color:#8791a6;margin-top:26px;
  letter-spacing:.02em;}}
</style></head><body><div class="page"><div class="glow"></div><div class="noise"></div>
<div class="inner">
  <div class="mark">{logo_mark(300)}</div>
  <div class="word">JD Hub <span>Academy</span></div>
  <div class="tag">{TAGLINE}</div>
  <div class="rule"></div>
  <div class="sub">A training initiative of JD Hub Tech · Kampala</div>
</div></div></body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="build a single course slug")
    args = ap.parse_args()

    todo = [c for c in COURSES if not args.only or c["slug"] == args.only]
    covers = ROOT / "assets" / "covers"
    illus = ROOT / "assets" / "illustrations"

    for c in todo:
        out = covers / f"{c['slug']}.png"
        render(cover_html(c), out, 1080, 1528, scale=1.6)
        downscale(out, 1080)
        print("cover       ", out.relative_to(ROOT))

        out = covers / f"{c['slug']}-wide.png"
        render(wide_html(c), out, 1600, 900, scale=1.4)
        downscale(out, 1600)
        print("banner      ", out.relative_to(ROOT))

        out = illus / f"{c['slug']}.png"
        render(illustration_html(c), out, 1600, 1200, scale=1.2)
        downscale(out, 1600)
        print("illustration", out.relative_to(ROOT))

    if not args.only:
        out = ROOT / "assets" / "brand" / "logo-card.png"
        render(logo_card_html(), out, 1080, 1080, scale=1.4)
        downscale(out, 1080)
        print("logo card   ", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
