import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

question_types = {
    "MCQs": "Generate MCQs on the given content",
    "Short Answer": "Generate Short Answer Questions on the given content",
    "Interview": "Generate Short Answer Questions on the given content",
}


def question_generator(content, q_type):
    system_prompt = question_types[q_type]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, temperature=0.4, max_output_tokens=2000
        ),
        contents=content,
    )
    return response.text


content = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum."
q_type = "Short Answer"
output = question_generator(content, q_type)
print(output)
