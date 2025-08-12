# ReAct Agent Demo (Day 2 - Learn AI Agents Course)

## Overview
This project is a simple demonstration of the **ReAct (Reason + Act) framework** for AI agents.  
It simulates how an AI model:
1. **Thinks** about a problem (`Thought:`)
2. **Chooses an action** to perform (`Action:`)
3. **Pauses** while the tool executes
4. **Observes** the result (`Observation:`)
5. Produces a **final answer** (`Final Answer:`)

**Note:**  
For this demo, the LLM is **mocked** (hardcoded) — no real API calls are made.  
The only tool implemented is a basic calculator.

## How It Works
- The agent loop runs until it reaches a final answer or max turns.
- Thoughts (reasoning steps) are printed before the final answer.
- A fake LLM (`mock_llm`) generates responses in the ReAct format.
- Tool calls are parsed from the LLM output and executed locally.
