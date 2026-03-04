import streamlit as st

def render_dashboard():

    st.header("Competency Dashboard")

    taxable_income = st.session_state.get("taxable_income", 0)
    tax = st.session_state.get("tax", 0)
    assessment_score = st.session_state.get("assessment_score", 0)

    st.metric("Last Taxable Income Simulation", taxable_income)
    st.metric("Last Estimated Tax", tax)
    st.metric("Assessment Score", assessment_score)