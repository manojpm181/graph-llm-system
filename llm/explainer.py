from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_result(question, df):
    prompt = f"""
You are a business analyst.

User Question:
{question}

SQL Result:
{df.to_string(index=False)}

Rules:
- Be concise
- Use ONLY actual values
- No assumptions
- No fake examples

Give 2-3 key insights.
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    return res.choices[0].message.content