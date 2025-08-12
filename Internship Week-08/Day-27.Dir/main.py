# react_agent.py

def mock_llm(messages):
    """A fake LLM just for demo."""
    if len(messages) == 1:
        return """Thought: I should calculate minutes in 3 weeks.
Action: {"name": "calculator", "input": {"expr": "3 * 7 * 24 * 60"}}
PAUSE"""
    else:
        return """Thought: I have the result from the calculator.
Final Answer: 30240 minutes."""

def run_tool(action):
    """Executes a simple tool based on the action name."""
    if action["name"] == "calculator":
        expr = action["input"]["expr"]
        return str(eval(expr))  # CAUTION: only safe for trusted input
    return "Unknown tool"

def parse_action(llm_response):
    """Extracts the action from the LLM output."""
    import json, re
    match = re.search(r'Action:\s*(\{.*\})', llm_response, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return None

def react_agent(user_query):
    messages = [user_query]

    for turn in range(5):  # max 5 steps
        llm_output = mock_llm(messages)
        print("\n=== LLM OUTPUT ===")
        print(llm_output)

        # Show reasoning steps
        for line in llm_output.splitlines():
            if line.startswith("Thought:"):
                print("Reasoning:", line.replace("Thought:", "").strip())

        # Check for final answer
        if "Final Answer:" in llm_output:
            final_answer = llm_output.split("Final Answer:")[-1].strip()
            print("\nFINAL ANSWER:", final_answer)
            break

        # If there's an action, execute it
        action = parse_action(llm_output)
        if action:
            observation = run_tool(action)
            print("Observation:", observation)
            messages.append(f"Observation: {observation}")

if __name__ == "__main__":
    react_agent("How many minutes are in 3 weeks?")
