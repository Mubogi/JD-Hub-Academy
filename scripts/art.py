"""Original vector artwork for JD Hub Academy.

Every illustration here is drawn from scratch in SVG — no stock art, no
licensing questions. Each scene is built in four layers so it reads as an
illustration rather than a diagram:

    haze       soft radial glow, sets the mood and depth
    structure  thin geometry, gives the eye a grid to rest on
    mass       the solid forms — cards, slabs, panels
    accent     gradient-lit elements carrying the course colour
    spark      small bright details

The scene is tinted at render time from the course theme, so the same drawing
serves a cyan AI book and a green Excel book without a second file.
"""

from __future__ import annotations

_S = 'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" fill="none"'


# ---------------------------------------------------------------------------
# 48x48 line glyphs, used in tables and small UI spots.
# ---------------------------------------------------------------------------
ICONS: dict[str, str] = {
    "spark": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M24 6l4.2 10.4L38.6 20 28.2 24.2 24 34.6 19.8 24.2 9.4 20l10.4-3.6z"/>
        <path d="M37 32l1.8 4.4L43 38l-4.2 1.6L37 44l-1.8-4.4L31 38l4.2-1.6z"/>
        <path d="M10 32l1.4 3.4L14.8 37l-3.4 1.4L10 42l-1.4-3.6L5.2 37l3.4-1.6z"/>
    </g></svg>""",
    "shield": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M24 6l14 5v11c0 9-6 16-14 20-8-4-14-11-14-20V11z"/>
        <path d="M18 24l4.5 4.5L31 20"/>
    </g></svg>""",
    "check": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <circle cx="24" cy="24" r="17"/><path d="M16 24l6 6 11-12"/>
    </g></svg>""",
}

_FALLBACK = ICONS["spark"]


def icon(name: str, size: int = 40, color: str = "currentColor", extra: str = "") -> str:
    """Return a line icon sized and coloured."""
    svg = ICONS.get(name, _FALLBACK)
    return svg.replace(
        "<svg ",
        f'<svg width="{size}" height="{size}" style="color:{color};{extra}" ',
        1,
    )


# ---------------------------------------------------------------------------
# Shared gradient and filter definitions.
# ---------------------------------------------------------------------------
_DEFS = """
<defs>
  <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%(a)s"/>
    <stop offset="1" stop-color="%(b)s"/>
  </linearGradient>
  <linearGradient id="gsoft" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%(a)s" stop-opacity=".55"/>
    <stop offset="1" stop-color="%(b)s" stop-opacity=".08"/>
  </linearGradient>
  <radialGradient id="ghaze">
    <stop offset="0" stop-color="%(a)s" stop-opacity=".38"/>
    <stop offset=".55" stop-color="%(a)s" stop-opacity=".10"/>
    <stop offset="1" stop-color="%(a)s" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="ghaze2">
    <stop offset="0" stop-color="%(b)s" stop-opacity=".30"/>
    <stop offset="1" stop-color="%(b)s" stop-opacity="0"/>
  </radialGradient>
  <filter id="blur8" x="-50%%" y="-50%%" width="200%%" height="200%%">
    <feGaussianBlur stdDeviation="8"/>
  </filter>
</defs>
"""


def _haze() -> str:
    """Background mood layer — shared by every scene."""
    return (
        '<circle cx="200" cy="150" r="170" fill="url(#ghaze)"/>'
        '<circle cx="280" cy="210" r="122" fill="url(#ghaze2)"/>'
    )


def _grid() -> str:
    """A faint dotted field — the studio floor."""
    dots = "".join(
        f'<circle cx="{x}" cy="{y}" r="1.1"/>'
        for y in range(40, 290, 26)
        for x in range(30, 390, 26)
    )
    return f'<g fill="url(#g1)" opacity=".13" filter="url(#blur8)">{dots}</g>'


# ---------------------------------------------------------------------------
# The scenes. 400x300 each; {haze} and {grid} are substituted at render.
# ---------------------------------------------------------------------------
ART: dict[str, str] = {

    # =======================================================================
    # THE AI LADDER — cyan steps to violet as the learner climbs
    # =======================================================================
    "ai-foundation": """
  <g>
    {haze}{grid}
    <g fill="none" stroke="url(#g1)" opacity=".30">
      <ellipse cx="200" cy="150" rx="150" ry="58" stroke-width="1.1"/>
      <ellipse cx="200" cy="150" rx="150" ry="58" stroke-width="1.1" transform="rotate(60 200 150)"/>
      <ellipse cx="200" cy="150" rx="150" ry="58" stroke-width="1.1" transform="rotate(120 200 150)"/>
    </g>
    <circle cx="200" cy="150" r="62" fill="url(#gsoft)" opacity=".5"/>
    <circle cx="200" cy="150" r="46" fill="url(#g1)" opacity=".92"/>
    <circle cx="200" cy="150" r="46" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="1.2"/>
    <circle cx="186" cy="136" r="17" fill="#fff" opacity=".22"/>
    <g fill="url(#g1)">
      <circle cx="350" cy="150" r="9"/><circle cx="50" cy="150" r="9"/>
      <circle cx="275" cy="88" r="7"/><circle cx="125" cy="212" r="7"/>
      <circle cx="275" cy="212" r="7"/><circle cx="125" cy="88" r="7"/>
    </g>
    <g fill="#fff" opacity=".85">
      <circle cx="350" cy="150" r="3.4"/><circle cx="50" cy="150" r="3.4"/>
      <circle cx="275" cy="88" r="2.6"/><circle cx="125" cy="212" r="2.6"/>
      <circle cx="275" cy="212" r="2.6"/><circle cx="125" cy="88" r="2.6"/>
    </g>
    <g stroke="#fff" stroke-opacity=".55" stroke-width="1.4" stroke-linecap="round">
      <path d="M200 92v-14M200 208v14M142 150h-14M258 150h14"/>
    </g>
  </g>""",

    "ai-practitioner": """
  <g>
    {haze}{grid}
    <g fill="none" stroke="url(#g1)" stroke-width="1.6" opacity=".45" stroke-linecap="round">
      <path d="M92 150h44M264 150h44M200 96v-28M200 204v28"/>
      <path d="M126 116l24 24M274 116l-24 24M126 184l24-24M274 184l-24-24"/>
    </g>
    <rect x="152" y="104" width="96" height="92" rx="16" fill="url(#gsoft)"/>
    <rect x="152" y="104" width="96" height="92" rx="16" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
    <g fill="url(#g1)">
      <rect x="168" y="122" width="52" height="7" rx="3.5"/>
      <rect x="168" y="138" width="64" height="7" rx="3.5" opacity=".7"/>
      <rect x="168" y="154" width="38" height="7" rx="3.5" opacity=".45"/>
    </g>
    <circle cx="216" cy="176" r="5" fill="#fff" opacity=".9"/>
    <g fill="url(#g1)">
      <circle cx="70" cy="150" r="15"/><circle cx="330" cy="150" r="15"/>
      <circle cx="200" cy="52" r="12"/><circle cx="200" cy="248" r="12"/>
    </g>
    <g fill="#fff" opacity=".8">
      <circle cx="70" cy="150" r="5"/><circle cx="330" cy="150" r="5"/>
      <circle cx="200" cy="52" r="4"/><circle cx="200" cy="248" r="4"/>
    </g>
  </g>""",

    "ai-builder": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width="1" opacity=".28" fill="none">
      <path d="M60 236h280M60 236V96M340 236V96M60 96h280"/>
    </g>
    <rect x="86" y="168" width="88" height="56" rx="10" fill="url(#gsoft)"/>
    <rect x="86" y="168" width="88" height="56" rx="10" fill="none" stroke="url(#g1)" stroke-width="1.5"/>
    <rect x="186" y="128" width="88" height="96" rx="10" fill="url(#g1)" opacity=".85"/>
    <rect x="286" y="152" width="70" height="72" rx="10" fill="url(#gsoft)"/>
    <rect x="286" y="152" width="70" height="72" rx="10" fill="none" stroke="url(#g1)" stroke-width="1.5"/>
    <g stroke="url(#g1)" stroke-width="1.4" opacity=".6" fill="none">
      <path d="M174 196h12M274 176h12"/>
    </g>
    <g fill="#fff" opacity=".9">
      <circle cx="130" cy="196" r="4"/><circle cx="230" cy="176" r="5"/><circle cx="321" cy="188" r="4"/>
    </g>
    <path d="M230 176l16 6-6 2.5-2.5 6z" fill="#fff" opacity=".95"/>
  </g>""",

    "ai-specialist": """
  <g>
    {haze}{grid}
    <circle cx="200" cy="150" r="112" fill="none" stroke="url(#g1)" stroke-width="1" opacity=".35" stroke-dasharray="4 7"/>
    <circle cx="200" cy="150" r="88" fill="none" stroke="url(#g1)" stroke-width="1" opacity=".22"/>
    <path d="M200 58l68 24v54c0 46-30 78-68 96-38-18-68-50-68-96V82z" fill="url(#gsoft)"/>
    <path d="M200 58l68 24v54c0 46-30 78-68 96-38-18-68-50-68-96V82z" fill="none" stroke="url(#g1)" stroke-width="2"/>
    <path d="M170 148l22 22 44-46" fill="none" stroke="url(#g1)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M170 148l22 22 44-46" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="2" stroke-linecap="round"/>
    <g stroke="url(#g1)" stroke-width="1.6" opacity=".6" stroke-linecap="round">
      <path d="M96 108l-12-8M92 140l-14-4M96 172l-13 4"/>
      <path d="M304 108l12-8M308 140l14-4M304 172l13 4"/>
    </g>
  </g>""",

    # =======================================================================
    # STEM & FOUNDATIONS
    # =======================================================================
    "scratch-coding": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width=".8" opacity=".18">
      <path d="M40 90h320M40 150h320M40 210h320"/>
      <path d="M110 50v200M200 50v200M290 50v200"/>
    </g>
    <rect x="70" y="86" width="118" height="44" rx="12" fill="url(#g1)" opacity=".9"/>
    <rect x="146" y="152" width="130" height="44" rx="12" fill="url(#gsoft)"/>
    <rect x="146" y="152" width="130" height="44" rx="12" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
    <rect x="96" y="212" width="104" height="44" rx="12" fill="url(#g1)" opacity=".5"/>
    <g fill="#fff" opacity=".55">
      <rect x="90" y="102" width="34" height="5" rx="2.5"/>
      <rect x="166" y="168" width="46" height="5" rx="2.5"/>
      <rect x="116" y="228" width="30" height="5" rx="2.5"/>
    </g>
    <rect x="272" y="120" width="76" height="76" rx="14" fill="url(#gsoft)"/>
    <rect x="272" y="120" width="76" height="76" rx="14" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
    <path d="M302 146l30 16-30 16z" fill="url(#g1)"/>
  </g>""",

    "practical-stem": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width="1.2" opacity=".35" stroke-linecap="round">
      <path d="M56 250h288"/>
      <path d="M76 250v-10M116 250v-16M156 250v-10M196 250v-20M236 250v-10M276 250v-16M316 250v-10"/>
    </g>
    <path d="M186 62h28v44l46 92a22 22 0 01-19.6 32H159.6A22 22 0 01140 198l46-92z" fill="url(#gsoft)"/>
    <path d="M186 62h28v44l46 92a22 22 0 01-19.6 32H159.6A22 22 0 01140 198l46-92z" fill="none" stroke="url(#g1)" stroke-width="2"/>
    <path d="M158 176h84l16 32a16 16 0 01-14 20H156a16 16 0 01-14-20z" fill="url(#g1)" opacity=".85"/>
    <path d="M158 176h84" stroke="#fff" stroke-opacity=".5" stroke-width="1.6"/>
    <g fill="#fff" opacity=".8">
      <circle cx="182" cy="200" r="4"/><circle cx="204" cy="216" r="3"/><circle cx="222" cy="198" r="3.4"/>
    </g>
    <g transform="translate(300 92)">
      <circle r="26" fill="none" stroke="url(#g1)" stroke-width="2" opacity=".7"/>
      <g stroke="url(#g1)" stroke-width="2" opacity=".7" stroke-linecap="round">
        <path d="M0 -34v8M0 26v8M-34 0h8M26 0h8M-24 -24l6 6M18 18l6 6M-24 24l6-6M18 -18l6-6"/>
      </g>
      <circle r="9" fill="url(#g1)" opacity=".8"/>
    </g>
  </g>""",

    "digital-literacy": """
  <g>
    {haze}{grid}
    <rect x="62" y="72" width="276" height="176" rx="14" fill="url(#gsoft)"/>
    <rect x="62" y="72" width="276" height="176" rx="14" fill="none" stroke="url(#g1)" stroke-width="1.7"/>
    <rect x="62" y="72" width="276" height="32" rx="14" fill="url(#g1)" opacity=".55"/>
    <g fill="#fff" opacity=".85">
      <circle cx="82" cy="88" r="4.4"/><circle cx="97" cy="88" r="4.4"/><circle cx="112" cy="88" r="4.4"/>
    </g>
    <g fill="url(#g1)" opacity=".55">
      <rect x="86" y="126" width="96" height="8" rx="4"/>
      <rect x="86" y="146" width="140" height="8" rx="4" opacity=".6"/>
      <rect x="86" y="166" width="118" height="8" rx="4" opacity=".4"/>
    </g>
    <rect x="240" y="120" width="76" height="76" rx="10" fill="url(#g1)" opacity=".75"/>
    <g fill="#fff" opacity=".9">
      <rect x="254" y="136" width="48" height="5" rx="2.5"/>
      <rect x="254" y="150" width="34" height="5" rx="2.5" opacity=".7"/>
    </g>
    <path d="M246 186l14 5-5.5 2-2 5.5z" fill="#fff" opacity=".95"/>
  </g>""",

    # =======================================================================
    # DESIGN & MEDIA
    # =======================================================================
    "graphic-design": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width="1" opacity=".22" fill="none">
      <rect x="72" y="60" width="256" height="180"/>
      <path d="M72 150h256M200 60v180"/>
      <circle cx="200" cy="150" r="90"/>
    </g>
    <rect x="86" y="92" width="96" height="96" rx="8" fill="url(#g1)" opacity=".95"/>
    <rect x="140" y="118" width="96" height="96" rx="8" fill="url(#g1)" opacity=".55"/>
    <rect x="194" y="144" width="96" height="96" rx="8" fill="url(#g1)" opacity=".28"/>
    <path d="M96 240C150 190 250 250 320 170" fill="none" stroke="url(#g1)" stroke-width="2.6" stroke-linecap="round"/>
    <g fill="#fff" opacity=".95">
      <circle cx="96" cy="240" r="4.5"/><circle cx="320" cy="170" r="4.5"/>
    </g>
    <g stroke="#fff" stroke-opacity=".5" stroke-width="1" stroke-dasharray="3 3">
      <path d="M96 240l30-14M320 170l-30 14"/>
    </g>
    <circle cx="126" cy="226" r="3" fill="#fff" opacity=".8"/>
    <circle cx="290" cy="184" r="3" fill="#fff" opacity=".8"/>
  </g>""",

    "content-creation": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width="1" opacity=".3" fill="none">
      <path d="M48 96h304M48 204h304"/>
    </g>
    <rect x="150" y="52" width="100" height="196" rx="20" fill="url(#gsoft)"/>
    <rect x="150" y="52" width="100" height="196" rx="20" fill="none" stroke="url(#g1)" stroke-width="1.8"/>
    <rect x="164" y="78" width="72" height="72" rx="8" fill="url(#g1)" opacity=".85"/>
    <g fill="url(#g1)" opacity=".6">
      <rect x="164" y="162" width="72" height="7" rx="3.5"/>
      <rect x="164" y="178" width="52" height="7" rx="3.5" opacity=".7"/>
      <rect x="164" y="194" width="62" height="7" rx="3.5" opacity=".45"/>
    </g>
    <path d="M190 104l22 10-22 10z" fill="#fff" opacity=".95"/>
    <g fill="url(#g1)" opacity=".7">
      <circle cx="92" cy="150" r="18"/><circle cx="308" cy="150" r="18"/>
    </g>
    <g fill="#fff" opacity=".85">
      <circle cx="92" cy="150" r="6"/><circle cx="308" cy="150" r="6"/>
    </g>
    <g stroke="url(#g1)" stroke-width="1.2" opacity=".4" stroke-linecap="round">
      <path d="M110 150h34M256 150h34"/>
    </g>
  </g>""",

    # =======================================================================
    # MONEY
    # =======================================================================
    "financial-sacco": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width="1" opacity=".25">
      <path d="M62 236h276M62 196h276M62 156h276M62 116h276M62 76h276"/>
    </g>
    <g>
      <rect x="86" y="176" width="42" height="60" rx="6" fill="url(#g1)" opacity=".35"/>
      <rect x="144" y="148" width="42" height="88" rx="6" fill="url(#g1)" opacity=".55"/>
      <rect x="202" y="112" width="42" height="124" rx="6" fill="url(#g1)" opacity=".78"/>
      <rect x="260" y="76" width="42" height="160" rx="6" fill="url(#g1)"/>
    </g>
    <path d="M107 170L165 142L223 106L281 70" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    <g fill="#fff">
      <circle cx="107" cy="170" r="4"/><circle cx="165" cy="142" r="4"/>
      <circle cx="223" cy="106" r="4"/><circle cx="281" cy="70" r="4"/>
    </g>
    <g transform="translate(316 210)">
      <circle r="26" fill="url(#g1)"/>
      <circle r="26" fill="none" stroke="#fff" stroke-opacity=".45" stroke-width="1.4"/>
      <path d="M0 -13v26M-7 -5h11a6 6 0 010 12h-8" fill="none" stroke="#fff" stroke-opacity=".9" stroke-width="2.4" stroke-linecap="round"/>
    </g>
  </g>""",

    "business-growth": """
  <g>
    {haze}{grid}
    <circle cx="200" cy="150" r="104" fill="none" stroke="url(#g1)" stroke-width="1" opacity=".28" stroke-dasharray="3 6"/>
    <path d="M200 58c26 22 38 56 38 92 0 20-4 38-10 52h-56c-6-14-10-32-10-52 0-36 12-70 38-92z" fill="url(#gsoft)"/>
    <path d="M200 58c26 22 38 56 38 92 0 20-4 38-10 52h-56c-6-14-10-32-10-52 0-36 12-70 38-92z" fill="none" stroke="url(#g1)" stroke-width="1.8"/>
    <circle cx="200" cy="132" r="18" fill="url(#g1)"/>
    <circle cx="200" cy="132" r="18" fill="none" stroke="#fff" stroke-opacity=".4" stroke-width="1.2"/>
    <path d="M172 168l-24 40 30-12zM228 168l24 40-30-12z" fill="url(#g1)" opacity=".8"/>
    <path d="M188 202h24c0 22-6 34-12 44-6-10-12-22-12-44z" fill="url(#g1)" opacity=".9"/>
    <path d="M192 202h16c0 16-4 24-8 32-4-8-8-16-8-32z" fill="#fff" opacity=".8"/>
    <g stroke="url(#g1)" stroke-width="1.6" opacity=".5" stroke-linecap="round">
      <path d="M110 110h-26M120 76h-18M96 150h-22"/>
    </g>
  </g>""",

    # =======================================================================
    # MARKETING
    # =======================================================================
    "digital-marketing": """
  <g>
    {haze}{grid}
    <g fill="none" stroke="url(#g1)">
      <circle cx="150" cy="160" r="34" stroke-width="1.6" opacity=".8"/>
      <circle cx="150" cy="160" r="62" stroke-width="1.3" opacity=".5"/>
      <circle cx="150" cy="160" r="92" stroke-width="1" opacity=".3"/>
      <circle cx="150" cy="160" r="122" stroke-width=".9" opacity=".16"/>
    </g>
    <g transform="translate(232 148) rotate(-18)">
      <path d="M0 -26l64 -22v96l-64 -22z" fill="url(#g1)" opacity=".9"/>
      <rect x="-20" y="-20" width="22" height="40" rx="8" fill="url(#g1)"/>
      <path d="M64 -48a34 34 0 010 96" fill="none" stroke="url(#g1)" stroke-width="3" opacity=".55"/>
    </g>
    <g fill="url(#g1)">
      <circle cx="118" cy="120" r="6"/><circle cx="182" cy="120" r="6"/>
      <circle cx="106" cy="176" r="6"/><circle cx="194" cy="176" r="6"/>
      <circle cx="150" cy="204" r="6"/><circle cx="150" cy="112" r="7"/>
    </g>
    <circle cx="150" cy="112" r="2.8" fill="#fff" opacity=".9"/>
    <path d="M300 84c-8-10-24-6-24 6 0 10 12 18 24 26 12-8 24-16 24-26 0-12-16-16-24-6z" fill="url(#g1)" opacity=".75"/>
  </g>""",

    # =======================================================================
    # LEADERSHIP — the flagship
    # =======================================================================
    "leadership": """
  <g>
    {haze}{grid}
    <g stroke="url(#g1)" stroke-width="1" opacity=".22" stroke-linecap="round">
      <path d="M200 150L200 20M200 150L310 50M200 150L360 150M200 150L310 250M200 150L200 280M200 150L90 250M200 150L40 150M200 150L90 50"/>
    </g>
    <path d="M60 244L200 84l140 160z" fill="url(#gsoft)"/>
    <path d="M60 244L200 84l140 160z" fill="none" stroke="url(#g1)" stroke-width="1.6" opacity=".7"/>
    <path d="M200 84l56 64-56 22-56-22z" fill="url(#g1)" opacity=".9"/>
    <path d="M200 84V28" stroke="url(#g1)" stroke-width="3" stroke-linecap="round"/>
    <path d="M200 30l44 14-44 14z" fill="url(#g1)"/>
    <g fill="#fff" opacity=".9">
      <circle cx="118" cy="70" r="3"/><circle cx="292" cy="62" r="2.4"/>
      <circle cx="330" cy="118" r="2"/><circle cx="76" cy="120" r="2"/>
    </g>
    <g fill="url(#g1)" opacity=".55">
      <circle cx="262" cy="36" r="2.6"/><circle cx="142" cy="44" r="2.2"/>
    </g>
  </g>""",

    # =======================================================================
    # MICROSOFT OFFICE — one scene per product, in that product's own hue
    # =======================================================================
    "microsoft-word": """
  <g>
    {haze}{grid}
    <g transform="rotate(-6 200 150)">
      <rect x="128" y="52" width="144" height="196" rx="10" fill="url(#gsoft)"/>
      <rect x="128" y="52" width="144" height="196" rx="10" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
      <g fill="url(#g1)">
        <rect x="148" y="82" width="84" height="8" rx="4"/>
        <rect x="148" y="102" width="104" height="6" rx="3" opacity=".65"/>
        <rect x="148" y="120" width="96" height="6" rx="3" opacity=".65"/>
        <rect x="148" y="138" width="104" height="6" rx="3" opacity=".65"/>
        <rect x="148" y="156" width="62" height="6" rx="3" opacity=".65"/>
      </g>
      <rect x="148" y="174" width="2.6" height="14" fill="#fff" opacity=".9"/>
      <rect x="214" y="174" width="38" height="6" rx="3" fill="url(#g1)" opacity=".4"/>
    </g>
    <g transform="translate(286 196)">
      <rect x="-30" y="-30" width="60" height="60" rx="14" fill="url(#g1)"/>
      <path d="M-14 -8l6 18 8-13 8 13 6-18" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </g>""",

    "microsoft-excel": """
  <g>
    {haze}{grid}
    <rect x="66" y="66" width="268" height="168" rx="10" fill="url(#gsoft)"/>
    <rect x="66" y="66" width="268" height="168" rx="10" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
    <rect x="66" y="66" width="268" height="26" rx="10" fill="url(#g1)" opacity=".55"/>
    <g stroke="url(#g1)" stroke-width="1" opacity=".4">
      <path d="M66 122h268M66 152h268M66 182h268M66 212h268"/>
      <path d="M120 92v142M174 92v142M228 92v142M282 92v142"/>
    </g>
    <g fill="url(#g1)">
      <rect x="126" y="188" width="42" height="22" opacity=".35"/>
      <rect x="180" y="158" width="42" height="52" opacity=".6"/>
      <rect x="234" y="128" width="42" height="82" opacity=".85"/>
      <rect x="288" y="98" width="40" height="112"/>
    </g>
    <g transform="translate(200 40)">
      <rect x="-46" y="-16" width="92" height="32" rx="8" fill="url(#g1)" opacity=".9"/>
      <text x="0" y="6" text-anchor="middle" font-family="monospace" font-size="16" font-weight="700" fill="#fff">=SUM()</text>
    </g>
  </g>""",

    "microsoft-powerpoint": """
  <g>
    {haze}{grid}
    <rect x="104" y="46" width="192" height="118" rx="10" fill="url(#gsoft)" opacity=".6"/>
    <rect x="72" y="78" width="192" height="118" rx="10" fill="url(#gsoft)"/>
    <rect x="72" y="78" width="192" height="118" rx="10" fill="none" stroke="url(#g1)" stroke-width="1.7"/>
    <g fill="url(#g1)">
      <rect x="96" y="140" width="26" height="38" rx="4" opacity=".5"/>
      <rect x="130" y="122" width="26" height="56" rx="4" opacity=".75"/>
      <rect x="164" y="104" width="26" height="74" rx="4"/>
    </g>
    <g fill="url(#g1)" opacity=".55">
      <rect x="204" y="104" width="40" height="7" rx="3.5"/>
      <rect x="204" y="120" width="32" height="7" rx="3.5" opacity=".7"/>
      <rect x="204" y="136" width="38" height="7" rx="3.5" opacity=".5"/>
    </g>
    <g transform="translate(300 208)">
      <rect x="-30" y="-30" width="60" height="60" rx="14" fill="url(#g1)"/>
      <path d="M-8 10v-24h9a8 8 0 010 16h-9" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </g>""",

    "microsoft-access": """
  <g>
    {haze}{grid}
    <ellipse cx="200" cy="86" rx="96" ry="26" fill="url(#g1)" opacity=".85"/>
    <path d="M104 86v96c0 14 43 26 96 26s96-12 96-26V86" fill="url(#gsoft)"/>
    <path d="M104 86v96c0 14 43 26 96 26s96-12 96-26V86" fill="none" stroke="url(#g1)" stroke-width="1.7"/>
    <ellipse cx="200" cy="134" rx="96" ry="26" fill="none" stroke="url(#g1)" stroke-width="1.2" opacity=".6"/>
    <ellipse cx="200" cy="182" rx="96" ry="26" fill="none" stroke="url(#g1)" stroke-width="1.2" opacity=".35"/>
    <path d="M296 108h34a14 14 0 0114 14v52" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="1.6"/>
    <rect x="326" y="174" width="44" height="44" rx="8" fill="url(#g1)" opacity=".8"/>
    <g fill="#fff" opacity=".85">
      <rect x="336" y="186" width="24" height="4" rx="2"/>
      <rect x="336" y="196" width="16" height="4" rx="2" opacity=".7"/>
    </g>
    <g fill="#fff" opacity=".9">
      <circle cx="170" cy="134" r="3"/><circle cx="200" cy="134" r="3"/><circle cx="230" cy="134" r="3"/>
    </g>
  </g>""",

    "word-excel-combo": """
  <g>
    {haze}{grid}
    <rect x="62" y="72" width="132" height="164" rx="12" fill="url(#gsoft)"/>
    <rect x="62" y="72" width="132" height="164" rx="12" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
    <rect x="206" y="72" width="132" height="164" rx="12" fill="url(#gsoft)"/>
    <rect x="206" y="72" width="132" height="164" rx="12" fill="none" stroke="url(#g1)" stroke-width="1.6"/>
    <g fill="url(#g1)" opacity=".7">
      <rect x="80" y="98" width="72" height="8" rx="4"/>
      <rect x="80" y="118" width="96" height="6" rx="3" opacity=".7"/>
      <rect x="80" y="136" width="84" height="6" rx="3" opacity=".7"/>
      <rect x="80" y="154" width="60" height="6" rx="3" opacity=".7"/>
    </g>
    <g stroke="url(#g1)" stroke-width="1" opacity=".45">
      <path d="M206 122h132M206 152h132M206 182h132"/>
      <path d="M250 84v152M294 84v152"/>
    </g>
    <g fill="url(#g1)">
      <rect x="256" y="158" width="38" height="22" opacity=".55"/>
      <rect x="300" y="128" width="38" height="52" opacity=".9"/>
    </g>
    <g transform="translate(200 250)">
      <path d="M-18 0h36M10 -7l9 7-9 7" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </g>""",

    "microsoft-office-suite": """
  <g>
    {haze}{grid}
    <circle cx="200" cy="150" r="106" fill="none" stroke="url(#g1)" stroke-width="1" opacity=".3" stroke-dasharray="3 7"/>
    <g>
      <rect x="130" y="80" width="66" height="66" rx="14" fill="url(#g1)" opacity=".9"/>
      <rect x="204" y="80" width="66" height="66" rx="14" fill="url(#g1)" opacity=".62"/>
      <rect x="130" y="154" width="66" height="66" rx="14" fill="url(#g1)" opacity=".45"/>
      <rect x="204" y="154" width="66" height="66" rx="14" fill="url(#g1)" opacity=".28"/>
    </g>
    <g fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" opacity=".92">
      <path d="M148 104l6 18 8-13 8 13 6-18"/>
      <path d="M222 96l14 18M236 96l-14 18"/>
      <path d="M148 178v16h9a8 8 0 010-16h-9"/>
      <path d="M220 190h16M228 182v16"/>
    </g>
    <circle cx="200" cy="150" r="9" fill="#fff" opacity=".85"/>
  </g>""",
}


def art(slug: str, width: int = 400, height: int = 300,
        c1: str = "#ffde59", c2: str = "#e3a821") -> str:
    """Return a conceptual illustration as inline SVG."""
    body = ART.get(slug, ART["ai-foundation"]).format(haze=_haze(), grid=_grid())
    defs = _DEFS % {"a": c1, "b": c2}
    return (
        f'<svg viewBox="0 0 400 300" width="{width}" height="{height}" '
        f'xmlns="http://www.w3.org/2000/svg">{defs}{body}</svg>'
    )
