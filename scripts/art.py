"""Vector illustration library.

Everything here is original SVG drawn for this repository — no stock art, no
licensing questions, and every piece is tinted with the caller's accent colour
so covers stay on-brand.

Two families:
  ICONS  — 48x48 line glyphs, one per course, used on covers and cards.
  ART    — 400x300 conceptual illustrations used as the hero figure on each
           course book's first page and as decorative panels.
"""

from __future__ import annotations

_S = 'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" fill="none"'

ICONS: dict[str, str] = {
    # --- AI ---------------------------------------------------------------
    "spark": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M24 6l4.2 10.4L38.6 20 28.2 24.2 24 34.6 19.8 24.2 9.4 20l10.4-3.6z"/>
        <path d="M37 32l1.8 4.4L43 38l-4.2 1.6L37 44l-1.8-4.4L31 38l4.2-1.6z"/>
        <path d="M10 32l1.4 3.4L14.8 37l-3.4 1.4L10 42l-1.4-3.6L5.2 37l3.4-1.6z"/>
    </g></svg>""",
    "circuit": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="14" y="14" width="20" height="20" rx="4"/>
        <path d="M24 8v6M24 34v6M8 24h6M34 24h6"/>
        <circle cx="24" cy="24" r="4"/>
        <circle cx="24" cy="6" r="2.4"/><circle cx="24" cy="42" r="2.4"/>
        <circle cx="6" cy="24" r="2.4"/><circle cx="42" cy="24" r="2.4"/>
    </g></svg>""",
    "blocks": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="7" y="27" width="15" height="14" rx="3"/>
        <rect x="26" y="27" width="15" height="14" rx="3"/>
        <rect x="16" y="7" width="16" height="14" rx="3"/>
        <path d="M24 21v6M14 27v-3h20v3"/>
    </g></svg>""",
    "shield": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M24 6l14 5v11c0 9-6 16-14 20-8-4-14-11-14-20V11z"/>
        <path d="M18 24l4.5 4.5L31 20"/>
    </g></svg>""",
    # --- Software ---------------------------------------------------------
    "laptop": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="9" y="11" width="30" height="20" rx="3"/>
        <path d="M5 35h38M14 39h20"/>
        <path d="M18 20l4 4-4 4M26 28h5"/>
    </g></svg>""",
    "word": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M12 7h16l9 9v25a2 2 0 01-2 2H12a2 2 0 01-2-2V9a2 2 0 012-2z"/>
        <path d="M28 7v9h9"/>
        <path d="M16 26l3 9 3.5-6 3.5 6 3-9"/>
    </g></svg>""",
    "excel": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M12 7h16l9 9v25a2 2 0 01-2 2H12a2 2 0 01-2-2V9a2 2 0 012-2z"/>
        <path d="M28 7v9h9"/>
        <path d="M17 23l8 12M25 23l-8 12"/>
    </g></svg>""",
    "powerpoint": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M12 7h16l9 9v25a2 2 0 01-2 2H12a2 2 0 01-2-2V9a2 2 0 012-2z"/>
        <path d="M28 7v9h9"/>
        <path d="M19 34V23h5a4 4 0 010 8h-5"/>
    </g></svg>""",
    "database": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <ellipse cx="24" cy="13" rx="13" ry="5.5"/>
        <path d="M11 13v22c0 3 5.8 5.5 13 5.5s13-2.5 13-5.5V13"/>
        <path d="M11 24c0 3 5.8 5.5 13 5.5s13-2.5 13-5.5"/>
    </g></svg>""",
    "wordexcel": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="5" y="10" width="18" height="28" rx="3"/>
        <rect x="25" y="10" width="18" height="28" rx="3"/>
        <path d="M10 20l3 8 2.5-5 2.5 5 3-8"/>
        <path d="M30 20l6 8M36 20l-6 8"/>
    </g></svg>""",
    "suite": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="6" y="6" width="16" height="16" rx="3"/>
        <rect x="26" y="6" width="16" height="16" rx="3"/>
        <rect x="6" y="26" width="16" height="16" rx="3"/>
        <rect x="26" y="26" width="16" height="16" rx="3"/>
        <path d="M12 14h4M12 34l4-4M32 34v-4M34 14h-4"/>
    </g></svg>""",
    # --- STEM -------------------------------------------------------------
    "flask": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M19 7h10v10l9 18a4 4 0 01-3.6 5.8H13.6A4 4 0 0110 35l9-18z"/>
        <path d="M14.5 30h19"/>
        <path d="M21 7v10M27 7v10"/>
    </g></svg>""",
    "robot": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="11" y="15" width="26" height="20" rx="6"/>
        <circle cx="19" cy="25" r="2.4"/><circle cx="29" cy="25" r="2.4"/>
        <path d="M24 15V9M20 35v5M28 35v5M11 25H7M37 25h4"/>
    </g></svg>""",
    # --- Design -----------------------------------------------------------
    "pen": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M9 39l3-9 20-20a3.5 3.5 0 015 5L17 35z"/>
        <path d="M28 14l6 6"/>
        <path d="M9 39l8-2"/>
    </g></svg>""",
    "camera": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <rect x="5" y="13" width="38" height="26" rx="5"/>
        <circle cx="24" cy="26" r="8"/>
        <path d="M17 13l3-5h8l3 5"/>
        <circle cx="36" cy="19" r="1.6"/>
    </g></svg>""",
    "megaphone": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M9 20v8a3 3 0 003 3h4l16 8V9L16 17h-4a3 3 0 00-3 3z"/>
        <path d="M16 31v8a3 3 0 006 0v-6"/>
        <path d="M37 19a6 6 0 010 10"/>
    </g></svg>""",
    # --- Finance ----------------------------------------------------------
    "chart": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M7 41h34"/>
        <path d="M7 41V9"/>
        <path d="M14 34l8-10 7 5 11-14"/>
        <circle cx="22" cy="24" r="2.2"/><circle cx="29" cy="29" r="2.2"/>
    </g></svg>""",
    "growth": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <path d="M8 40h32"/>
        <rect x="11" y="28" width="6" height="12" rx="2"/>
        <rect x="21" y="20" width="6" height="20" rx="2"/>
        <rect x="31" y="12" width="6" height="28" rx="2"/>
        <path d="M11 20l9-6 7 3 8-8"/>
    </g></svg>""",
    "coin": f"""<svg viewBox="0 0 48 48"><g {_S}>
        <circle cx="24" cy="24" r="16"/>
        <path d="M24 14v20M19 19h8a4 4 0 010 8h-6a4 4 0 000 8h8"/>
    </g></svg>""",
}

