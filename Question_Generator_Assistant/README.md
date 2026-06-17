# Question Generator Assistant

A Python application that uses the Google GenAI SDK to generate questions from provided text content.

## Project Files

*   [app.py](./app.py): Python script that handles API key configuration, user input, and the Google GenAI client logic.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Question_Generator_Assistant
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

Run the question generator assistant:
```bash
python app.py
```

After running, type or paste the text content you want to generate questions from into the terminal, then press **Enter**. The assistant will print the generated questions to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Uses `python-dotenv` to load the API key from the local `.env` file.
2.  **GenAI Client**: Initializes `genai.Client` from the `google-genai` library.
3.  **Input Reading**: Reads input from standard input (stdin) using `input()`.
4.  **Generation**: Uses `client.models.generate_content` with the `gemini-2.5-flash` model to generate questions from the input text.
