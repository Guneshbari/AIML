# TravelBuddy Agent with Memory

An intelligent travel planning assistant agent built using LangChain and LangGraph. The agent combines Tavily Search for destination research (attractions, culture, guides), SerpAPI's Google Flights engine for real-time flight search, and an `InMemorySaver` checkpointer memory to preserve context between multiple user queries in a chat thread.

## Project Files

*   [app.py](./app.py): Python script configuring the LLM agent, Tavily search tool, Google Flights SerpAPI tool, memory saver checkpointer, system prompt, and multi-turn agent execution.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-tavily`, `google-search-results`, `langgraph`, and `requests`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd TravelBuddy_Agent_with_Memory
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

By default, the script asks the agent *"I want to visit Goa from Hyderabad on 2026-12-15. Show me top attractions and flight options"*, prints the response, then asks a follow-up question (*"Tell me more about the first flight option you mentioned"*) which uses the checkpointer's memory configuration (`thread_id`) to maintain session history.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API keys using `python-dotenv`.
2.  **Agent Initialization**: Initializes the agent using LangChain's `create_agent` factory wrapper.
3.  **InMemory Checkpointer**: Declares `InMemorySaver` and passes it to the agent definition, allowing context to persist for configurations sharing a `thread_id`.
4.  **Multi-turn Invocation**: Executes `agent.invoke` twice with the same `config` config dictionary to demonstrate how the agent recalls previous flight results.
