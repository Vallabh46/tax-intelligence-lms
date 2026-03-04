import streamlit as st
import plotly.graph_objects as go
from gpt_engine import grade_answer

# ---------------------------------------------------
# TAX BRACKET ENGINE (2024 SINGLE SIMPLIFIED)
# ---------------------------------------------------

def calculate_tax(income):

    brackets = [
        (11000, 0.10),
        (44725, 0.12),
        (95375, 0.22),
        (182100, 0.24),
        (231250, 0.32),
        (578125, 0.35),
        (float("inf"), 0.37),
    ]

    tax = 0
    prev = 0

    for limit, rate in brackets:
        if income > limit:
            tax += (limit - prev) * rate
            prev = limit
        else:
            tax += (income - prev) * rate
            break

    return tax


# ---------------------------------------------------
# STANDARD DEDUCTION BY STATUS
# ---------------------------------------------------

STANDARD_DEDUCTIONS = {
    "Single": 13850,
    "Married Filing Jointly": 27700,
    "Married Filing Separately": 13850,
    "Head of Household": 20800,
}


# ---------------------------------------------------
# MAIN SIMULATOR
# ---------------------------------------------------

def render_1040_simulator():

    st.markdown("""
    <div style="border:2px solid #003366; padding:20px; border-radius:8px;">
    <h2 style="color:#003366;">Form 1040 — Advanced Preparation Interface</h2>
    <p>Structured IRS Worksheet with Professional Validation</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # -------------------------------------------
    # FILING STATUS
    # -------------------------------------------

    st.subheader("Filing Status")

    filing_status = st.selectbox(
        "Select Filing Status",
        list(STANDARD_DEDUCTIONS.keys())
    )

    standard_deduction = STANDARD_DEDUCTIONS[filing_status]

    st.info(f"Standard Deduction for {filing_status}: ${standard_deduction:,}")

    st.markdown("---")

    # -------------------------------------------
    # INCOME SECTION
    # -------------------------------------------

    st.subheader("Income")

    wages = st.number_input("Line 1 – Wages (W-2)", min_value=0.0)
    interest = st.number_input("Line 2b – Taxable Interest", min_value=0.0)
    dividends = st.number_input("Line 3b – Dividends", min_value=0.0)
    business = st.number_input("Schedule C – Business Income", min_value=0.0)
    capital = st.number_input("Line 7 – Capital Gains", min_value=0.0)

    total_income = wages + interest + dividends + business + capital
    st.markdown(f"### Line 9 – Total Income: **${total_income:,.2f}**")

    st.markdown("---")

    # -------------------------------------------
    # ADJUSTMENTS
    # -------------------------------------------

    st.subheader("Adjustments to Income")

    adjustments = st.number_input("Schedule 1 Adjustments", min_value=0.0)

    agi = total_income - adjustments
    st.markdown(f"### Line 11 – Adjusted Gross Income: **${agi:,.2f}**")

    if adjustments > total_income:
        st.warning("Adjustments exceed income — review entries.")

    st.markdown("---")

    # -------------------------------------------
    # DEDUCTIONS
    # -------------------------------------------

    st.subheader("Deduction Layer")

    taxable_income = max(0, agi - standard_deduction)
    st.markdown(f"### Line 15 – Taxable Income: **${taxable_income:,.2f}**")

    st.markdown("---")

    # -------------------------------------------
    # TAX CALCULATION
    # -------------------------------------------

    tax = calculate_tax(taxable_income)
    st.success(f"Estimated Federal Income Tax: ${tax:,.2f}")

    # -------------------------------------------
    # FICA / SE TAX CALCULATOR
    # -------------------------------------------

    st.markdown("---")
    st.subheader("FICA / Self-Employment Tax")

    if business > 0:
        se_base = business * 0.9235
        se_tax = se_base * 0.153
        st.info(f"Estimated Self-Employment Tax: ${se_tax:,.2f}")
    else:
        fica = wages * 0.0765
        st.info(f"Estimated Employee FICA: ${fica:,.2f}")

    # -------------------------------------------
    # AUDIT RISK INDICATOR
    # -------------------------------------------

    st.markdown("---")
    st.subheader("Preliminary Risk Indicator")

    risk_score = 0

    if business > 0:
        risk_score += 1
    if capital > 50000:
        risk_score += 1
    if adjustments > 30000:
        risk_score += 1

    if risk_score == 0:
        st.success("Low Structural Audit Risk")
    elif risk_score == 1:
        st.warning("Moderate Review Risk")
    else:
        st.error("High Review Risk – Recommend Documentation")

    # -------------------------------------------
    # VISUAL TAX GRAPH
    # -------------------------------------------

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Taxable Income"],
        y=[taxable_income],
        marker_color="#003366"
    ))
    fig.update_layout(
        height=350,
        plot_bgcolor="white",
        paper_bgcolor="white",
        title="Taxable Income Visualization"
    )
    st.plotly_chart(fig)

    # -------------------------------------------
    # AI REVIEW BUTTON
    # -------------------------------------------

    st.markdown("---")
    st.subheader("AI Structural Review")

    if st.button("Run AI Review of Return"):

        summary = f"""
        Filing Status: {filing_status}
        Wages: {wages}
        Interest: {interest}
        Dividends: {dividends}
        Business: {business}
        Capital Gains: {capital}
        Adjustments: {adjustments}
        Taxable Income: {taxable_income}
        Estimated Tax: {tax}
        """

        feedback = grade_answer(summary)

        st.markdown("### Personalised Feedback")
        st.write(feedback)

    # Store results
    st.session_state["taxable_income"] = taxable_income
    st.session_state["tax"] = tax