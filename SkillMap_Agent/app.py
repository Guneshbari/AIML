import os
import sys
import requests
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

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
    querystring = {
        "query": f"{skill} in {location}",
        "page": "1",
        "country": "in",
        "employment_types": "INTERN,FULLTIME",
        "job_requirements": "no_experience,under_3_years_experience",
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    jobs = data.get("data", [])
    print(f"Found {len(jobs)} jobs\n")

    result = []
    for job in jobs:
        result.append(
            {
                "title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_city"),
                "apply_link": job.get("job_apply_link"),
            }
        )
    return result


system_prompt = """You are a Skill-to-Career Mapping assistant that helps students understand skill demand and find matching job opportunities.
You have access to these tools:
- skill_demand_tool: Search for industry demand, salary insights, and career trends
- search_jobs: Find actual job listings requiring specific skills
Help the student by researching the skill they ask about and finding relevant opportunities. Present results in a clean, readable format with clear sections and proper spacing. 
Include all job details with apply links. Don't use markdown format."""

agent = create_agent(
    model=model, tools=[skill_demand_tool, search_jobs], system_prompt=system_prompt
)

user_query = "What's the demand for generative ai in the industry and show me related job openings in India"

response = agent.invoke({"messages": [{"role": "user", "content": user_query}]})

print(response["messages"][-1].content)
