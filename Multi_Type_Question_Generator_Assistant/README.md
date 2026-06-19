# Multi-Type Question Generator Assistant

A Python application that uses the Google GenAI SDK to generate different types of questions (such as MCQs, Short Answer, or Interview questions) from a given text input.

## Project Files

*   [app.py](./app.py): Python script configuring the client, dictionary of question types, system instructions, and GenAI helper.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Multi_Type_Question_Generator_Assistant
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

By default, the script takes dummy Lorem Ipsum content, asks the model to generate **Short Answer** questions based on it, and prints the generated questions to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **GenAI Client**: Initializes the unified `genai.Client` SDK.
3.  **System Instruction Mapping**: Uses a dictionary to map question types (e.g., MCQs, Short Answer, Interview) to generation instructions.
4.  **Generation with Config**: Calls `client.models.generate_content` using the `gemini-2.5-flash` model, passing the system instruction mapping inside `types.GenerateContentConfig` along with settings like temperature and max tokens.
