from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    api_key=api_key,
)

system_msg = SystemMessage(
    "You are a travel guide who gives brief recommendations for tourist destinations."
)
human_msg = HumanMessage("Suggest top 3 places to visit in Japan.")
messages = [system_msg, human_msg]

response = model.invoke(messages)
print(response.content)
