# TravelBuddy Agent

A smart travel planning assistant agent built using LangChain. The agent combines Tavily Search for destination research (attractions, culture, guides) and SerpAPI's Google Flights engine for real-time flight search.

## Project Files

*   [app.py](./app.py): Python script configuring the LLM agent, Tavily search tool, Google Flights SerpAPI tool, system prompt, and agent execution.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-tavily` and `google-search-results`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd TravelBuddy_Agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Keys:**
    Create a `.env` file in this directory and add your API keys:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    TAVILY_API_KEY=your_tavily_api_key_here
    SERPAPI_KEY=your_serpapi_key_here
    ```

## Usage

Run the travel buddy agent:
```bash
python app.py
```

By default, the script asks the agent *"I want to visit Goa from Hyderabad on 2026-12-15. Show me top attractions and flight options"*. The agent decides which tools to invoke (Tavily search for attractions and SerpAPI flight search for flights), executes them, formats the travel guide plan, and prints the result to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API keys using `python-dotenv`.
2.  **Agent Initialization**: Initializes the agent using LangChain's `create_agent` factory wrapper.
3.  **Google Flights Tool**: A custom `@tool` that queries SerpAPI's Google Flights engine for pricing, airlines, flight numbers, departures/arrivals, and durations, returning them as a list of dictionaries.
4.  **Tavily Search Tool**: Integrates `TavilySearch` from `langchain-tavily` to search the web for travel insights and destinations.
5.  **Execution Loop**: Invokes the agent with the user's travel query and outputs the final recommendation.
