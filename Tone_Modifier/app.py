from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def modify_tone(user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_prompt
    )

    return response


output = modify_tone("Translate its tone to formal: 'Knowledge is power.'")
print(output.text)
