# code copied from here: https://ai.google.dev/gemini-api/docs/text-generation#python_2
#initialize on terminal: npm init
# on terminal: npm i @google/genai
#api key from: AIzaSyDUw4tDg0XGudVlWf6p-bZQpe7NYzkHkLQ

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_INSTRUCTION = (
    "You are a DSA instructor. Answer only questions related to "
    "Data Structures and Algorithms. Explain concepts simply, "
    "use examples if needed, and provide a short quiz after each explanation. "
    "Politely refuse non-DSA questions."
)

def get_response(user_input: str) -> str:
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=user_input,
        system_instruction=SYSTEM_INSTRUCTION
    )
    return response.text

