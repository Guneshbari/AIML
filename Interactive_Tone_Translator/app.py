import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import gradio as gr

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

tones = {
    "Formal": "Convert the given sentence into a formal tone.",
    "Casual": "Convert the given sentence into a casual tone.",
    "Friendly": "Convert the given sentence into a friendly tone.",
    "Professional": "Convert the given sentence into a professional tone.",
}


def modify_tone(sentence, tone):
    system_prompt = tones[tone]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt, temperature=0.3, max_output_tokens=2000
        ),
        contents=sentence,
    )
    return response.text


demo = gr.Interface(
    fn=modify_tone,
    inputs=[
        gr.Textbox(
            lines=4,
            placeholder="Enter a sentence to rewrite...",
            label="Input Sentence",
        ),
        gr.Radio(
            choices=list(tones.keys()), value="Formal", label="Target Tone"
        ),
    ],
    outputs=gr.Textbox(lines=6, label="Rewritten Output"),
    title="Interactive Tone Translator",
    description="Rewrite sentences in different tones using Gemini.",
)

demo.launch(server_name="0.0.0.0", root_path="/gradio")
