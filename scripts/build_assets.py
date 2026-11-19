"""Generate every cover and illustration in the repository.

Run:  python scripts/build_assets.py [--only slug]

Outputs:
  assets/covers/<slug>.png          1080x1528 book cover
  assets/covers/<slug>-wide.png     1600x900  web / slide banner
  assets/illustrations/<slug>.png   1600x1200 concept figure for the book
  assets/brand/logo-card.png        square logo card for social
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import art
from brand import (
    ACCENTS, AUTHOR, AUTHOR_TITLE, BLUE, CREAM, CYAN, GOLD, GOLD_2, GOLD_3,
    NAVY, NAVY_2, NAVY_3, ORG, RED, WHITE, YEAR, base_css, downscale,
    logo_img, logo_mark_img, render, ROOT,
)
from catalogue import COURSES


def _accent(course: dict) -> dict:
    return ACCENTS.get(course["category"], ACCENTS["software"])


def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )


def _wrap(text: str, limit: int) -> list[str]:
    """Greedy word wrap for cover titles."""
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


# ---------------------------------------------------------------------------
# Book cover — 1080 x 1528 (A5-ish ratio, prints well and posts well)
# ---------------------------------------------------------------------------
def cover_html(course: dict) -> str:
    acc = _accent(course)
    main, soft = acc["main"], acc["soft"]
    title_lines = _wrap(course["title"], 17)
    # Shrink the type as the title gets longer so it always fits the block.
    n = len(title_lines)
    size = {1: 104, 2: 92, 3: 78, 4: 66}.get(n, 60)
    title_html = "<br>".join(_esc(l) for l in title_lines)

    tier_badge = (
        f'<span style="background:{main};color:{NAVY};padding:7px 16px;border-radius:999px;'
        f'font-size:15px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;">'
        f'{_esc(course["tier"])} TIER</span>'
        if course["tier"]
        else f'<span style="border:1.5px solid {main};color:{main};padding:7px 16px;border-radius:999px;'
        f'font-size:15px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;">'
        f'{_esc(acc["label"])}</span>'
    )

    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1080px;height:1528px;background:{NAVY};overflow:hidden;}}
.glow-a{{position:absolute;width:900px;height:900px;border-radius:50%;
  background:radial-gradient(circle,{main}33 0%,transparent 68%);top:-330px;right:-300px;}}
.glow-b{{position:absolute;width:800px;height:800px;border-radius:50%;
  background:radial-gradient(circle,{GOLD}22 0%,transparent 70%);bottom:-380px;left:-320px;}}
.rule{{position:absolute;left:0;right:0;height:10px;
  background:linear-gradient(90deg,{main},{GOLD},{RED});}}
.frame{{position:absolute;inset:38px;border:1px solid rgba(255,255,255,.12);border-radius:22px;}}
.content{{position:relative;z-index:3;padding:92px 84px 0;display:flex;flex-direction:column;height:100%;}}
.eyebrow{{display:flex;align-items:center;gap:14px;margin-bottom:44px;}}
.pill{{font-family:'Mono';font-size:14px;letter-spacing:.2em;color:{GOLD_2};
  border:1px solid rgba(255,209,102,.4);padding:7px 14px;border-radius:8px;}}
.title{{font-family:'Bricolage';font-weight:800;font-size:{size}px;line-height:.97;
  letter-spacing:-.03em;color:{CREAM};margin-bottom:26px;}}
.sub{{font-size:26px;line-height:1.42;color:#b9c2d6;max-width:830px;font-weight:500;}}
.specs{{position:absolute;left:84px;right:84px;top:640px;display:flex;gap:14px;z-index:4;}}
.spec{{flex:1;border:1px solid rgba(255,255,255,.13);border-radius:14px;
  padding:18px 16px;background:rgba(255,255,255,.035);}}
.spec .k{{font-family:'Mono';font-size:11.5px;letter-spacing:.16em;color:{main};margin-bottom:9px;}}
.spec .v{{font-size:19px;font-weight:700;color:{CREAM};line-height:1.25;}}
.artbox{{position:absolute;right:-56px;bottom:196px;width:700px;opacity:.96;}}
.artbox svg{{width:100%;height:auto;}}
.footer{{position:absolute;left:84px;right:84px;bottom:66px;display:flex;
  justify-content:space-between;align-items:flex-end;z-index:4;}}
.author{{font-size:23px;font-weight:700;color:{CREAM};}}
.role{{font-family:'Mono';font-size:13.5px;color:{GOLD_2};letter-spacing:.13em;margin-top:7px;}}
.meta{{text-align:right;font-family:'Mono';font-size:13px;color:#8b96ad;line-height:1.9;}}
</style></head><body><div class="page">
  <div class="glow-a"></div><div class="glow-b"></div><div class="noise"></div>
  <div class="rule" style="top:0"></div>
  <div class="rule" style="bottom:0;height:6px;opacity:.85"></div>
  <div class="frame"></div>
  <div class="content">
    <div class="eyebrow">{logo_img(44)}</div>
    <div style="margin-bottom:26px">{tier_badge}</div>
    <div class="title">{title_html}</div>
    <div class="sub">{_esc(course["subtitle"])}</div>
  </div>
  <div class="specs">
    <div class="spec"><div class="k">LEVEL</div><div class="v">{_esc(course["level"].split("—")[0].strip())}</div></div>
    <div class="spec"><div class="k">DURATION</div><div class="v">{_esc(course["duration"].split("·")[0].strip())}</div></div>
    <div class="spec"><div class="k">CODE</div><div class="v">{_esc(course["code"])}</div></div>
  </div>
  <div class="artbox">{art.art(course["slug"], 700, 525, main, GOLD)}</div>
  <div class="footer">
    <div>
      <div class="author">{AUTHOR}</div>
      <div class="role">{AUTHOR_TITLE.upper()}</div>
    </div>
    <div class="meta">
      {ORG.upper()}<br>{_esc(course["code"])} &nbsp;·&nbsp; {YEAR}
    </div>
  </div>
</div></body></html>"""


