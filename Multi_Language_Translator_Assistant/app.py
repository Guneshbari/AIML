import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

languages = {
    "Hindi": "Translate the given sentence into Hindi.",
    "Telugu": "Translate the given sentence into Telugu.",
    "French": "Translate the given sentence into French.",
}


def language_translator(question, language):
    system_prompt = languages[language]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3,
            max_output_tokens=2000,
        ),
        contents=question,
    )
    return response.text


question = "What are LLMs?"
language = "French"
output = language_translator(question, language)
print(output)
