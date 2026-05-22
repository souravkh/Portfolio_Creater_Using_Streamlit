import streamlit as st
import os
from utils.jsonimport import JsonImporter

st.set_page_config(
    page_title="About Me",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

data = JsonImporter.load_data_from_file("./data/myinfo.json")

resume_file_name = data.get("profile", {}).get("resume", {}).get("file_name", "Resume.pdf")
static_resume_path = os.path.join("static", resume_file_name)

if os.path.exists(static_resume_path):
    resume_url = f"app/static/{resume_file_name}"
    resume_tag = f'''<a href="{resume_url}" download="{resume_file_name}" target="_blank" class="btn-primary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        Resume
    </a>'''
else:
    resume_tag = ""

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ── Reset & Base ── */
html, body, [class*="css"], [data-testid] {
    font-family: 'Inter', sans-serif !important;
}

/* ── Animated Mesh Gradient Background ── */
[data-testid="stAppViewContainer"] {
    background-color: #0D0D14;
    background-image:
        radial-gradient(ellipse 80% 60% at 20% 10%, rgba(120, 60, 220, 0.25) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 80% 20%, rgba(0, 200, 180, 0.15) 0%, transparent 55%),
        radial-gradient(ellipse 70% 60% at 50% 90%, rgba(220, 50, 150, 0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 90% 70%, rgba(80, 120, 255, 0.12) 0%, transparent 50%);
    background-attachment: fixed;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(13, 13, 20, 0.92) !important;
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.08) !important;
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] label {
    color: #A8A8B8 !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #E2E8F0 !important;
}
[data-testid="stSidebar"] a {
    color: #C4B5FD !important;
    text-decoration: none;
}
[data-testid="stSidebar"] a:hover {
    color: #A78BFA !important;
}
/* Sidebar nav active link */
[data-testid="stSidebar"] [aria-selected="true"] {
    color: #C084FC !important;
    background: rgba(168,85,247,0.12) !important;
    border-radius: 8px;
}

/* ── Block container ── */
[data-testid="block-container"] {
    background: transparent;
    padding: 3rem 3rem 2rem !important;
    max-width: 960px;
    margin: 0 auto;
}

/* ── Hide only the Streamlit footer branding ── */
footer { visibility: hidden; }
/* Keep header/sidebar toggle visible */

/* ── Floating orb decoration ── */
.hero-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.4;
    pointer-events: none;
}

/* ── Hero section ── */
.hero-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    gap: 48px;
    padding: 56px 48px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    backdrop-filter: blur(12px);
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow:
        0 0 0 1px rgba(192,132,252,0.05),
        0 32px 64px rgba(0,0,0,0.4),
        inset 0 1px 0 rgba(255,255,255,0.06);
}

.hero-wrapper::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(168,85,247,0.18) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-wrapper::after {
    content: '';
    position: absolute;
    bottom: -60px; left: -60px;
    width: 240px; height: 240px;
    background: radial-gradient(circle, rgba(20,184,166,0.12) 0%, transparent 70%);
    border-radius: 50%;
}

.profile-img-wrap {
    flex-shrink: 0;
    position: relative;
    z-index: 1;
}
.profile-img-wrap img {
    width: 160px;
    height: 160px;
    border-radius: 20px;
    object-fit: cover;
    border: 2px solid rgba(192,132,252,0.3);
    box-shadow: 0 0 40px rgba(168,85,247,0.2), 0 8px 24px rgba(0,0,0,0.4);
}

.hero-content { position: relative; z-index: 1; }

.hero-eyebrow {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #14B8A6;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px; height: 1.5px;
    background: #14B8A6;
}

.hero-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 700;
    color: #F8FAFC;
    line-height: 1.1;
    letter-spacing: -1.5px;
    margin: 0 0 14px 0;
}

.hero-title-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(168,85,247,0.15), rgba(20,184,166,0.1));
    border: 1px solid rgba(168,85,247,0.3);
    color: #C084FC;
    border-radius: 50px;
    padding: 5px 16px;
    font-size: 0.82rem;
    font-weight: 500;
    margin-bottom: 16px;
    letter-spacing: 0.2px;
}
.hero-title-badge::before {
    content: '';
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #A855F7;
    box-shadow: 0 0 8px #A855F7;
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.7); }
}

.hero-bio {
    font-size: 0.95rem;
    color: #94A3B8;
    line-height: 1.75;
    max-width: 520px;
    margin-bottom: 28px;
}

/* ── Buttons ── */
.btn-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
}

.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: linear-gradient(135deg, #7C3AED, #A855F7);
    color: #FFFFFF !important;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-size: 0.85rem;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    text-decoration: none !important;
    white-space: nowrap;
    transition: all 0.25s cubic-bezier(0.4,0,0.2,1);
    box-shadow: 0 4px 15px rgba(124,58,237,0.35);
    cursor: pointer;
}
.btn-primary:hover {
    background: linear-gradient(135deg, #6D28D9, #9333EA);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(124,58,237,0.5);
    color: #FFFFFF !important;
}

.btn-ghost {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(255,255,255,0.05);
    color: #CBD5E1 !important;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 0.85rem;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
    text-decoration: none !important;
    white-space: nowrap;
    transition: all 0.25s cubic-bezier(0.4,0,0.2,1);
    cursor: pointer;
    backdrop-filter: blur(8px);
}
.btn-ghost:hover {
    background: rgba(255,255,255,0.1);
    border-color: rgba(192,132,252,0.4);
    color: #E2E8F0 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}

/* ── Responsive ── */
@media (max-width: 700px) {
    .hero-wrapper { flex-direction: column; padding: 36px 24px; text-align: center; }
    .hero-eyebrow { justify-content: center; }
    [data-testid="block-container"] { padding: 1.5rem 1rem 2rem !important; }
}
@media (max-width: 500px) {
    [data-testid="stImage"] img {
        margin: 0 auto !important; display: block !important;
        max-width: 110px !important; border-radius: 16px;
    }
}

/* ── Streamlit image override to fit in hero ── */
[data-testid="stImage"] {
    display: contents !important;
}
[data-testid="stImage"] > div { display: contents !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# Hero Card
# ─────────────────────────────────────────
col_img, col_info = st.columns([1, 2.8], gap="large", vertical_alignment="center")

with col_img:
    st.image(data["profile"]["profile_image"], width=160)

with col_info:
    st.html(f"""
    <div>
        <div class="hero-eyebrow">Portfolio</div>
        <h1 class="hero-name">{data['profile']['name']}</h1>
        <div class="hero-title-badge">{data['profile']['title']}</div>
        <p class="hero-bio">{data['profile']['short_summary']}</p>

        <div class="btn-row">
            <a href="{data['profile']['contact']['linkedin']['url']}" target="_blank" class="btn-ghost">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                LinkedIn
            </a>
            <a href="{data['profile']['contact']['github']['url']}" target="_blank" class="btn-ghost">
                <svg width="15" height="15" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
                GitHub
            </a>
            <a href="{data['profile']['contact']['mailto']}" class="btn-ghost">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                Email
            </a>
            {resume_tag}
        </div>
    </div>
    """)