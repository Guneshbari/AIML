# Currency Converter with Tool Calling

A Python application demonstrating tool calling (function calling) capabilities using the new Google GenAI SDK and the `gemini-2.5-flash` model. The assistant can perform live currency conversion by calling a local python function that requests live exchange rate data from the ExchangeRate-API.

## Project Files

*   [app.py](./app.py): Python script configuring the GenAI client, defining the currency converter tool schema, messages history, local conversion execution, and follow-up generation.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `google-genai` and `requests`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Currency_Converter_with_Tool_Calling
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    Create a `.env` file in this directory and add your Gemini API Key:
    ```env
    API_KEY=your_gemini_api_key_here
    ```

## Usage

Run the currency converter assistant:
```bash
python app.py
```

By default, the script asks the model to *"Convert 1 USD to INR"*. The model determines that it needs to call `convert_currency`, returns the tool invocation request, the script executes the function locally to fetch live rates, sends the result back to the model, and prints the model's final response to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API key using `python-dotenv`.
2.  **Conversion Function**: Defines `convert_currency(amount, from_currency, to_currency)` which calls the public API `https://open.er-api.com/v6/latest/` to fetch live rates.
3.  **Tool Declaration**: Declares a `types.Tool` with the `convert_currency` function definition and parameters schema so that Gemini knows how to invoke it.
4.  **Initial Chat Request**: Requests the model (`gemini-2.5-flash`) with the user's query and the tool configuration.
5.  **Function Execution**: Extracts `function_call` from the model's output parts, executes the local conversion, appends the tool response to the history using `function_response`, and requests the model again for the final text output.
