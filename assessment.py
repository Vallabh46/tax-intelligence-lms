import streamlit as st
import random
import plotly.graph_objects as go
from gpt_engine import grade_answer

# ----------------------------------------------------
# QUESTION DATABASE (STRUCTURED WITH TOPIC TAGS)
# ----------------------------------------------------

QUESTION_BANK = [
    {
        "question": "Are tips reported to an employer taxable income?",
        "options": ["Yes", "No"],
        "correct": 0,
        "difficulty": 1,
        "topic": "Wages",
        "irs_pub": "Publication 17",
        "link": "https://www.irs.gov/publications/p17"
    },
    {
        "question": "Is municipal bond interest federally taxable?",
        "options": ["Yes", "No"],
        "correct": 1,
        "difficulty": 1,
        "topic": "Interest",
        "irs_pub": "Publication 550",
        "link": "https://www.irs.gov/publications/p550"
    },
    {
        "question": "Are gambling winnings taxable even if no Form W-2G is issued?",
        "options": ["Yes", "No"],
        "correct": 0,
        "difficulty": 2,
        "topic": "Other Income",
        "irs_pub": "Publication 525",
        "link": "https://www.irs.gov/publications/p525"
    },
    {
        "question": "Does constructive receipt doctrine tax income when available but not withdrawn?",
        "options": ["Yes", "No"],
        "correct": 0,
        "difficulty": 2,
        "topic": "Accounting Method",
        "irs_pub": "Publication 538",
        "link": "https://www.irs.gov/publications/p538"
    },
    {
        "question": "Is self-employment income subject to SE tax?",
        "options": ["Yes", "No"],
        "correct": 0,
        "difficulty": 3,
        "topic": "Self Employment",
        "irs_pub": "Schedule SE Instructions",
        "link": "https://www.irs.gov/forms-pubs/about-schedule-se-form-1040"
    },
]

# ----------------------------------------------------
# ADAPTIVE ASSESSMENT ENGINE
# ----------------------------------------------------

def render_adaptive_assessment():

    st.header("Adaptive Assessment Lab")

    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.performance = []
        st.session_state.level = 1
        st.session_state.current_question = None

    # Select next question based on difficulty weighting
    if st.session_state.current_question is None:

        weighted_questions = [
            q for q in QUESTION_BANK
            if q["difficulty"] == st.session_state.level
        ]

        if not weighted_questions:
            weighted_questions = QUESTION_BANK

        st.session_state.current_question = random.choice(weighted_questions)

    q = st.session_state.current_question

    st.subheader(f"Difficulty Level: {st.session_state.level}")

    answer = st.radio(q["question"], q["options"])

    if st.button("Submit Answer"):

        correct = q["options"].index(answer) == q["correct"]

        if correct:
            st.success("Correct.")
            st.session_state.score += 1
            st.session_state.level = min(3, st.session_state.level + 1)
        else:
            st.error("Incorrect.")
            st.session_state.level = max(1, st.session_state.level - 1)

            st.markdown(f"""
            **Recommended IRS Publication:**  
            [{q['irs_pub']}]({q['link']})
            """)

        # AI EXPLANATION
        explanation_prompt = f"""
        Explain why the correct answer to this tax question is correct:

        Question: {q['question']}
        Correct Answer: {q['options'][q['correct']]}

        Keep explanation concise and reference relevant IRS doctrine.
        """

        ai_feedback = grade_answer(explanation_prompt)

        st.markdown("### AI Explanation")
        st.write(ai_feedback)

        # Track performance
        st.session_state.performance.append({
            "topic": q["topic"],
            "correct": correct,
            "difficulty": q["difficulty"]
        })

        st.session_state.current_question = None
        st.experimental_rerun()