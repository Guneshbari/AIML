from google import genai
from google.genai import types
import requests
import os
from dotenv import load_dotenv

# Load .env file relative to script location
dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)

client = genai.Client(api_key=os.getenv("API_KEY"))


def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
    data = requests.get(url).json()

    if data.get("result") != "success":
        return {"error": "Invalid base currency or API failed"}

    rates = data["rates"]
    if to_currency.upper() not in rates:
        return {"error": "Invalid target currency"}

    return {
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount,
        "converted_amount": amount * rates[to_currency.upper()],
        "rate": rates[to_currency.upper()],
    }


tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="convert_currency",
                description="Convert currency using live exchange rates",
                parameters={
                    "type": "object",
                    "properties": {
                        "amount": {"type": "number"},
                        "from_currency": {"type": "string"},
                        "to_currency": {"type": "string"},
                    },
                    "required": ["amount", "from_currency", "to_currency"],
                },
            )
        ]
    )
]


messages = [
    {
        "role": "user",
        "parts": [{"text": "Convert 1 USD to INR"}],
    }
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(tools=tools),
)


parts = response.candidates[0].content.parts
tool_call = next((p.function_call for p in parts if hasattr(p, "function_call")), None)

if not tool_call:
    print(response.text)
    raise SystemExit()

args = tool_call.args

result = convert_currency(
    args["amount"],
    args["from_currency"],
    args["to_currency"],
)

followup = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages
    + [
        {"role": "model", "parts": [{"function_call": tool_call}]},
        {
            "role": "tool",
            "parts": [
                {
                    "function_response": {
                        "name": "convert_currency",
                        "response": result,
                    }
                }
            ],
        },
    ],
)


print(followup.text)
