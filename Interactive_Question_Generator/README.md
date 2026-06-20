# Interactive Question Generator

A Python web application that uses the Google GenAI SDK and Gradio to provide a user-friendly browser interface for generating various types of questions (MCQs, Short Answer, or Interview questions) from a given text input.

## Project Files

*   [app.py](./app.py): Python script containing question generator helper logic and Gradio UI definition and launcher.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `gradio`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Interactive_Question_Generator
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

The script will launch a local server. Open the displayed URL (usually `http://127.0.0.1:7860/` or similar) in your web browser to paste study content, select a question type, and see the generated questions.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **GenAI Client**: Initializes the unified `genai.Client` SDK.
3.  **Question Generation Logic**: The `question_generator` function maps the selected question type to a generation prompt instruction and requests a response from the `gemini-2.5-flash` model.
4.  **Gradio Interface**: Defines a web UI using `gr.Interface` with a text area for input content and radio buttons for selecting the question type, then launches it.
