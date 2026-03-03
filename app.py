import streamlit as st
from streamlit_option_menu import option_menu
from openai import OpenAI
import os
import plotly.graph_objects as go

# ===============================
# CONFIG
# ===============================
st.set_page_config(layout="wide")

# ===============================
# PREMIUM STYLING (Blue / White / Mustard)
# ===============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

.stApp { background-color: white; }

.block-container { padding: 2rem 5rem; }

h1,h2,h3 {
    font-family: 'Playfair Display', serif;
    color: #0B3D91 !important;
}

p {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.9;
    color: black !important;
}

.chapter-card {
    padding: 35px;
    border-radius: 15px;
    border-left: 6px solid #FFC72C;
    box-shadow: 0 15px 40px rgba(0,0,0,0.05);
    margin-bottom: 40px;
    animation: fadeIn 0.8s ease;
}

@keyframes fadeIn {
    from {opacity:0; transform: translateY(30px);}
    to {opacity:1; transform: translateY(0);}
}

.progress-ring {
    height: 200px;
    width: 200px;
    border-radius: 50%;
    background: conic-gradient(#0B3D91 var(--percent), #eee 0);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    font-weight:bold;
    color:#0B3D91;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# SESSION STATE
# ===============================
if "completed" not in st.session_state:
    st.session_state.completed = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0

# ===============================
# GPT ENGINE
# ===============================
def gpt_feedback(question, answer):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    prompt = f"""
    You are a US Tax Professor.
    Question: {question}
    Student Answer: {answer}
    Provide:
    1. Evaluation
    2. Conceptual gaps
    3. Reference specific IRS publication pages
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content

# ===============================
# NAVIGATION
# ===============================
selected = option_menu(
    None,
    ["Knowledge Studio","Assessment","Tax Simulator","Form 1040 Builder","Progress Intelligence"],
    orientation="horizontal"
)

# ===============================================================
# KNOWLEDGE STUDIO (11 CHAPTERS HARD CODED)
# ===============================================================
if selected == "Knowledge Studio":

    st.title("Income Recognition & Form 1040 Intelligence System")

    chapters = [
        "1. Form 1040 Architecture",
        "2. Accounting Periods",
        "3. Accounting Methods",
        "4. 12 Month Rule",
        "5. Information Returns",
        "6. Salaries & Wages",
        "7. FICA & SE Tax",
        "8. Social Security Taxability",
        "9. Income Exclusions",
        "10. Interest & OID",
        "11. Dividends & Passive Income"
    ]

    chapter = st.selectbox("Select Chapter", chapters)

    st.markdown("<div class='chapter-card'>", unsafe_allow_html=True)

    if chapter == "1. Form 1040 Architecture":
        st.header("Form 1040 – Structural Blueprint")
        st.write("""
Form 1040 is the master summary of an individual’s federal income tax return.
It is not merely a form but a structural consolidation point.

Schedules 1,2,3,A,B,C,D,E,F and H feed into it.
Wages flow from Form W-2.
Interest and Dividends flow from Schedule B.
Business Income from Schedule C.
Rental & K-1 from Schedule E.
Capital Gains from Schedule D.

Think of Form 1040 as the control tower of income aggregation.
""")

    elif chapter == "2. Accounting Periods":
        st.header("Accounting Period Framework")
        st.write("""
An accounting period defines the reporting cycle of income.
Individuals follow calendar year.
Businesses may adopt fiscal year.
Short year applies in formation or dissolution.

This timing defines recognition boundaries.
""")

    elif chapter == "3. Accounting Methods":
        st.header("Cash vs Accrual vs Hybrid")
        st.write("""
Cash Method: Income recognized when received.
Accrual Method: Income recognized when earned.
Hybrid: Combination.

Constructive receipt doctrine ensures income is taxable when available.
Refer IRS Publication 538.
""")

    elif chapter == "4. 12 Month Rule":
        st.header("Prepaid Expense Deduction Rule")
        st.write("""
Cash taxpayers may deduct prepaid expense only if benefit does not extend beyond 12 months AND end of next tax year.
""")

    elif chapter == "5. Information Returns":
        st.header("1099 & W2 Reporting Architecture")
        st.write("""
1099-NEC: Non employee compensation.
1099-MISC: Rent, royalty.
1099-INT: Interest.
1099-DIV: Dividends.
W2: Wage reporting.
""")

    elif chapter == "6. Salaries & Wages":
        st.header("Employee vs Non Employee Compensation")
        st.write("""
W2 income subject to FICA.
1099 income subject to SE tax.
Tip income taxable.
""")

    elif chapter == "7. FICA & SE Tax":
        st.header("FICA vs Self Employment")
        st.write("""
FICA = 7.65% employee + 7.65% employer.
SE tax = 15.3%.
92.35% adjustment ensures employer equivalent deduction.
Refer IRS Publication 334.
""")

    elif chapter == "8. Social Security Taxability":
        st.header("Provisional Income Calculation")
        st.write("""
Provisional Income = AGI + Tax exempt interest + 1/2 SS.
Up to 85% taxable depending on threshold.
Refer IRS Publication 915.
""")

    elif chapter == "9. Income Exclusions":
        st.header("Non Taxable Income")
        st.write("""
Gifts, inheritance, life insurance proceeds,
Foreign earned income exclusion,
Certain healthcare distributions.
""")

    elif chapter == "10. Interest & OID":
        st.header("OID & De Minimis Rule")
        st.write("""
OID taxable as it accrues.
De minimis = 1/4 of 1% × face × years.
Refer IRS Publication 550.
""")

    elif chapter == "11. Dividends & Passive Income":
        st.header("Qualified Dividend & Passive Rules")
        st.write("""
Qualified dividends taxed at capital gain rates.
Rental income generally passive.
QBI deduction subject to phaseouts.
Refer IRS Publication 535.
""")

    if st.button("Mark Chapter Complete"):
        if chapter not in st.session_state.completed:
            st.session_state.completed.append(chapter)

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================================================
# ASSESSMENT (MCQ + GPT GRADING)
# ===============================================================
elif selected == "Assessment":

    st.title("Comprehensive Income Assessment Engine")

    # ---------------------------
    # MCQ DATABASE (Your Questions)
    # ---------------------------
    mcqs = [
        {
            "question": "Which of the following types of income is always taxable?",
            "options": [
                "Municipal bond interest",
                "Child support received",
                "Tips reported to the employer",
                "Life insurance proceeds upon death"
            ],
            "answer": "Tips reported to the employer",
            "explanation": "Tips are taxable and must be reported as income."
        },
        {
            "question": "Which of the following interest income is tax-exempt at the federal level?",
            "options": [
                "Corporate bond interest",
                "Bank savings interest",
                "U.S. Treasury bond interest",
                "Municipal bond interest"
            ],
            "answer": "Municipal bond interest",
            "explanation": "Municipal bond interest is generally exempt from federal income tax."
        },
        {
            "question": "Qualified dividends are taxed at which rate for most taxpayers?",
            "options": [
                "Same as ordinary income",
                "10%",
                "15%",
                "25%"
            ],
            "answer": "15%",
            "explanation": "Qualified dividends are taxed at 0%, 15%, or 20% depending on income."
        },
        {
            "question": "Under constructive receipt doctrine, income is taxable when:",
            "options": [
                "The taxpayer receives the check",
                "The taxpayer deposits the check",
                "The income is earned regardless of receipt",
                "The income is available and controlled by the taxpayer"
            ],
            "answer": "The income is available and controlled by the taxpayer",
            "explanation": "Income is taxable when it is credited or made available without restriction."
        },
        {
            "question": "Gambling winnings must be reported:",
            "options": [
                "Only if over $600",
                "Only if reported on Form W-2G",
                "In all cases, regardless of amount",
                "Only if net winnings exceed $5,000"
            ],
            "answer": "In all cases, regardless of amount",
            "explanation": "All gambling winnings are taxable even if no form is issued."
        }
    ]

    # ---------------------------
    # SESSION STATE TRACKING
    # ---------------------------
    if "mcq_score" not in st.session_state:
        st.session_state.mcq_score = 0
    if "mcq_answered" not in st.session_state:
        st.session_state.mcq_answered = {}

    # ---------------------------
    # DISPLAY QUESTIONS
    # ---------------------------
    for idx, q in enumerate(mcqs):

        st.markdown("---")
        st.subheader(f"Question {idx + 1}")
        st.write(q["question"])

        user_choice = st.radio(
            "Select your answer:",
            q["options"],
            key=f"q_{idx}"
        )

        if st.button("Submit Answer", key=f"submit_{idx}"):

            st.session_state.mcq_answered[idx] = True

            if user_choice == q["answer"]:
                st.success("Correct")
                st.session_state.mcq_score += 1
            else:
                st.error(f"Incorrect. Correct Answer: {q['answer']}")

            st.info(q["explanation"])

    # ---------------------------
    # FINAL SCORE
    # ---------------------------
    if len(st.session_state.mcq_answered) == len(mcqs):

        percentage = (st.session_state.mcq_score / len(mcqs)) * 100

        st.markdown("## Final Score")
        st.write(f"Score: {st.session_state.mcq_score} / {len(mcqs)}")
        st.write(f"Percentage: {percentage:.2f}%")

        if percentage < 50:
            st.warning("Refer IRS Publication 17 and 538 for revision.")
        elif percentage < 80:
            st.info("Good understanding. Review weaker areas.")
        else:
            st.success("Excellent mastery demonstrated.")

    st.title("Adaptive Assessment Engine")

    question = "Explain constructive receipt doctrine."
    answer = st.text_area("Your Answer")

    if st.button("Submit for Evaluation"):
        feedback = gpt_feedback(question, answer)
        st.subheader("Personalised Feedback")
        st.write(feedback)

# ===============================================================
# TAX SIMULATOR
# ===============================================================
elif selected == "Tax Simulator":

    st.title("Interactive Tax Computation Simulator")

    wages = st.number_input("Wages")
    business = st.number_input("Business Income")
    interest = st.number_input("Interest Income")

    total_income = wages + business + interest

    st.metric("Total Income", total_income)

# ===============================================================
# FORM 1040 BUILDER
# ===============================================================
elif selected == "Form 1040 Builder":

    st.title("Interactive Form 1040 Builder")

    st.markdown("### Enter Income Details")

    wages = st.number_input("Line 1: Wages (W-2)", min_value=0.0)
    interest = st.number_input("Line 2b: Taxable Interest", min_value=0.0)
    dividends = st.number_input("Line 3b: Ordinary Dividends", min_value=0.0)
    capital_gain = st.number_input("Line 7: Capital Gain", min_value=0.0)
    additional_income = st.number_input("Line 8: Additional Income (Schedule 1)", min_value=0.0)

    correct_total_income = wages + interest + dividends + capital_gain + additional_income

    st.markdown("### Student Computation")

    student_total_income = st.number_input("Line 9: Total Income (Student Entry)", min_value=0.0)

    standard_deduction = st.number_input("Line 12: Standard Deduction", min_value=0.0)

    student_taxable_income = st.number_input("Line 15: Taxable Income (Student Entry)", min_value=0.0)

    correct_taxable_income = max(correct_total_income - standard_deduction, 0)

    st.markdown("## Validation Results")

    # Validate Total Income
    if student_total_income == correct_total_income:
        st.success("Line 9 Total Income is Correct")
    else:
        st.error(f"Line 9 Incorrect. Correct Value: {correct_total_income}")

    # Validate Taxable Income
    if student_taxable_income == correct_taxable_income:
        st.success("Line 15 Taxable Income is Correct")
    else:
        st.error(f"Line 15 Incorrect. Correct Value: {correct_taxable_income}")

    st.markdown("---")
    st.markdown("### Conceptual Explanation")

    if student_total_income != correct_total_income:
        st.warning("Review aggregation rules under Form 1040 Instructions Page 23.")
    elif student_taxable_income != correct_taxable_income:
        st.warning("Review Standard Deduction computation – IRS Publication 17.")
    else:
        st.success("Strong structural understanding of Form 1040 computation.")

    st.title("Visual Form 1040 Flow Builder")

    fig = go.Figure(go.Sankey(
        node = dict(label=["W2","Schedule C","Schedule B","Form 1040"]),
        link = dict(
            source=[0,1,2],
            target=[3,3,3],
            value=[1,1,1]
        )))

    st.plotly_chart(fig)

# ===============================================================
# PROGRESS INTELLIGENCE
# ===============================================================
elif selected == "Progress Intelligence":

    st.title("Performance Analytics")

    total_chapters = 11
    percent = int((len(st.session_state.completed)/total_chapters)*100)

    st.markdown(
        f"<div class='progress-ring' style='--percent:{percent}%;'>{percent}%</div>",
        unsafe_allow_html=True
    )

    st.write(f"Completed: {len(st.session_state.completed)} / {total_chapters}")

    if percent < 40:
        st.warning("Refer IRS Publication 538 & 334 for foundational clarity.")
    elif percent < 80:
        st.info("Review IRS Publication 550 & 915 for conceptual reinforcement.")
    else:
        st.success("Strong mastery demonstrated.")
