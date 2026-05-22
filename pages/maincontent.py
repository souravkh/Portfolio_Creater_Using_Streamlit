import streamlit as st
from utils.jsonimport import JsonImporter

st.set_page_config(
    page_title="Experience",
    page_icon="👨‍💻",
    layout="wide"
)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
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

/* Hide only Streamlit footer branding, keep header/sidebar toggle */
footer { visibility: hidden; }
h1 { font-family: 'Space Grotesk', sans-serif !important; }

/* ── Section label ── */
.section-eyebrow {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #14B8A6;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}
.section-eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px; height: 1.5px;
    background: #14B8A6;
}

/* ── Experience Card ── */
.exp-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    margin-bottom: 20px;
    overflow: hidden;
    backdrop-filter: blur(12px);
    box-shadow: 0 2px 8px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.05);
    transition: border-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}
.exp-card:hover {
    border-color: rgba(168,85,247,0.3);
    transform: translateY(-2px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.4), 0 0 0 1px rgba(168,85,247,0.1);
}

.exp-card-header {
    padding: 20px 28px;
    background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(20,184,166,0.08));
    border-bottom: 1px solid rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
}
.exp-card-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(124,58,237,0.05) 0%, transparent 60%);
}

.exp-company {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    color: #F1F5F9;
    margin: 0 0 8px 0;
    letter-spacing: -0.3px;
    position: relative;
}

.exp-role-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(168,85,247,0.15);
    border: 1px solid rgba(168,85,247,0.3);
    color: #C084FC;
    border-radius: 50px;
    padding: 3px 14px;
    font-size: 0.8rem;
    font-weight: 500;
    position: relative;
}

.exp-card-body { padding: 20px 28px 24px; }

.exp-meta {
    display: flex;
    align-items: center;
    gap: 16px;
    font-size: 0.83rem;
    color: #64748B;
    margin-bottom: 18px;
    flex-wrap: wrap;
}
.exp-location { color: #94A3B8; }
.exp-dates {
    color: #A855F7;
    font-weight: 600;
    font-family: 'Space Grotesk', sans-serif;
}
.exp-divider {
    width: 4px; height: 4px;
    background: #334155;
    border-radius: 50%;
}

/* ── Highlights box ── */
.highlights-box {
    background: rgba(168,85,247,0.04);
    border: 1px solid rgba(168,85,247,0.12);
    border-left: 3px solid #7C3AED;
    border-radius: 10px;
    padding: 16px 18px 14px 20px;
    margin-bottom: 18px;
}
.highlights-label {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #A855F7;
    margin-bottom: 10px;
}
.highlight-item {
    display: flex;
    gap: 10px;
    margin-bottom: 8px;
    font-size: 0.88rem;
    line-height: 1.65;
    color: #94A3B8;
}
.highlight-title {
    color: #14B8A6;
    font-weight: 600;
    white-space: nowrap;
    flex-shrink: 0;
}

/* ── Skill badges ── */
.skills-label {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #A855F7;
    margin-bottom: 10px;
}
.skill-badge {
    display: inline-block;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    color: #CBD5E1;
    border-radius: 6px;
    padding: 4px 12px;
    margin: 3px 4px 3px 0;
    font-size: 0.78rem;
    font-weight: 500;
    transition: border-color 0.2s, color 0.2s;
}
.skill-badge:hover {
    border-color: rgba(168,85,247,0.4);
    color: #E2E8F0;
}

@media (max-width: 700px) {
    [data-testid="block-container"] { padding: 1.5rem 1rem 2rem !important; }
    .exp-card-header, .exp-card-body { padding-left: 18px; padding-right: 18px; }
}
</style>
""", unsafe_allow_html=True)


# ─── Page Header ───────────────────────────────────
st.markdown("""
<div style="margin-bottom: 2.5rem;">
    <div class="section-eyebrow">Career</div>
    <h1 style="
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2rem, 5vw, 2.8rem);
        font-weight: 700;
        color: #F8FAFC;
        letter-spacing: -1px;
        margin: 0 0 8px 0;
        line-height: 1.1;
    ">Experience Timeline</h1>
    <p style="color: #64748B; font-size: 0.95rem; font-weight: 400; margin:0;">
        A journey through professional milestones
    </p>
</div>
""", unsafe_allow_html=True)


# ─── Load Data ─────────────────────────────────────
data = JsonImporter.load_data_from_file("./data/experience.json")

for exp in data:

    highlights_html = ""
    for h in exp["highlights"]:
        highlights_html += f"""
        <div class="highlight-item">
            <span class="highlight-title">{h['title']}</span>
            <span style="color:#475569;">—</span>
            <span>{h['description']}</span>
        </div>
        """

    skills_html = ""
    for skill in exp["skills"]:
        skills_html += f'<span class="skill-badge">{skill}</span>'

    st.html(f"""
    <div class="exp-card">
        <div class="exp-card-header">
            <div class="exp-company">🏢 {exp['company']}</div>
            <span class="exp-role-badge">{exp['role']}</span>
        </div>
        <div class="exp-card-body">
            <div class="exp-meta">
                <span class="exp-location">📍 {exp['location']}</span>
                <div class="exp-divider"></div>
                <span class="exp-dates">{exp['duration']['start']} → {exp['duration']['end']}</span>
            </div>

            <div class="highlights-box">
                <div class="highlights-label">✦ Highlights</div>
                {highlights_html}
            </div>

            <div class="skills-label">🛠 Tech Stack</div>
            <div>{skills_html}</div>
        </div>
    </div>
    """)
