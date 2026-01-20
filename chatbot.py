# code copied from here: https://ai.google.dev/gemini-api/docs/text-generation#python_2
#initialize on terminal: npm init
# on terminal: npm i @google/genai
#api key from: AIzaSyDUw4tDg0XGudVlWf6p-bZQpe7NYzkHkLQ


import os
from dotenv import load_dotenv
from groq import Groq

# 🔥 THIS LINE IS CRITICAL
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a DSA Instructor.
Only answer Data Structures & Algorithms questions.
Explain simply with examples.
Politely refuse non-DSA questions.
"""

def get_response(user_input):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content
