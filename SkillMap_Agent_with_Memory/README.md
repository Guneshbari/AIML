# SkillMap Agent with Memory

An intelligent career advisor agent built using LangChain and LangGraph. The agent combines Tavily Search for career research, RapidAPI's JSearch API for job listings, and an `InMemorySaver` checkpointer memory to preserve context between multiple user queries in a chat thread.

## Project Files

*   [app.py](./app.py): Python script configuring the LLM agent, Tavily search tool, Google JSearch RapidAPI tool, memory saver checkpointer, system prompt, and multi-turn agent execution.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-tavily`, `langgraph`, and `requests`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd SkillMap_Agent_with_Memory
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
    RAPIDAPI_KEY=your_rapidapi_key_here
    ```

## Usage

Run the career advisor agent:
```bash
python app.py
```

By default, the script asks the agent *"What's the demand for generative ai in the industry and show me related job openings in India"*, prints the response, then asks a follow-up question (*"Summarize the key findings from our research in 2 bullet points"*) which uses the checkpointer's memory configuration (`thread_id`) to maintain session history.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API keys using `python-dotenv`.
2.  **Agent Initialization**: Initializes the agent using LangChain's `create_agent` factory wrapper.
3.  **InMemory Checkpointer**: Declares `InMemorySaver` and passes it to the agent definition, allowing context to persist for configurations sharing a `thread_id`.
4.  **Multi-turn Invocation**: Executes `agent.invoke` twice with the same `config` config dictionary to demonstrate how the agent recalls previous search results.
