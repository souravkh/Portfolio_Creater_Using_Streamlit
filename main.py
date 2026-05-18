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

# --- SHARED ON ALL PAGES ---
st.logo("Images/bolt.svg")

# 1. Custom content at the VERY top
st.sidebar.title("Template - Portfolio")
st.sidebar.markdown("Made with [Sourav](https://github.com/souravkh)")
st.sidebar.divider()

# 2. Rebuild the navigation menu manually
st.sidebar.subheader("Info")
st.sidebar.page_link(about_me)

st.sidebar.subheader("Projects")
st.sidebar.page_link(main_content)

# 3. Hide the default forced navigation
pages = st.navigation(
    {
        "Info": [about_me],
        "Work Experience": [main_content],
    },
    position="hidden"
)
pages.run()