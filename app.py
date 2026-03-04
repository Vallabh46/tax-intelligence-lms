import streamlit as st
from streamlit_option_menu import option_menu
from simulator import render_1040_simulator
from assessment import render_adaptive_assessment
from cpa_simulation import render_cpa_simulation
from content import render_chapter

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Form 1040 Mastery Lab",
    layout="wide"
)

# --------------------------------------------------
# IRS STYLE THEME
# --------------------------------------------------

st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}

h1, h2, h3 {
    color: #ffffff;
}

.stButton>button {
    background-color: #990000;
    color: white;
    border-radius: 6px;
}

.stButton>button:hover {
    background-color: #7a0000;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div style='background-color:#003366;padding:25px;border-radius:10px;'>
<h1 style='color:white;'>Form 1040 Mastery Lab</h1>
<p style='color:#f1f1f1;'>Professional Tax Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION MENU
# --------------------------------------------------

selected = option_menu(
    menu_title=None,
    options=[
        "Knowledge Studio",
        "Form 1040 Simulator",
        "Assessment",
        "CPA Simulation Lab",
        "Progress Dashboard"
    ],
    icons=["book", "file-earmark-text", "clipboard-check", "briefcase", "bar-chart"],
    orientation="horizontal"
)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# PAGE ROUTING
# --------------------------------------------------

if selected == "Knowledge Studio":
    render_chapter()
    
elif selected == "Form 1040 Simulator":
    render_1040_simulator()

elif selected == "Assessment":
    render_adaptive_assessment()

elif selected == "CPA Simulation Lab":
    render_cpa_simulation()

elif selected == "Progress Dashboard":
    st.header("Progress Dashboard")

    if "score" in st.session_state:
        st.metric("Assessment Score", st.session_state.score)
    else:
        st.info("No assessment activity yet.")