import streamlit as st
import base64
import os
from utils.jsonimport import JsonImporter

# -----------------------------
# Streamlit page config
# -----------------------------
st.set_page_config(
    page_title="About Me",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed"   # starts collapsed; CSS hides toggle on mobile
)

data = JsonImporter.load_data_from_file("./data/myinfo.json")

# Serve the PDF file statically from Streamlit
resume_file_name = data.get("profile", {}).get("resume", {}).get("file_name", "Resume.pdf")
static_resume_path = os.path.join("static", resume_file_name)

if os.path.exists(static_resume_path):
    resume_url = f"app/static/{resume_file_name}"
    resume_tag = f'''<a href="{resume_url}" download="{resume_file_name}" target="_blank" style="text-decoration: none;">
        <span style="
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(135deg, #6366F1, #A855F7);
            color: #FFFFFF;
            border-radius: 25px;
            padding: 9px 22px;
            font-size: 0.88rem;
            font-weight: 600;
            font-family: 'Roboto', sans-serif;
            box-shadow: 0 3px 12px rgba(99, 102, 241, 0.25);
            letter-spacing: 0.3px;
            white-space: nowrap;
            cursor: pointer;
        ">📄 Download Resume</span>
    </a>'''
else:
    resume_tag = "<span style='color:#94A3B8; font-size:0.85rem; display:inline-flex; align-items:center;'>Resume not available</span>"
# -----------------------------
# Global styles + Google Fonts + Responsive CSS
# -----------------------------
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Code:ital,wght,MONO@0,300..800,1;1,300..800,1&family=Playwrite+NO:wght@100..400&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <style>
        html, body, [class*="css"], [data-testid] {
            font-family: 'Roboto', sans-serif !important;
        }
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #F0F4FF 0%, #FAF5FF 100%);
        }
        [data-testid="stSidebar"] {
            background-color: #FFFFFF;
            border-right: 1px solid #E5E7EB;
        }
        [data-testid="block-container"] {
            background-color: transparent;
            padding-top: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        /* ── Responsive: Tablet (≤ 900px) ── */
        @media (max-width: 900px) {
            [data-testid="block-container"] {
                padding-left: 1rem;
                padding-right: 1rem;
            }
            /* Stack columns vertically on tablet */
            [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
            }
            [data-testid="stColumn"] {
                width: 100% !important;
                min-width: 100% !important;
                flex: 1 1 100% !important;
            }
        }

        /* ── Responsive: Mobile (≤ 600px) ── */
        @media (max-width: 600px) {
            [data-testid="block-container"] {
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }
            .about-card-body {
                padding: 14px 16px 18px !important;
            }
        }

        /* ── Mobile only (≤ 500px) ── */
        @media (max-width: 500px) {
            /* Force the first column's internal container to center the profile image */
            [data-testid="stColumn"]:first-of-type [data-testid="element-container"] {
                display: flex !important;
                justify-content: center !important;
                width: 100% !important;
            }
            /* Control profile image — cap at 120px */
            [data-testid="stImage"] {
                display: flex !important;
                justify-content: center !important;
                margin: 0 auto !important;
            }
            [data-testid="stImage"] img {
                margin: 0 auto !important;
                display: block !important;
                max-width: 120px !important;
                width: 120px !important;
                height: auto !important;
                border-radius: 12px;
            }
        }
    </style>
""", unsafe_allow_html=True)


# -----------------------------
# Hero Section — Profile + Name
# -----------------------------
col1, col2 = st.columns([1, 2.5], gap="large", vertical_alignment="center")

with col1:
    st.image(data["profile"]["profile_image"], width=180)  # fixed width; CSS caps it on mobile

with col2:
    st.html(f"""
    <div style="padding: 10px 0;">
        <h2 style="
            font-family: 'Roboto', sans-serif;
            font-size: clamp(1.4rem, 4vw, 2rem);
            font-weight: 700;
            color: #1E293B;
            margin-bottom: 6px;
        ">{data['profile']['name']}</h2>

        <span style="
            display: inline-block;
            background: linear-gradient(135deg, #6366F1, #A855F7);
            color: #FFFFFF;
            border-radius: 20px;
            padding: 4px 18px;
            font-size: clamp(0.78rem, 2vw, 0.9rem);
            font-family: 'Roboto', sans-serif;
            font-weight: 500;
            margin-bottom: 14px;
        ">{data['profile']['title']}</span>

        <p style="
            font-family: 'Roboto', sans-serif;
            color: #64748B;
            font-size: clamp(0.85rem, 2vw, 0.97rem);
            font-weight: 300;
            line-height: 1.7;
            margin-top: 10px;
        ">{data['profile']['short_summary']}</p>
    </div>
    """)

    # -----------------------------
    # Social Buttons — Left aligned, inside col2
    # -----------------------------
    st.html(f"""
    <div style="
        padding: 6px 0 10px 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        gap: 12px;
    ">
        <!-- LinkedIn -->
        <a href="{data['profile']['contact']['linkedin']['url']}" target="_blank" style="text-decoration: none;">
            <span style="
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: linear-gradient(135deg, #0077B5, #0A66C2);
                color: #FFFFFF;
                border-radius: 25px;
                padding: 9px 22px;
                font-size: 0.88rem;
                font-weight: 600;
                font-family: 'Roboto', sans-serif;
                box-shadow: 0 3px 12px rgba(0, 119, 181, 0.25);
                letter-spacing: 0.3px;
                white-space: nowrap;
            ">🔗 LinkedIn</span>
        </a>

        <!-- GitHub -->
        <a href="{data['profile']['contact']['github']['url']}" target="_blank" style="text-decoration: none;">
            <span style="
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: linear-gradient(135deg, #24292e, #040d14);
                color: #FFFFFF;
                border-radius: 25px;
                padding: 9px 22px;
                font-size: 0.88rem;
                font-weight: 600;
                font-family: 'Roboto', sans-serif;
                box-shadow: 0 3px 12px rgba(36, 41, 46, 0.25);
                letter-spacing: 0.3px;
                white-space: nowrap;
            ">
                <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor">
                  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
                GitHub
            </span>
        </a>

        <!-- Email -->
        <a href="{data['profile']['contact']['mailto']}" style="text-decoration: none;">
            <span style="
                display: inline-flex;
                align-items: center;
                gap: 8px;
                background: linear-gradient(135deg, #EA4335, #C5221F);
                color: #FFFFFF;
                border-radius: 25px;
                padding: 9px 22px;
                font-size: 0.88rem;
                font-weight: 600;
                font-family: 'Roboto', sans-serif;
                box-shadow: 0 3px 12px rgba(234, 67, 53, 0.25);
                letter-spacing: 0.3px;
                white-space: nowrap;
            ">✉️ Email Me</span>
        </a>
        {resume_tag}

        
    </div>
    """)

# ── Styled Download Button ──
   

st.write("")