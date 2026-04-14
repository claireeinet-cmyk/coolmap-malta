"""CoolMap Malta — shared branding helpers."""

import streamlit as st


# Brand palette — Malta Mediterranean
COOLMAP_BLUE = "#0B6E99"
COOLMAP_TEAL = "#14A5A5"
COOLMAP_SAND = "#F4E3C6"
COOLMAP_CORAL = "#E8704E"
COOLMAP_SHADE = "#1C2B33"   # dark text
COOLMAP_LEAF = "#4A9A62"

UTCI_COLORS = {
    "Strong cold":      "#053061",
    "Moderate cold":    "#2166AC",
    "Slight cold":      "#67A9CF",
    "No stress":        "#92C5DE",
    "Moderate heat":    "#FDDBC7",
    "Strong heat":      "#F4A582",
    "Very strong heat": "#D6604D",
    "Extreme heat":     "#B2182B",
}

# Text colours for UTCI legend chips — dark for pale chips, white for dark ones
UTCI_TEXT = {
    "Strong cold":      "#ffffff",
    "Moderate cold":    "#ffffff",
    "Slight cold":      "#1C2B33",
    "No stress":        "#1C2B33",
    "Moderate heat":    "#1C2B33",
    "Strong heat":      "#1C2B33",
    "Very strong heat": "#ffffff",
    "Extreme heat":     "#ffffff",
}


def logo_svg() -> str:
    return f"""
<svg viewBox="0 0 64 64" width="46" height="46" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{COOLMAP_BLUE}"/>
      <stop offset="100%" stop-color="{COOLMAP_TEAL}"/>
    </linearGradient>
  </defs>
  <circle cx="32" cy="32" r="30" fill="url(#sky)"/>
  <circle cx="42" cy="26" r="10" fill="#FFD66B"/>
  <path d="M8 44 Q20 30 32 44 T56 44 L56 56 L8 56 Z" fill="{COOLMAP_SAND}"/>
  <path d="M22 44 C 22 32, 32 28, 42 30 C 34 32, 28 38, 26 44 Z" fill="{COOLMAP_LEAF}"/>
  <path d="M14 44 C 14 36, 22 34, 30 36 C 22 38, 18 42, 18 44 Z" fill="{COOLMAP_LEAF}" opacity="0.8"/>
</svg>
""".strip()


