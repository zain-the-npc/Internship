from openai import OpenAI
import datetime
import random
import json

# --- CONFIG ---
API_KEY = "       P L A C E     Y O U R        R E A L       A P I         H E R E        "  
client = OpenAI(api_key=API_KEY)

# --- FUNCTION IMPLEMENTATIONS ---
def get_location():
    return "Karachi, Pakistan"

def get_weather(location):
    conditions = ["Sunny", "Cloudy", "Rainy", "Windy"]
    return f"The current weather in {location} is {random.choice(conditions)}, 30°C."

def get_time(location):
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
    return f"The current time in {location} is {now.strftime('%I:%M %p')}."

# --- TOOL DEFINITIONS ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_location",
            "description": "Get the user's location",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get the current time for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]

# --- SCRIPT RUN ---
messages = [{"role": "system", "content": "You are a helpful assistant that can get location, weather, and time."}]

# First request: Ask for location
messages.append({"role": "user", "content": "Find my location, then tell me the weather and time there."})
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)

message = response.choices[0].message

if message.tool_calls:
    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        try:
            args = json.loads(tool_call.function.arguments)
        except json.JSONDecodeError:
            args = {}

        if function_name == "get_location":
            result = get_location()
        elif function_name == "get_weather":
            result = get_weather(args.get("location", "Unknown"))
        elif function_name == "get_time":
            result = get_time(args.get("location", "Unknown"))
        else:
            result = "Unknown function."

        messages.append({"role": "function", "name": function_name, "content": result})

# Second request: Ask AI to summarize
follow_up = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print("AI:", follow_up.choices[0].message.content)
