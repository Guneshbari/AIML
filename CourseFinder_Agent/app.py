import os
import sys
import requests
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain.tools import tool
from dotenv import load_dotenv
from langchain.agents import create_agent

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path)

google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

if not google_api_key:
    print("Error: GOOGLE_API_KEY or GEMINI_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

if not tavily_api_key:
    print("Error: TAVILY_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

if not youtube_api_key:
    print("Error: YOUTUBE_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

model = init_chat_model("google_genai:gemini-2.5-flash", api_key=google_api_key)

course_research_tool = TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=tavily_api_key,
)


@tool
def search_courses(skill: str) -> list:
    """Search for free video courses and tutorials on YouTube."""
    print(f"\nCalling search_courses tool")
    print(f"Searching courses for: {skill}")

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": f"{skill} complete course tutorial",
        "type": "video",
        "videoDuration": "long",
        "maxResults": 5,
        "order": "relevance",
        "key": youtube_api_key,
    }

    response = requests.get(url, params=params)
    data = response.json()
    courses = data.get("items", [])
    print(f"Found {len(courses)} courses\n")

    result = []
    for course in courses:
        video_id = course.get("id", {}).get("videoId")
        snippet = course.get("snippet", {})
        title = snippet.get("title")
        channel = snippet.get("channelTitle")
        link = f"https://www.youtube.com/watch?v={video_id}" if video_id else None
        
        result.append(
            {
                "title": title,
                "channel": channel,
                "link": link,
            }
        )
    return result


# Define system prompt for the agent
system_prompt = """You are a CourseFinder assistant that helps students discover the best learning resources.
You have access to these tools:
- course_research_tool: Research learning roadmaps, free resources, certification options, and skill prerequisites
- search_courses: Find free video courses and tutorials on YouTube
Help students by:
1. Using course_research_tool to provide a comprehensive learning roadmap
2. Using search_courses to find relevant YouTube tutorials and courses
3. Present results in clear sections: Learning Roadmap and Video Courses
Do NOT use markdown format. Use plain text with clear headings."""

agent = create_agent(
    model=model,
    tools=[course_research_tool, search_courses],
    system_prompt=system_prompt,
    debug=True,
)

user_query = "I want to learn Machine Learning from scratch. Show me the best roadmap and find me beginner-friendly courses"

response = agent.invoke({"messages": [{"role": "user", "content": user_query}]})
print(response["messages"][-1].content)
