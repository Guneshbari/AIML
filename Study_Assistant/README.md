# Study Assistant

A simple Python application that uses the Google GenAI SDK to answer study-related questions.

## Project Files

*   [app.py](./app.py): Python script that handles API key configuration, study prompt logic, and Google GenAI client initialization.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Study_Assistant
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

Run the study assistant:
```bash
python app.py
```

By default, the script asks the Gemini model to *"Explain Generative AI"* and prints the generated explanation to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Uses `python-dotenv` to load the API key from the local `.env` file.
2.  **GenAI Client**: Initializes `genai.Client` from the `google-genai` library with the loaded API key.
3.  **Generation**: Uses `client.models.generate_content` with the `gemini-2.5-flash` model to answer the query *"Explain Generative AI"*.
