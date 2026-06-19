# Persona-Based Study Assistant

A Python application that uses the Google GenAI SDK to answer study questions using configured personalities (such as a Friendly assistant or a formal Academic professor).

## Project Files

*   [app.py](./app.py): Python script configuring the client, dictionary of assistant personas, system instructions, and GenAI helper.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Persona_Based_Study_Assistant
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

By default, the script asks the model *"What are LLMs?"* using the **Friendly** persona, and prints the response to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **GenAI Client**: Initializes the unified `genai.Client` SDK.
3.  **Persona Mapping**: Uses a dictionary to map personalities (e.g., Friendly, Academic) to system instructions that define the model's behavior, tone, and formatting.
4.  **Generation with Config**: Calls `client.models.generate_content` using the `gemini-2.5-flash` model, passing the system instruction mapping inside `types.GenerateContentConfig` along with settings like temperature and max tokens.
