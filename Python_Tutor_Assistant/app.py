from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

import os

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)
api_key = os.getenv("GROQ_API_KEY")

system_msg = SystemMessage(
    "You are a Python tutor who explains concepts with simple code examples."
)
human_msg = HumanMessage("Explain what a dictionary is in Python with an example.")
messages = [system_msg, human_msg]

model = init_chat_model(
    "groq:llama-3.3-70b-versatile",
    api_key=api_key,
)

response = model.invoke(messages)
print(response.content)
