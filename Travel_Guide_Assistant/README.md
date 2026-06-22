# Travel Guide Assistant

A Python application that uses the LangChain framework and the `langchain-google-genai` integration to construct a travel guide assistant using the `gemini-2.5-flash` model.

## Project Files

*   [app.py](./app.py): Python script that configures and initializes the LangChain chat model using `init_chat_model`, constructs system/human messages, and invokes the model.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain` and `langchain-google-genai`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Travel_Guide_Assistant
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

Run the travel guide assistant:
```bash
python app.py
```

By default, the script asks the travel assistant to *"Suggest top 3 places to visit in Japan"* and prints the recommendations to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **LangChain Model Initialization**: Uses `init_chat_model("google_genai:gemini-2.5-flash", api_key=api_key)` to dynamically initialize the Google GenAI chat model.
3.  **Construct Messages**: Creates a system context message defining the assistant's persona using `SystemMessage`, and the user's query using `HumanMessage`.
4.  **Model Invocation**: Runs `model.invoke` with the messages and prints the response content.
