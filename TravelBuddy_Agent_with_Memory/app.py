import os
import sys
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_tavily import TavilySearch
from serpapi import GoogleSearch
from langgraph.checkpoint.memory import InMemorySaver

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path)

google_api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")
serpapi_key = os.getenv("SERPAPI_KEY")

if not google_api_key or "your_google" in google_api_key:
    # Try to fallback to global GEMINI_API_KEY if local is just placeholders
    google_api_key = os.getenv("GEMINI_API_KEY")

if not google_api_key or "your_google" in google_api_key:
    print("Error: GOOGLE_API_KEY or GEMINI_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

if not tavily_api_key or "your_tavily" in tavily_api_key:
    print("Error: TAVILY_API_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

if not serpapi_key or "your_serpapi" in serpapi_key:
    print("Error: SERPAPI_KEY environment variable not set.")
    print("Please set it in your environment or a .env file.")
    sys.exit(1)

model = init_chat_model("google_genai:gemini-2.5-flash", api_key=google_api_key)

destination_research_tool = TavilySearch(
    max_results=5, search_depth="advanced", tavily_api_key=tavily_api_key
)


@tool
def search_flights(origin: str, destination: str, date: str) -> list:
    """Search for flights using SerpAPI Google Flights. Date should be in YYYY-MM-DD format like '2026-12-15'."""
    print(f"\nCalling search_flights tool")
    print(f"Searching flights from {origin} to {destination} on {date}")

    params = {
        "api_key": serpapi_key,
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "outbound_date": date,
        "currency": "INR",
        "type": "2",
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    best_flights = results.get("best_flights", [])
    other_flights = results.get("other_flights", [])
    flights = best_flights + other_flights
    print(f"Found {len(flights)} flights\n")

    result = []
    for flight in flights[:5]:  # Return top 5 flights
        legs = flight.get("flights", [])
        if legs:
            first_leg = legs[0]
            result.append(
                {
                    "price": flight.get("price"),
                    "airline": first_leg.get("airline"),
                    "flight_number": first_leg.get("flight_number"),
                    "departure_time": first_leg.get("departure_airport", {}).get("time"),
                    "arrival_time": first_leg.get("arrival_airport", {}).get("time"),
                    "duration": flight.get("total_duration"),
                }
            )
    return result


checkpointer = InMemorySaver()
config = {"configurable": {"thread_id": "1"}}

system_prompt = """You are a TravelBuddy assistant that helps travelers plan trips.
You have access to these tools:
- destination_research_tool: Research attractions, culture, and travel tips
- search_flights: Find flight options (use IATA codes: HYD=Hyderabad, GOI=Goa, BOM=Mumbai, DEL=Delhi, BLR=Bangalore)
Help the traveler by researching destinations and finding flights.
Present results in a clean, readable format with clear sections.
Don't use markdown format."""

agent = create_agent(
    model=model,
    tools=[destination_research_tool, search_flights],
    system_prompt=system_prompt,
    checkpointer=checkpointer,
    debug=True,
)

user_query = "I want to visit Goa from Hyderabad on 2026-12-15. Show me top attractions and flight options"

response = agent.invoke(
    {"messages": [{"role": "user", "content": user_query}]},
    config=config,
)

print(response["messages"][-1].content)

user_query_2 = "Tell me more about the first flight option you mentioned"

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
