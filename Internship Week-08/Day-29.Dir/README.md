# Function Calling Agent (Day 4 - Learn AI Agents)

## Overview
A simple demo of **OpenAI function calling** to auto-fetch location, weather, and time — no user input needed.

The agent:
- Gets a fixed location  
- Fetches simulated weather & time  
- Summarizes results in natural language  

---

## How It Works
1. Three Python functions:
   - `get_location()` → Returns "Karachi, Pakistan"  
   - `get_weather(location)` → Simulated weather data  
   - `get_time(location)` → Simulated local time  
2. Registered as tools for OpenAI  
3. AI calls them, receives results, and outputs a final summary  

---

## Note
- All data is simulated for demo purposes  
- Replace functions with real API calls for live results  
