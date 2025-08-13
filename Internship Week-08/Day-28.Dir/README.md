# ReAct Agent Demo (Day 3 - Learn AI Agents Course)

## Overview
This project is a simple demonstration of extending the ReAct (Reason + Act) framework for AI agents.  
It builds on the basic ReAct loop to add **command parsing and function execution** without using a real or simulated LLM.

The agent now:
1. Thinks about a problem (`Thought:`)
2. Parses the command to identify a function and arguments
3. Chooses an action to perform (`Action:`)
4. Pauses while the tool executes
5. Observes the result (`Observation:`)
6. Produces a final answer (`Final Answer:`)

**Note:**  
For this demo, there is no AI model or LLM — the parsing logic is handled directly in Python.  
The tools implemented are basic functions like add, subtract, and greet just to know the ReAct response style.

---

## How It Works
- The agent loop runs until it reaches a final answer or max turns.
- Thoughts (reasoning steps) are printed before the final answer.
- Commands are read as plain text and parsed into a function name and arguments.
- The matching local function is called with the extracted arguments.
- The result is observed and returned as the final response.

---
