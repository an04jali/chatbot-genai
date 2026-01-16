# code copied from here: https://ai.google.dev/gemini-api/docs/text-generation#python_2
#initialize on terminal: npm init
# on terminal: npm i @google/genai
#api key from: AIzaSyDUw4tDg0XGudVlWf6p-bZQpe7NYzkHkLQ

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables (local only)
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# System instruction
SYSTEM_INSTRUCTION = (
    "You are a DSA instructor. Answer only questions related to "
    "Data Structures and Algorithms. Explain concepts simply, "
    "use examples if needed, and provide a short quiz after each explanation. "
    "Politely refuse non-DSA questions."
)

# Create model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    system_instruction=SYSTEM_INSTRUCTION
)

def get_response(user_input: str) -> str:
    response = model.generate_content(user_input)
    return response.text
