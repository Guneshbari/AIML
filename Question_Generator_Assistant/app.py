from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def question_generator(user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_prompt
    )
    return response


text = input()
prompt = f"Generate questions from the following content:\n{text}"

output = question_generator(prompt)

print(output.text)
