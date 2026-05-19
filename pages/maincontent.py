import streamlit as st
from utils.jsonimport import JsonImporter

# -----------------------------
# Streamlit page config
# -----------------------------
st.set_page_config(
    page_title="Experience",
    page_icon="👨‍💻",
    layout="wide"
)

# -----------------------------
# Global styles + Google Fonts
# -----------------------------
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Code:ital,wght,MONO@0,300..800,1;1,300..800,1&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <style>
        /* Apply Roboto globally */
        html, body, [class*="css"], [data-testid] {
            font-family: 'Roboto', sans-serif !important;
        }

        /* Page background */
        [data-testid="stAppViewContainer"] {
            background-color: #FFFFFF;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #FAFAFA;
            border-right: 1px solid #E4E4E7;
        }

        [data-testid="block-container"] {
            background-color: transparent;
            padding-top: 2rem;
        }

        /* Override Streamlit default h1 */
        h1 {
            font-family: 'Roboto', sans-serif !important;
        }
    </style>
""", unsafe_allow_html=True)


# -----------------------------
# Page Title  (Roboto font with Orange Accent)
# -----------------------------
st.markdown("""
<div style="text-align: center; margin-bottom: 2.5rem;">
    <h1 style="
        font-family: 'Roboto', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        color: #09090B;
        margin-bottom: 6px;
        letter-spacing: -0.8px;
    ">💼 Experience Timeline</h1>
    <p style="
        font-family: 'Roboto', sans-serif;
        color: #71717A;
        font-size: 1rem;
        font-weight: 300;
        letter-spacing: 0.5px;
    ">A journey through professional milestones</p>
    <div style="
        width: 60px;
        height: 3px;
        background: #FF5F1F;
        border-radius: 2px;
        margin: 12px auto 0;
    "></div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Load experience JSON
# -----------------------------
data = JsonImporter.load_data_from_file("./data/experience.json")


for exp in data:

    # Build highlights list items
    highlights_html = ""
    for h in exp["highlights"]:
        highlights_html += f"""
            <li style="
                margin-bottom: 10px;
                color: #27272A;
                line-height: 1.75;
                font-family: 'Roboto', sans-serif;
                font-size: 0.93rem;
            ">
                <span style="
                    font-family: 'Google Sans Code', monospace;
                    color: #EA580C;
                    font-weight: 600;
                ">{h['title']}</span>
                <span style="color: #FFEDD5;"> &mdash; </span>
                {h['description']}
            </li>
        """

    # Build skill badges
    skills_badges = ""
    for skill in exp["skills"]:
        skills_badges += f"""
            <span style="
                display: inline-block;
                background: #F4F4F5;
                color: #18181B;
                border: 1px solid #E4E4E7;
                border-radius: 6px;
                padding: 4px 14px;
                margin: 4px 5px 4px 0;
                font-size: 0.80rem;
                font-weight: 500;
                font-family: 'Roboto', sans-serif;
                letter-spacing: 0.2px;
            ">{skill}</span>
        """

    st.html(f"""
    <div style="
        background: #FFFFFF;
        border: 1px solid #E4E4E7;
        border-radius: 8px;
        margin-bottom: 24px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        overflow: hidden;
    ">
        <!-- Minimalist top banner -->
        <div style="
            background: #18181B;
            padding: 18px 28px;
        ">
            <h2 style="
                margin: 0 0 6px 0;
                color: #FFFFFF;
                font-size: 1.4rem;
                font-weight: 700;
                font-family: 'Roboto', sans-serif;
                letter-spacing: -0.3px;
            ">🏢 {exp['company']}</h2>
            <span style="
                display: inline-block;
                background: #FFF7ED;
                color: #EA580C;
                border: 1px solid #FFEDD5;
                border-radius: 6px;
                padding: 2px 12px;
                font-size: 0.85rem;
                font-family: 'Roboto', sans-serif;
                font-weight: 500;
            ">{exp['role']}</span>
        </div>

        <!-- Card body -->
        <div style="padding: 20px 28px 24px;">

            <!-- Location & Duration -->
            <p style="
                color: #71717A;
                font-size: 0.88rem;
                margin-bottom: 18px;
                font-family: 'Roboto', sans-serif;
            ">
                📍 <span style="color: #475569;">{exp['location']}</span>
                &nbsp;&nbsp;|&nbsp;&nbsp;
                🗓️ <b style="color: #FF5F1F;">{exp['duration']['start']}</b>
                &nbsp;→&nbsp;
                <b style="color: #FF5F1F;">{exp['duration']['end']}</b>
            </p>

            <!-- Highlights -->
            <div style="
                background: #FAFAFA;
                border: 1px solid #E4E4E7;
                border-left: 3px solid #FF5F1F;
                border-radius: 6px;
                padding: 14px 18px 14px 20px;
                margin-bottom: 18px;
            ">
                <p style="
                    color: #FF5F1F;
                    font-size: 0.72rem;
                    text-transform: uppercase;
                    letter-spacing: 1.5px;
                    margin-bottom: 10px;
                    font-weight: 700;
                    font-family: 'Roboto', sans-serif;
                ">✦ Highlights</p>
                <ul style="margin: 0; padding-left: 18px;">
                    {highlights_html}
                </ul>
            </div>

            <!-- Skills -->
            <p style="
                color: #FF5F1F;
                font-size: 0.72rem;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                margin-bottom: 10px;
                font-weight: 700;
                font-family: 'Roboto', sans-serif;
            ">🛠 Tech Skills</p>
            <div>{skills_badges}</div>

        </div>
    </div>
    """)

    st.write("")  # spacing
