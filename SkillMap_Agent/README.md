# Skill-to-Career Mapping Agent

An intelligent assistant agent built using LangChain that helps students understand industry skill demand and find relevant job openings. The agent uses Tavily for researching market trends and RapidAPI's JSearch API for searching actual job listings.

## Project Files

*   [app.py](./app.py): Python script configuring the LLM agent, Tavily search tool, RapidAPI custom search tool, system prompt, and agent execution.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-tavily` and `requests`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd SkillMap_Agent
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

Run the carrier mapping agent:
```bash
python app.py
```

By default, the script asks the agent *"What's the demand for generative ai in the industry and show me related job openings in India"*. The agent decides which tools to invoke (Tavily search for demand and JSearch for listings), executes them, compiles the findings, and prints the result to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API keys using `python-dotenv`.
2.  **Agent Initialization**: Initializes the agent using LangChain's `create_agent` factory wrapper.
3.  **Search Jobs Tool**: A custom `@tool` that queries the JSearch endpoint on RapidAPI for internship and full-time job openings matching the requested skill and location, then parses titles, employers, locations, and apply links.
4.  **Tavily Search Tool**: Integrates `TavilySearch` from `langchain-tavily` to search the web for industry insights.
5.  **Execution Loop**: Invokes the agent with the user's query and prints the final career advice response.
