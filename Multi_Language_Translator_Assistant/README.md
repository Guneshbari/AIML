# Multi-Language Translator Assistant

A Python application that uses the Google GenAI SDK to translate a given sentence into multiple target languages (such as Hindi, Telugu, or French) using system instructions and content generation configuration.

## Project Files

*   [app.py](./app.py): Python script configuring the client, dictionary of language prompts, system instructions, and GenAI translation helper.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Multi_Language_Translator_Assistant
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

Run the translator assistant:
```bash
python app.py
```

By default, the script asks the model to translate *"What are LLMs?"* into **French** using system instructions, and prints the result to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **GenAI Client**: Initializes the unified `genai.Client` SDK.
3.  **System Instruction Mapping**: Uses a dictionary to map target languages (e.g., Telugu, Hindi, French) to translation prompt instructions.
4.  **Generation with Config**: Calls `client.models.generate_content` using the `gemini-2.5-flash` model, passing the system instruction mapping inside `types.GenerateContentConfig` along with settings like temperature and max tokens.
