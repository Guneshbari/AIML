import os
import sys
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path)

google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
rapidapi_key = os.getenv("RAPIDAPI_KEY")

if not google_api_key:
    print("Error: GOOGLE_API_KEY or GEMINI_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

if not tavily_api_key:
    print("Error: TAVILY_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

if not rapidapi_key:
    print("Error: RAPIDAPI_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

model = init_chat_model("google_genai:gemini-2.5-flash", api_key=google_api_key)

skill_demand_tool = TavilySearch(
    max_results=5, search_depth="advanced", tavily_api_key=tavily_api_key
)


@tool
def search_jobs(skill: str, location: str) -> list:
    """Search for jobs requiring a specific skill using JSearch API from RapidAPI."""
    print(f"\nCalling search_jobs tool")
    print(f"Searching jobs for: {skill} in {location}")
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
    }
    querystring = {"query": f"{skill} in {location}", "page": "1", "num_pages": "1"}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    jobs = data.get("data", [])
    results = []
    for job in jobs[:5]:
        results.append(
            {
                "title": job.get("job_title", "N/A"),
                "company": job.get("employer_name", "N/A"),
                "location": job.get("job_city", "N/A"),
                "type": job.get("job_employment_type", "N/A"),
                "apply_link": job.get("job_apply_link", "N/A"),
            }
        )
    return results


system_prompt = """You are a Skill-to-Career Mapping assistant that helps students understand skill demand and find matching job opportunities.
You have access to these tools:
- skill_demand_tool: Search for industry demand, salary insights, and career trends
- search_jobs: Find actual job listings requiring specific skills
Help the student by researching the skill they ask about and finding relevant opportunities. Present results in a clean, readable format with clear sections and proper spacing. 
Include all job details with apply links. Don't use markdown format."""

checkpointer = InMemorySaver()

config = {"configurable": {"thread_id": "1"}}

agent = create_agent(
    model=model,
    tools=[skill_demand_tool, search_jobs],
    system_prompt=system_prompt,
    checkpointer=checkpointer,
    debug=True,
)

user_query = "What's the demand for generative ai in the industry and show me related job openings in India"

response = agent.invoke(
    {"messages": [{"role": "user", "content": user_query}]},
    config=config,
)

print(response["messages"][-1].content)

# Follow-up question to test agent's memory
user_query_2 = "Summarize the key findings from our research in 2 bullet points"
response_2 = agent.invoke(
    {"messages": [{"role": "user", "content": user_query_2}]},
    config=config,
)

# Safely print text content to avoid TypeError if content is a list or string
content_2 = response_2["messages"][-1].content
if isinstance(content_2, list):
    print(content_2[0].get("text", content_2))
else:
    print(content_2)
