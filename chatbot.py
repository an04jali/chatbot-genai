# code copied from here: https://ai.google.dev/gemini-api/docs/text-generation#python_2
#initialize on terminal: npm init
# on terminal: npm i @google/genai
#api key from: AIzaSyDUw4tDg0XGudVlWf6p-bZQpe7NYzkHkLQ

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(user_input: str) -> str:
    prompt = f"""
You are a DSA Instructor.

Rules:
- Answer ONLY Data Structures & Algorithms questions
- Explain concepts simply
- Use examples if needed
- Add a short quiz at the end
- Politely refuse non-DSA questions

Question:
{user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
