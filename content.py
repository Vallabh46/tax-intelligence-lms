import streamlit as st

def render_chapter():

    st.header("Form 1040 – Structural Intelligence of U.S. Taxation")

    with st.expander("I. The Architecture of Gross Income", expanded=True):
        st.markdown("""
Form 1040 is not merely a compliance document. It is the architectural convergence point of all economic activity recognized under the Internal Revenue Code.

Under IRC §61, gross income includes *“all income from whatever source derived.”* This principle establishes a presumption of inclusion. Income is taxable unless a statutory exclusion applies.

This means taxation begins with classification — not calculation.

Wages flow through Line 1.  
Interest flows through Schedule B.  
Business income flows through Schedule C.  
Capital gains flow through Schedule D.  

Schedules compute. Form 1040 consolidates.

### Client Scenario – The Founder

“I earned $420,000 in revenue this year. Why is my taxable income lower?”

Because revenue is not taxable income.

Expenses reduce business profit.
Holding period affects capital gains rates.
Dividends may qualify for preferential treatment.
Interest is taxed at ordinary rates.

Taxation is structural law applied to economic reality.
""")

    with st.expander("II. Timing & Recognition Doctrine"):
        st.markdown("""
Income is taxed when recognized.

Cash Method → taxed when received.  
Accrual Method → taxed when earned.  

Constructive receipt doctrine taxes income when it is made available without restriction.

### Client Scenario – The Consultant

“I deposited the check in January.”

But the check was available in December.

Recognition is based on availability, not convenience.
""")

    with st.expander("III. AGI – The Structural Filter"):
        st.markdown("""
Adjusted Gross Income is not cosmetic.

It determines:

• Phase-outs  
• Social Security taxation  
• Additional Medicare thresholds  
• Investment surtaxes  

Cross structural thresholds — consequences activate.

### Client Scenario – Dual Earners

“We earned more but received fewer credits.”

Because AGI exceeded statutory limits.
""")

    with st.expander("IV. Deduction Layer"):
        st.markdown("""
Standard deduction simplifies compliance.
Itemized deduction personalizes structure.

Taxable income is post-architecture residue.

Tax is not applied to revenue.
Tax is applied to structured taxable income.
""")

    with st.expander("V. Advisory Intelligence"):
        st.markdown("""
A preparer inputs numbers.

An advisor understands architecture.

Form 1040 reveals structural intelligence:
Classification.
Recognition.
Threshold activation.
Rate application.

Mastery of Form 1040 is mastery of tax law architecture.
""")