from google import genai
from dotenv import load_dotenv
import os

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def study_assistant(user_prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_prompt
    )
    return response


user_question = "Explain Generative AI"

output = study_assistant(user_question)

print(output.text)
