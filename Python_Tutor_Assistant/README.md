# Python Tutor Assistant

A Python application that uses the LangChain framework and the `langchain-groq` integration to construct a Python programming tutor using the `llama-3.3-70b-versatile` model.

## Project Files

*   [app.py](./app.py): Python script that configures and initializes the LangChain chat model for Groq, constructs system/human messages, and invokes the model.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain` and `langchain-groq`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Python_Tutor_Assistant
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Create a `.env` file in this directory and add your Groq API Key:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

Run the tutor assistant:
```bash
python app.py
```

By default, the script asks the Python tutor to *"Explain what a dictionary is in Python with an example"* and prints the explanation to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **LangChain Model Initialization**: Uses `init_chat_model("groq:llama-3.3-70b-versatile", api_key=api_key)` to dynamically initialize the Groq chat model.
3.  **Construct Messages**: Creates a system context message defining the tutor's persona using `SystemMessage`, and the user's query using `HumanMessage`.
4.  **Model Invocation**: Runs `model.invoke` with the messages and prints the response content.
