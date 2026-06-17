# Language Translator Assistant

A simple Python application that uses the new Google GenAI SDK to translate languages.

## Project Files

*   [app.py](./app.py): Python script containing translation client logic.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Language_Translator_Assistant
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

Run the translator assistant script:
```bash
python app.py
```

It will run the translation function `language_translator` with the input *"Translate I am a boy in hindi"* and print the generated Hindi translation to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Uses `python-dotenv` to load the API key from the local `.env` file.
2.  **GenAI Client**: Initializes `genai.Client` from the `google-genai` library.
3.  **Generation**: Uses `client.models.generate_content` with the `gemini-2.5-flash` model to translate inputs.
