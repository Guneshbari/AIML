# Persona-Based Tone Modifier Assistant

A Python application that uses the Google GenAI SDK to modify the tone of a given sentence to either a Formal or Casual style.

## Project Files

*   [app.py](./app.py): Python script configuring the client, dictionary of tone modifiers, system instructions, and GenAI helper.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Persona_Based_Tone_Modifier_Assistant
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

Run the tone modifier assistant:
```bash
python app.py
```

By default, the script takes the phrase *"we are applying for the job"*, asks the model to rewrite it in a **Formal** tone, and prints the result to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **GenAI Client**: Initializes the unified `genai.Client` SDK.
3.  **Tone Mapping**: Uses a dictionary mapping tones (Formal, Casual) to system instructions that instruct the model on how to convert input sentences.
4.  **Generation with Config**: Calls `client.models.generate_content` using the `gemini-2.5-flash` model, passing the system instruction mapping inside `types.GenerateContentConfig` along with settings like temperature and max tokens.
