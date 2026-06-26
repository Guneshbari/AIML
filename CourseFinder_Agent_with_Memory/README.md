# CourseFinder Agent with Memory

An educational planning assistant agent built using LangChain and LangGraph `InMemorySaver` to retain conversation history. The agent helps students discover the best learning resources by constructing custom roadmaps using Tavily Search, querying the official YouTube Data API v3 for high-quality free video tutorials, and supporting multi-turn conversational follow-up questions using memory checkpointers.

## Project Files

*   [app.py](./app.py): Python script configuring the LLM agent with conversation memory, Tavily research tool, YouTube Search API tool, system prompt, and agent execution.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-tavily`, `requests`, and `langgraph`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd CourseFinder_Agent_with_Memory
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
    YOUTUBE_API_KEY=your_youtube_api_key_here
    ```

## Usage

Run the course finder agent:
```bash
python app.py
```

By default, the script:
1. Asks the agent: *"I want to learn Machine Learning from scratch. Show me the best roadmap and find me beginner-friendly courses"*.
2. Asks a follow-up question: *"Suggest the best beginner course from the videos you showed"*, utilizing the chat memory checkpointer to refer to previously displayed YouTube video results.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API keys using `python-dotenv` relative to the script location.
2.  **Memory Store**: Configures `InMemorySaver` from `langgraph.checkpoint.memory` to serve as a checkpointer for holding thread-based state.
3.  **Agent Initialization**: Initializes the agent using LangChain's `create_agent` factory wrapper, attaching the tools, prompt, and the checkpointer.
4.  **YouTube Search Tool**: A custom `@tool` that queries YouTube's v3 search API for long video tutorials matching the skill, returning video titles, channel names, descriptions, publication dates, and watch links.
5.  **Tavily Search Tool**: Integrates `TavilySearch` from `langchain-tavily` to research prerequisite roadmaps and learning paths on the web.
6.  **Interactive Run**: Runs the initial planning request, then executes a follow-up query showing that the agent recalls details from the first response.
