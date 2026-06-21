# Weather Assistant with Tool Calling

A Python application that demonstrates tool calling (function calling) capabilities using the Groq SDK and the `llama-3.3-70b-versatile` model. The assistant can fetch real-time weather information for any city by executing a local weather-fetching tool via the OpenWeatherMap API.

## Project Files

*   [app.py](./app.py): Python script configuring the Groq client, weather-fetching tool definition, messages array, tool-execution logic, and final prompt generation.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `groq` and `requests`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd Weather_Assistant_With_Tool_Calling
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Keys:**
    Create a `.env` file in this directory and add your API keys:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    WEATHER_API_KEY=your_openweathermap_api_key_here
    ```

## Usage

Run the weather assistant:
```bash
python app.py
```

By default, the script asks the model *"What's the weather in Mumbai?"*. The model determines that it needs to call the `get_weather` function, returns the function arguments, the script executes the function locally, passes the result back to the model, and prints the model's final response to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the Groq and OpenWeatherMap API keys using `python-dotenv`.
2.  **Weather Fetching Tool**: Defines `get_weather(location)` which calls OpenWeatherMap API to retrieve temperature and weather description.
3.  **Tool Schema**: Defines the JSON schema for the weather tool, telling the model about the function name, description, and required parameters.
4.  **Initial Chat Request**: Requests the model (`llama-3.3-70b-versatile`) with the user's query and the tool definition.
5.  **Function Execution**: If the model requests a tool call, the script reads the parameters, runs `get_weather` locally, appends the tool response to the message history, and submits it back to the model for the final answer.
