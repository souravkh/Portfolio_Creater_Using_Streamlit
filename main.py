import streamlit as st
import os

st.set_page_config(
    page_title="My Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

about_me = st.Page(
    page="Pages/aboutme.py",
    title="About me",
    default=True,
    icon="👤"
)

main_content = st.Page(
    page="Pages/maincontent.py",
    title="Experience/Projects",
    icon="💼"
)

# ─────────────────────────────────────────────
# Global dark theme injected into every page
# ─────────────────────────────────────────────
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ── Animated Mesh Gradient Background (global) ── */
[data-testid="stAppViewContainer"] {
    background-color: #0D0D14;
    background-image:
        radial-gradient(ellipse 80% 60% at 20% 10%, rgba(120, 60, 220, 0.25) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 80% 20%, rgba(0, 200, 180, 0.15) 0%, transparent 55%),
        radial-gradient(ellipse 70% 60% at 50% 90%, rgba(220, 50, 150, 0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 90% 70%, rgba(80, 120, 255, 0.12) 0%, transparent 50%);
    background-attachment: fixed;
}

/* ── Sidebar background ── */
[data-testid="stSidebar"] {
    background: rgba(10, 10, 18, 0.96) !important;
    backdrop-filter: blur(24px);
    border-right: 1px solid rgba(255, 255, 255, 0.07) !important;
}

/* ── Sidebar title / subheaders ── */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] .stSubheader p {
    color: #E2E8F0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: -0.3px;
}

/* ── Sidebar body text / markdown ── */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] small {
    color: #94A3B8 !important;
    font-size: 0.85rem;
}

/* ── Sidebar nav links ── */
[data-testid="stSidebar"] a {
    color: #A78BFA !important;
    text-decoration: none !important;
    font-weight: 500;
    transition: color 0.2s;
}
[data-testid="stSidebar"] a:hover {
    color: #C084FC !important;
}

/* ── Sidebar page nav items ── */
[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
    border-radius: 8px !important;
    transition: background 0.2s;
    color: #94A3B8 !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover {
    background: rgba(168, 85, 247, 0.1) !important;
    color: #E2E8F0 !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNavLink"][aria-selected="true"],
[data-testid="stSidebar"] [aria-current="page"] {
    background: rgba(168, 85, 247, 0.15) !important;
    color: #C084FC !important;
    border-left: 2px solid #A855F7;
}

/* ── Sidebar horizontal rule ── */
[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.08) !important;
}

/* ── Sidebar collapse/expand button arrow ── */
[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"] {
    color: #A78BFA !important;
    background: rgba(10,10,18,0.95) !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
}

/* ── Hide Streamlit footer branding only ── */
footer { visibility: hidden; }

/* ── Global font ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Shared sidebar content ──────────────────
st.logo("Images/bolt.svg")

st.sidebar.markdown("""
<div style="padding: 4px 0 12px 0;">
    <div style="
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #F1F5F9 !important;
        letter-spacing: -0.4px;
        margin-bottom: 2px;
    ">Portfolio</div>
    <div style="font-size: 0.75rem; color: #64748B !important;">
        Made by <a href="https://github.com/souravkh" target="_blank"
        style="color:#A78BFA !important; text-decoration: ; font-weight:500;"><b>Sourav</b></a>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.divider()

st.sidebar.markdown("""<p style="font-size:0.7rem; font-weight:700; letter-spacing:2px;
    text-transform:uppercase; color:#64748B !important; margin-bottom:4px;">Info</p>""",
    unsafe_allow_html=True)
st.sidebar.page_link(about_me)

st.sidebar.markdown("""<p style="font-size:0.7rem; font-weight:700; letter-spacing:2px;
    text-transform:uppercase; color:#64748B !important; margin:8px 0 4px 0;">Projects</p>""",
    unsafe_allow_html=True)
st.sidebar.page_link(main_content)

# ── Navigation ───────────────────────────────
pages = st.navigation(
    {
        "Info": [about_me],
        "Work Experience": [main_content],
    },
    position="hidden"
)
pages.run()