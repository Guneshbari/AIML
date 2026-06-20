# Interactive Tone Translator

A Python web application that uses the Google GenAI SDK and Gradio to provide a user-friendly browser interface for rewriting sentences in different tones (such as Formal, Casual, Friendly, or Professional).

## Project Files

*   [app.py](./app.py): Python script containing the tone modifier logic, target tone definitions, and Gradio UI definition and launcher.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `gradio`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Interactive_Tone_Translator
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Create a `.env` file in this directory and add your Gemini API Key:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

## Usage

Run the web server:
```bash
python app.py
```

The script will launch a local server. Open the displayed URL (usually `http://127.0.0.1:7860/` or similar) in your web browser to enter a sentence, select a target tone, and see the rewritten output.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **GenAI Client**: Initializes the unified `genai.Client` SDK.
3.  **Tone Translation Logic**: The `modify_tone` function maps the selected target tone to a system prompt instruction and requests a rewritten response from the `gemini-2.5-flash` model.
4.  **Gradio Interface**: Defines a web UI using `gr.Interface` with a text area for input sentences and radio buttons for selecting target tones, then launches it.