def apply_branding():
    """Inject global styles — all custom elements use explicit colours, no inheritance."""
    st.markdown(
        f"""
<style>
/* ── Global body text ─────────────────────────────────────────────── */
.stApp, .main, .block-container {{
  color: {COOLMAP_SHADE} !important;
  background-color: #F8FAFB !important;
}}

/* Make sure plain markdown paragraphs are always dark */
.stMarkdown p,
.stMarkdown li,
.stMarkdown td,
.stMarkdown th,
.stMarkdown blockquote,
.stMarkdown code {{
  color: {COOLMAP_SHADE} !important;
}}

/* ── Headings ─────────────────────────────────────────────────────── */
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
h1, h2, h3 {{
  color: {COOLMAP_SHADE} !important;
  font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
}}

/* ── Metrics ──────────────────────────────────────────────────────── */
[data-testid="stMetricValue"] {{
  color: {COOLMAP_BLUE} !important;
  font-weight: 700;
}}
[data-testid="stMetricLabel"],
[data-testid="stMetricDelta"] {{
  color: {COOLMAP_SHADE} !important;
}}

/* ── Sidebar ──────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {{
  background: #EBF4F7 !important;
}}
section[data-testid="stSidebar"] * {{
  color: {COOLMAP_SHADE} !important;
}}
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown span,
section[data-testid="stSidebar"] label {{
  color: {COOLMAP_SHADE} !important;
}}

/* ── Widgets ──────────────────────────────────────────────────────── */
label, .stSlider label, .stRadio label,
.stSelectbox label, .stCheckbox label {{
  color: {COOLMAP_SHADE} !important;
  font-weight: 500;
}}
.stRadio div[role="radiogroup"] label span,
.stCheckbox label span {{
  color: {COOLMAP_SHADE} !important;
}}

/* ── Dataframes / tables ──────────────────────────────────────────── */
.stDataFrame, .stDataFrame * {{
  color: {COOLMAP_SHADE} !important;
}}

/* ── Info / warning / success boxes ──────────────────────────────── */
.stAlert p, .stAlert span {{
  color: {COOLMAP_SHADE} !important;
}}

/* ── Hero banner ──────────────────────────────────────────────────── */
.cm-hero {{
  background: linear-gradient(135deg, {COOLMAP_BLUE} 0%, {COOLMAP_TEAL} 100%);
  padding: 1.5rem 1.8rem;
  border-radius: 14px;
  margin-bottom: 1.4rem;
  box-shadow: 0 8px 24px rgba(11,110,153,0.18);
  display: flex;
  align-items: center;
  gap: 1.2rem;
}}
.cm-hero-text h1 {{
  color: #FFFFFF !important;
  margin: 0 0 .25rem 0 !important;
  font-size: 1.85rem !important;
  font-weight: 700;
}}
.cm-hero-text .cm-subtitle {{
  color: #D8EFF5 !important;
  margin: 0;
  font-size: 1rem;
  line-height: 1.4;
}}
.cm-hero-text .cm-tagline {{
  color: #B8DCE6 !important;
  margin-top: .4rem;
  font-size: 0.85rem;
  letter-spacing: 0.01em;
}}

/* ── Info card ────────────────────────────────────────────────────── */
.cm-card {{
  background: #FFFFFF;
  border: 1px solid #D0DDE3;
  border-left: 4px solid {COOLMAP_TEAL};
  border-radius: 10px;
  padding: 1rem 1.2rem;
  margin: .6rem 0;
  color: {COOLMAP_SHADE} !important;
}}
.cm-card * {{
  color: {COOLMAP_SHADE} !important;
}}
.cm-card b, .cm-card strong {{
  color: {COOLMAP_BLUE} !important;
}}

/* ── Stage card (methodology page) ───────────────────────────────── */
.cm-stage {{
  background: #FFFFFF;
  border: 1px solid #D0DDE3;
  border-radius: 12px;
  padding: 1.1rem 1.3rem;
  margin: .7rem 0;
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  color: {COOLMAP_SHADE} !important;
}}
.cm-stage * {{
  color: {COOLMAP_SHADE} !important;
}}
.cm-stage-num {{
  background: {COOLMAP_BLUE};
  color: #FFFFFF !important;
  border-radius: 50%;
  min-width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1rem;
  flex-shrink: 0;
}}
.cm-stage-title {{
  font-weight: 700;
  font-size: 1.05rem;
  color: {COOLMAP_BLUE} !important;
  margin-bottom: .3rem;
}}
.cm-stage-body {{
  color: {COOLMAP_SHADE} !important;
  font-size: 0.95rem;
  line-height: 1.5;
}}

/* ── Sidebar brand block ──────────────────────────────────────────── */
.cm-sidebar-brand-name {{
  font-weight: 700;
  font-size: 1.05rem;
  color: {COOLMAP_SHADE} !important;
}}
.cm-sidebar-brand-sub {{
  font-size: 0.75rem;
  color: #4A6070 !important;
}}
.cm-sidebar-meta {{
  font-size: 0.78rem;
  color: #4A6070 !important;
  line-height: 1.5;
}}

/* ── Footer ───────────────────────────────────────────────────────── */
.cm-footer {{
  margin-top: 2.5rem;
  padding-top: 1rem;
  border-top: 1px solid #D0DDE3;
  color: #5B6F79 !important;
  font-size: 0.82rem;
  text-align: center;
}}
</style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar header
    with st.sidebar:
        st.markdown(
            f"""
<div style="display:flex;align-items:center;gap:.7rem;padding:.4rem 0 .9rem 0;">
  {logo_svg()}
  <div>
    <div class="cm-sidebar-brand-name">CoolMap Malta</div>
    <div class="cm-sidebar-brand-sub">Thermal comfort intelligence</div>
  </div>
</div>
<div class="cm-sidebar-meta">
  Hosted by <strong style="color:{COOLMAP_SHADE};">K³ KlimaKarten</strong><br/>
  Scientific lead: <strong style="color:{COOLMAP_SHADE};">Claire Gallacher</strong><br/>
  <span style="color:#6A8090;">Leibniz IÖR Dresden · Gallacher &amp; Boehnke, 2024</span>
</div>
""",
            unsafe_allow_html=True,
        )
        st.divider()


def hero_banner(title: str, subtitle: str, tagline: str = ""):
    st.markdown(
        f"""
<div class="cm-hero">
  <div>{logo_svg().replace('width="46" height="46"', 'width="68" height="68"')}</div>
  <div class="cm-hero-text">
    <h1>{title}</h1>
    <div class="cm-subtitle">{subtitle}</div>
    {f'<div class="cm-tagline">{tagline}</div>' if tagline else ''}
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def card(body_html: str):
    """A readable card with explicit dark text."""
    st.markdown(f'<div class="cm-card">{body_html}</div>', unsafe_allow_html=True)


def stage_card(number: str, title: str, body: str):
    """Numbered stage card for the methodology page."""
    st.markdown(
        f"""
<div class="cm-stage">
  <div class="cm-stage-num">{number}</div>
  <div>
    <div class="cm-stage-title">{title}</div>
    <div class="cm-stage-body">{body}</div>
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def footer():
    st.markdown(
        f"""
<div class="cm-footer">
  CoolMap Malta &nbsp;·&nbsp; Hosted by K³ KlimaKarten &nbsp;·&nbsp; F6S Application v6 &nbsp;·&nbsp; April 2026<br/>
  Category C — Technology and Digital Innovation for Urban Climate Adaptation &nbsp;·&nbsp;
  Based on Gallacher &amp; Boehnke (2024), <em>Int. J. of Biometeorology</em>
</div>
        """,
        unsafe_allow_html=True,
    )


def utci_legend():
    """Render a row of UTCI colour chips with readable text."""
    chips = "".join(
        f'<span style="background:{bg};color:{UTCI_TEXT[name]};'
        f'border-radius:6px;padding:4px 8px;font-size:0.78rem;'
        f'font-weight:600;white-space:nowrap;">{name}</span>'
        for name, bg in UTCI_COLORS.items()
    )
    st.markdown(
        f'<div style="display:flex;flex-wrap:wrap;gap:6px;margin:.4rem 0;">{chips}</div>',
        unsafe_allow_html=True,
    )


def utci_category(utci_c: float) -> str:
    if utci_c < -13: return "Strong cold"
    if utci_c < 0:   return "Moderate cold"
    if utci_c < 9:   return "Slight cold"
    if utci_c <= 26: return "No stress"
    if utci_c <= 32: return "Moderate heat"
    if utci_c <= 38: return "Strong heat"
    if utci_c <= 46: return "Very strong heat"
    return "Extreme heat"
