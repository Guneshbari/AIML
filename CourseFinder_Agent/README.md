# CourseFinder Agent

An educational planning assistant agent built using LangChain. The agent helps students discover the best learning resources by constructing custom roadmaps using Tavily Search, and querying the official YouTube Data API v3 for high-quality free video tutorials.

## Project Files

*   [app.py](./app.py): Python script configuring the LLM agent, Tavily research tool, YouTube Search API tool, system prompt, and agent execution.
*   [requirements.txt](./requirements.txt): Python dependencies for this assistant, including `langchain-tavily` and `requests`.

## Setup Instructions

1.  **Navigate to this assistant directory:**
    ```bash
    cd CourseFinder_Agent
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

By default, the script asks the agent *"I want to learn Machine Learning from scratch. Show me the best roadmap and find me beginner-friendly courses"*. The agent decides which tools to invoke (Tavily search for roadmap details and YouTube API search for video courses), executes them, formats the learning guide, and prints the result to the console.

## Code Explanation

The logic in [app.py](./app.py):
1.  **Environment Variables**: Loads the API keys using `python-dotenv`.
2.  **Agent Initialization**: Initializes the agent using LangChain's `create_agent` factory wrapper.
3.  **YouTube Search Tool**: A custom `@tool` that queries YouTube's v3 search API for long video tutorials matching the skill, returning video titles, channel names, and direct watch links.
4.  **Tavily Search Tool**: Integrates `TavilySearch` from `langchain-tavily` to research prerequisite roadmaps and learning paths on the web.
5.  **Execution Loop**: Invokes the agent with the student's query and outputs the final recommendation structure.
