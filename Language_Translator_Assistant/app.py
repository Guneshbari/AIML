from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)


def language_translator(user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_prompt
    )
    return response


output = language_translator("Translate I am a boy in hindi")
print(output.text)
