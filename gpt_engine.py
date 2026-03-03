from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def grade_answer(question, student_answer):
    prompt = f"""
    You are a US tax instructor.

    Question:
    {question}

    Student Answer:
    {student_answer}

    Grade the answer out of 10.
    Identify conceptual weaknesses.
    Recommend specific IRS Publication references.
    Be precise and professional.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
