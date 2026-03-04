import streamlit as st
from gpt_engine import grade_answer
import plotly.graph_objects as go

def render_cpa_simulation():

    st.header("CPA Simulation Lab")

    st.markdown("""
    ### Case Scenario – Individual Return with Mixed Income

    **Client Narrative**

    “My name is Daniel Carter. I am 32 years old and live in Austin, Texas.
    I work as a software engineer, but I also started freelancing last year.
    I received a few 1099 forms and also sold some stocks.
    I just want to make sure everything is reported properly.
    I don't want trouble with the IRS.”

    ---
    """)

    st.subheader("Exhibit A – W-2 Summary")
    st.info("Wages: $95,000")

    st.subheader("Exhibit B – 1099-NEC")
    st.info("Freelance Income: $28,000")

    st.subheader("Exhibit C – 1099-DIV")
    st.info("Ordinary Dividends: $3,000")

    st.subheader("Exhibit D – 1099-B")
    st.info("Long-Term Capital Gain: $12,000")

    st.markdown("---")

    st.subheader("Task 1 – Compute Total Income")

    wages = 95000
    freelance = 28000
    dividends = 3000
    capital_gain = 12000

    total_income = wages + freelance + dividends + capital_gain

    st.success(f"Total Income = ${total_income:,}")

    st.markdown("---")

    st.subheader("Task 2 – Compute Self-Employment Tax")

    se_base = freelance * 0.9235
    se_tax = se_base * 0.153

    st.success(f"Estimated Self-Employment Tax = ${se_tax:,.2f}")

    st.markdown("---")

    st.subheader("Task 3 – Written Advisory Analysis")

    advisory_response = st.text_area(
        "Explain how this income should flow through Form 1040. Identify schedules involved and tax implications.",
        height=200
    )

    if st.button("Submit Advisory for AI Review"):

        prompt = f"""
        Evaluate the following CPA candidate advisory response.
        Provide structured feedback, identify missing schedules,
        incorrect reasoning, and suggest IRS publications for improvement.

        Case Facts:
        Wages 95000
        Freelance 28000
        Dividends 3000
        Capital Gain 12000

        Student Response:
        {advisory_response}
        """

        feedback = grade_answer(prompt)

        st.markdown("### Personalised Feedback")
        st.write(feedback)

    st.markdown("---")

    st.subheader("Competency Radar")

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[80, 70, 60, 75],
        theta=["Income Classification", "Schedule Mapping", "Tax Computation", "Documentation Awareness"],
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False
    )

    st.plotly_chart(fig)