# ---------------------------------------------------------------------------
# Wide banner — 1600 x 900, for slides, web headers and WhatsApp previews
# ---------------------------------------------------------------------------
def wide_html(course: dict) -> str:
    acc = _accent(course)
    main, soft = acc["main"], acc["soft"]
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1600px;height:900px;background:linear-gradient(120deg,{NAVY} 0%,{NAVY_2} 55%,{soft} 100%);overflow:hidden;}}
.glow{{position:absolute;width:1100px;height:1100px;border-radius:50%;
  background:radial-gradient(circle,{main}2e 0%,transparent 66%);top:-420px;right:-300px;}}
.wrap{{position:relative;z-index:3;padding:86px 92px;display:flex;height:100%;align-items:center;gap:60px;}}
.left{{flex:1;max-width:840px;}}
.right{{width:520px;flex:none;}}
.right svg{{width:100%;height:auto;}}
h1{{font-family:'Bricolage';font-weight:800;font-size:72px;line-height:1.0;letter-spacing:-.03em;color:{CREAM};margin:26px 0 22px;}}
p{{font-size:25px;line-height:1.45;color:#b9c2d6;max-width:760px;}}
.bar{{position:absolute;left:0;top:0;bottom:0;width:12px;background:linear-gradient(180deg,{main},{GOLD},{RED});}}
.byline{{display:flex;align-items:center;gap:16px;margin-top:44px;font-size:19px;color:#8b96ad;}}
.byline b{{color:{CREAM};font-weight:700;}}
</style></head><body><div class="page"><div class="glow"></div><div class="noise"></div><div class="bar"></div>
<div class="wrap"><div class="left">
  {logo_img(40)}
  <h1>{_esc(course["title"])}</h1>
  <p>{_esc(course["subtitle"])}</p>
  <div class="byline"><b>{AUTHOR}</b> · {AUTHOR_TITLE} · {ORG}</div>
</div><div class="right">{art.art(course["slug"], 520, 390, main, GOLD)}</div></div>
</div></body></html>"""


# ---------------------------------------------------------------------------
# Concept illustration — 1600 x 1200, the hero figure inside each book
# ---------------------------------------------------------------------------
def illustration_html(course: dict) -> str:
    acc = _accent(course)
    main, soft = acc["main"], acc["soft"]
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1600px;height:1200px;
  background:radial-gradient(circle at 50% 42%,{soft} 0%,{NAVY} 72%);overflow:hidden;
  display:grid;place-items:center;}}
.grid{{position:absolute;inset:0;opacity:.16;
  background-image:linear-gradient({main}44 1px,transparent 1px),linear-gradient(90deg,{main}44 1px,transparent 1px);
  background-size:64px 64px;
  mask-image:radial-gradient(circle at 50% 50%,#000 30%,transparent 74%);
  -webkit-mask-image:radial-gradient(circle at 50% 50%,#000 30%,transparent 74%);}}
.ring{{position:absolute;width:820px;height:820px;border-radius:50%;
  border:1px solid {main}30;}}
.ring2{{position:absolute;width:1080px;height:1080px;border-radius:50%;border:1px solid {GOLD}18;}}
.art{{position:relative;z-index:3;width:760px;}}
.art svg{{width:100%;height:auto;filter:drop-shadow(0 26px 60px {main}44);}}
.cap{{position:absolute;left:0;right:0;bottom:70px;text-align:center;z-index:4;}}
.cap .t{{font-family:'Bricolage';font-weight:800;font-size:44px;color:{CREAM};letter-spacing:-.02em;}}
.cap .s{{font-family:'Mono';font-size:15px;letter-spacing:.22em;color:{GOLD_2};margin-top:16px;}}
</style></head><body><div class="page">
<div class="grid"></div><div class="ring"></div><div class="ring2"></div><div class="noise"></div>
<div class="art">{art.art(course["slug"], 760, 570, main, GOLD)}</div>
<div class="cap"><div class="t">{_esc(course["title"])}</div>
<div class="s">{ORG.upper()} &nbsp;·&nbsp; {_esc(course["code"])}</div></div>
</div></body></html>"""


def logo_card_html() -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
{base_css()}
.page{{position:relative;width:1080px;height:1080px;background:
  radial-gradient(circle at 30% 25%,{NAVY_3} 0%,{NAVY} 62%);display:grid;place-items:center;overflow:hidden;}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;
  background:radial-gradient(circle,{GOLD}26 0%,transparent 68%);}}
.inner{{position:relative;z-index:3;text-align:center;}}
.mark{{margin-bottom:44px;filter:drop-shadow(0 18px 40px rgba(0,0,0,.5));}}
.word{{font-family:'Bricolage';font-weight:800;font-size:88px;letter-spacing:-.035em;color:{CREAM};}}
.word span{{color:{BLUE}}}
.tag{{font-family:'Mono';font-size:19px;letter-spacing:.34em;color:{GOLD_2};margin-top:26px;}}
.rule{{width:180px;height:4px;margin:40px auto 0;border-radius:2px;
  background:linear-gradient(90deg,{GOLD_2},{GOLD},{RED});}}
</style></head><body><div class="page"><div class="glow"></div><div class="noise"></div>
<div class="inner"><div class="mark">{logo_mark_img(300)}</div>
<div class="word">JD Hub <span>Academy</span></div>
<div class="tag">LEARN · BUILD · EARN</div>
<div class="rule"></div></div></div></body></html>"""


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
