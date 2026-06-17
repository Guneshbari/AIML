# Tone Modifier

A simple Python application that uses the Google GenAI SDK to modify the tone of a given text input.

## Project Files

*   [app.py](./app.py): Python script that handles API key configuration, tone modifier function, and Google GenAI client logic.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Tone_Modifier
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

Run the tone modifier script:
```bash
python app.py
```

By default, the script takes the phrase *"Knowledge is power."*, translates its tone to formal, and prints the result to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Uses `python-dotenv` to load the API key from the local `.env` file.
2.  **GenAI Client**: Initializes `genai.Client` from the `google-genai` library.
3.  **Generation**: Uses `client.models.generate_content` with the `gemini-2.5-flash` model to rewrite input text into a formal tone.