_FALLBACK = ICONS["spark"]


def icon(name: str, size: int = 40, color: str = "currentColor", extra: str = "") -> str:
    """Return an icon as inline SVG, sized and coloured."""
    svg = ICONS.get(name, _FALLBACK)
    return svg.replace(
        "<svg ",
        f'<svg width="{size}" height="{size}" style="color:{color};{extra}" ',
        1,
    )


# ---------------------------------------------------------------------------
# Conceptual artwork. Each is a wide 400x300 composition built from shapes,
# designed to sit behind or beside text without competing with it.
# ---------------------------------------------------------------------------
ART: dict[str, str] = {
    "ai-foundation": """
      <g stroke="none">
        <circle cx="200" cy="150" r="96" fill="url(#g1)" opacity=".16"/>
        <circle cx="200" cy="150" r="96" fill="none" stroke="url(#g1)" stroke-width="1.6" opacity=".55"/>
        <circle cx="200" cy="150" r="64" fill="none" stroke="url(#g1)" stroke-width="1.2" opacity=".4"/>
        <circle cx="200" cy="150" r="120" fill="none" stroke="url(#g1)" stroke-width=".9" opacity=".22"/>
        <g stroke="url(#g1)" stroke-width="1.3" opacity=".55">
          <path d="M200 54L200 150M200 246L200 150M104 150L200 150M296 150L200 150"/>
          <path d="M132 82L200 150M268 82L200 150M132 218L200 150M268 218L200 150"/>
        </g>
        <g fill="url(#g1)">
          <circle cx="200" cy="54" r="6"/><circle cx="200" cy="246" r="6"/>
          <circle cx="104" cy="150" r="6"/><circle cx="296" cy="150" r="6"/>
          <circle cx="132" cy="82" r="5"/><circle cx="268" cy="82" r="5"/>
          <circle cx="132" cy="218" r="5"/><circle cx="268" cy="218" r="5"/>
          <circle cx="200" cy="150" r="14"/>
        </g>
      </g>""",
    "ai-practitioner": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="56" y="120" width="76" height="52" rx="10" stroke-width="1.8"/>
        <rect x="162" y="60" width="76" height="52" rx="10" stroke-width="1.8"/>
        <rect x="162" y="180" width="76" height="52" rx="10" stroke-width="1.8"/>
        <rect x="268" y="120" width="76" height="52" rx="10" stroke-width="1.8"/>
        <path d="M132 146h30M238 86v28h30M238 206v-28h30" stroke-width="1.6"/>
        <circle cx="94" cy="146" r="7" fill="url(#g1)" stroke="none"/>
        <circle cx="200" cy="86" r="7" fill="url(#g1)" stroke="none"/>
        <circle cx="200" cy="206" r="7" fill="url(#g1)" stroke="none"/>
        <circle cx="306" cy="146" r="7" fill="url(#g1)" stroke="none"/>
      </g>""",
    "ai-builder": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <path d="M80 220V120l60-40 60 40v100l-60 40z" stroke-width="1.8"/>
        <path d="M140 80v100M80 120l60 40 60-40M140 180l60-40" stroke-width="1.4" opacity=".7"/>
        <rect x="248" y="96" width="88" height="88" rx="14" stroke-width="1.8"/>
        <path d="M266 128h52M266 148h34M266 168h44" stroke-width="1.4" opacity=".75"/>
        <circle cx="292" cy="60" r="10" fill="url(#g1)" stroke="none" opacity=".85"/>
        <path d="M292 70v26" stroke-width="1.4" opacity=".6"/>
      </g>""",
    "ai-specialist": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <path d="M200 52l76 26v58c0 50-33 86-76 108-43-22-76-58-76-108V78z" stroke-width="1.9"/>
        <path d="M166 148l24 24 46-48" stroke-width="3.4"/>
        <circle cx="200" cy="150" r="112" stroke-width=".9" opacity=".3"/>
      </g>""",
    "scratch-coding": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="70" y="70" width="96" height="42" rx="21" stroke-width="1.9"/>
        <rect x="118" y="130" width="112" height="42" rx="21" stroke-width="1.9"/>
        <rect x="96" y="190" width="88" height="42" rx="21" stroke-width="1.9"/>
        <path d="M118 91h-16M174 151h-14M140 211h-12" stroke-width="1.6" opacity=".7"/>
        <rect x="252" y="96" width="82" height="82" rx="12" stroke-width="1.9"/>
        <path d="M272 126l22 12-22 12z" fill="url(#g1)" stroke="none"/>
      </g>""",
    "digital-literacy": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="70" y="86" width="180" height="118" rx="12" stroke-width="1.9"/>
        <path d="M48 214h224M120 226h80" stroke-width="1.7"/>
        <path d="M100 124h44M100 146h72M100 168h58" stroke-width="1.5" opacity=".75"/>
        <rect x="268" y="130" width="66" height="106" rx="12" stroke-width="1.9"/>
        <path d="M292 220h18" stroke-width="1.6" opacity=".7"/>
        <circle cx="301" cy="152" r="12" stroke-width="1.5" opacity=".8"/>
      </g>""",
    "practical-stem": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <circle cx="118" cy="150" r="58" stroke-width="1.8"/>
        <path d="M118 92v116M60 150h116M77 109l82 82M159 109l-82 82" stroke-width="1.3" opacity=".6"/>
        <circle cx="118" cy="150" r="9" fill="url(#g1)" stroke="none"/>
        <path d="M196 150h40" stroke-width="1.8"/>
        <path d="M236 122v56l48-28z" stroke-width="1.8"/>
        <rect x="296" y="120" width="34" height="60" rx="6" stroke-width="1.6" opacity=".85"/>
        <path d="M304 134h18M304 148h18M304 162h12" stroke-width="1.4" opacity=".6"/>
      </g>""",
    "graphic-design": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="70" y="70" width="130" height="160" rx="12" stroke-width="1.9"/>
        <circle cx="112" cy="112" r="18" stroke-width="1.6"/>
        <path d="M92 176h86M92 196h58" stroke-width="1.5" opacity=".75"/>
        <path d="M232 108l60 104h-120z" stroke-width="1.9"/>
        <circle cx="296" cy="86" r="22" stroke-width="1.7" opacity=".85"/>
        <path d="M262 214h68" stroke-width="1.5" opacity=".6"/>
      </g>""",
    "financial-sacco": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <path d="M60 232h280" stroke-width="1.7"/>
        <rect x="82" y="160" width="44" height="72" rx="6" stroke-width="1.7"/>
        <rect x="146" y="128" width="44" height="104" rx="6" stroke-width="1.7"/>
        <rect x="210" y="96" width="44" height="136" rx="6" stroke-width="1.7"/>
        <rect x="274" y="152" width="44" height="80" rx="6" stroke-width="1.7"/>
        <path d="M82 128l66-34 62 26 62-52" stroke-width="2.1"/>
        <circle cx="272" cy="68" r="8" fill="url(#g1)" stroke="none"/>
      </g>""",
    "microsoft-word": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <path d="M120 56h112l56 56v144a14 14 0 01-14 14H120a14 14 0 01-14-14V70a14 14 0 0114-14z" stroke-width="1.9"/>
        <path d="M232 56v56h56" stroke-width="1.7"/>
        <path d="M140 148h104M140 176h104M140 204h68" stroke-width="1.6" opacity=".7"/>
        <path d="M292 196l-16 40-14-24-14 24-16-40" stroke-width="2.4"/>
      </g>""",
    "microsoft-excel": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="76" y="70" width="248" height="164" rx="12" stroke-width="1.9"/>
        <path d="M76 118h248M76 166h248M152 70v164M228 70v164" stroke-width="1.5" opacity=".65"/>
        <path d="M106 100l16 0M182 148h16M258 196h16" stroke-width="2.2" opacity=".9"/>
        <path d="M186 196l32-40M186 156l32 40" stroke-width="2.2"/>
      </g>""",
    "microsoft-powerpoint": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="66" y="76" width="268" height="150" rx="12" stroke-width="1.9"/>
        <path d="M200 226v26M164 252h72" stroke-width="1.7"/>
        <rect x="106" y="108" width="88" height="86" rx="8" stroke-width="1.6" opacity=".8"/>
        <path d="M216 128h76M216 152h76M216 176h48" stroke-width="1.6" opacity=".7"/>
      </g>""",
    "microsoft-access": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <ellipse cx="150" cy="96" rx="76" ry="28" stroke-width="1.8"/>
        <path d="M74 96v112c0 15 34 28 76 28s76-13 76-28V96" stroke-width="1.8"/>
        <path d="M74 152c0 15 34 28 76 28s76-13 76-28" stroke-width="1.5" opacity=".7"/>
        <circle cx="300" cy="128" r="34" stroke-width="1.8"/>
        <path d="M300 110v36M290 122h16a7 7 0 010 14h-12" stroke-width="2"/>
      </g>""",
    "word-excel-combo": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="62" y="70" width="130" height="164" rx="12" stroke-width="1.8"/>
        <path d="M92 108h72M92 136h72M92 164h48" stroke-width="1.5" opacity=".7"/>
        <rect x="208" y="70" width="130" height="164" rx="12" stroke-width="1.8"/>
        <path d="M208 118h130M208 166h130M251 70v164M295 70v164" stroke-width="1.3" opacity=".6"/>
        <path d="M192 152h16" stroke-width="2.4"/>
      </g>""",
    "microsoft-office-suite": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="70" y="70" width="110" height="110" rx="12" stroke-width="1.8"/>
        <rect x="220" y="70" width="110" height="110" rx="12" stroke-width="1.8"/>
        <rect x="70" y="210" width="110" height="60" rx="12" stroke-width="1.8"/>
        <rect x="220" y="210" width="110" height="60" rx="12" stroke-width="1.8"/>
        <path d="M96 106l24 40M120 106l-24 40" stroke-width="2.2"/>
        <path d="M246 118h58M246 140h38" stroke-width="1.7" opacity=".75"/>
        <path d="M96 240h58" stroke-width="2"/>
        <circle cx="275" cy="240" r="14" stroke-width="1.7" opacity=".85"/>
      </g>""",
    "content-creation": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <rect x="66" y="86" width="150" height="132" rx="14" stroke-width="1.9"/>
        <circle cx="141" cy="152" r="34" stroke-width="1.7"/>
        <path d="M141 132v40M121 152h40" stroke-width="1.5" opacity=".55"/>
        <path d="M216 118h34v68h-34z" stroke-width="1.7" opacity=".85"/>
        <path d="M262 104c22 16 22 80 0 96" stroke-width="1.8"/>
        <path d="M288 88c30 22 30 112 0 134" stroke-width="1.8" opacity=".7"/>
        <path d="M90 246h130" stroke-width="1.6" opacity=".6"/>
        <circle cx="266" cy="222" r="18" stroke-width="1.7" opacity=".8"/>
      </g>""",
    "digital-marketing": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <path d="M72 178v44a14 14 0 0014 14h20l84 42V80l-84 42H86a14 14 0 00-14 14z" stroke-width="1.9"/>
        <path d="M110 222v34a16 16 0 0032 0v-24" stroke-width="1.7"/>
        <path d="M248 118a52 52 0 010 96" stroke-width="1.9"/>
        <path d="M282 94a92 92 0 010 144" stroke-width="1.7" opacity=".7"/>
        <circle cx="318" cy="166" r="8" fill="url(#g1)" stroke="none" opacity=".9"/>
      </g>""",
    "business-growth": """
      <g fill="none" stroke="url(#g1)" stroke-linecap="round">
        <path d="M64 244h276" stroke-width="1.7"/>
        <path d="M88 214l64-58 52 34 76-84" stroke-width="2.4"/>
        <circle cx="88" cy="214" r="8" fill="url(#g1)" stroke="none"/>
        <circle cx="152" cy="156" r="8" fill="url(#g1)" stroke="none"/>
        <circle cx="204" cy="190" r="8" fill="url(#g1)" stroke="none"/>
        <circle cx="280" cy="106" r="10" fill="url(#g1)" stroke="none"/>
        <path d="M280 106l0-44M280 62h34" stroke-width="1.6" opacity=".7"/>
        <path d="M96 96h56M96 118h34" stroke-width="1.4" opacity=".5"/>
      </g>""",
}

_DEFS = """
<defs>
  <linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="%(a)s"/>
    <stop offset="1" stop-color="%(b)s"/>
  </linearGradient>
</defs>
"""


def art(slug: str, width: int = 400, height: int = 300, c1: str = "#ffd166", c2: str = "#e3a821") -> str:
    """Return a conceptual illustration as inline SVG."""
    body = ART.get(slug, ART["ai-foundation"])
    defs = _DEFS % {"a": c1, "b": c2}
    return (
        f'<svg viewBox="0 0 400 300" width="{width}" height="{height}" '
        f'xmlns="http://www.w3.org/2000/svg">{defs}{body}</svg>'
    )
