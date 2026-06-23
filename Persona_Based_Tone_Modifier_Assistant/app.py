import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

tones = {
    "Formal": ("Convert the given sentence in the Formal Tone.",),
    "Casual": ("Convert the given sentence in a Casual Tone.",),
}

client = genai.Client(api_key=GEMINI_API_KEY)


def study_assistant(sentence, tone):
    system_prompt = tones[tone]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            temperature=0.3, system_instruction=system_prompt, max_output_tokens=2000
        ),
        contents=sentence,
    )
    return response.text


sentence = "we are applying for the job"
tone = "Formal"
print(study_assistant(sentence, tone))
