# Step 1: Define available functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def greet(name):
    return f"Hello, {name}!"

# Step 2: Simple command parser
def parse_command(command):
    words = command.lower().split()

    if words[0] == "add":
        return ("add", float(words[1]), float(words[3]))
    elif words[0] == "subtract":
        return ("subtract", float(words[1]), float(words[3]))
    elif words[0] == "greet":
        return ("greet", words[1])
    else:
        return (None,)

# Step 3: ReAct-style agent
def react_agent(command):
    # Thought
    print(f"Thought: I need to understand and process the command '{command}'")

    # Parse
    parsed = parse_command(command)

    if parsed[0] is None:
        return "Response: Sorry, I don't understand that command."

    # Action
    print(f"Action: Calling function '{parsed[0]}' with arguments {parsed[1:]}")

    # Observation & Response
    if parsed[0] == "add":
        result = add(parsed[1], parsed[2])
    elif parsed[0] == "subtract":
        result = subtract(parsed[1], parsed[2])
    elif parsed[0] == "greet":
        result = greet(parsed[1])

    print(f"Observation: Function returned {result}")
    return f"Response: {result}"

# Step 4: Test the agent
print(react_agent("add 5 and 7"))
print(react_agent("subtract 10 from 3"))
print(react_agent("greet zain"))
