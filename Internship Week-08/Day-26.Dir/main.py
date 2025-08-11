import difflib

qa_pairs = {
    "what is the best way to stay awake while studying": 
        "Cold brew coffee in one hand, motivational playlist in the other . Also… maybe actually sleep sometimes?",
    "how can i make my resume stand out": 
        "Highlight real achievements, keep it clean, and for goodness' sake — no Comic Sans. Recruiters have eyes too. ",
    "what should i do if i'm nervous before a presentation": 
        "Take three deep breaths, imagine the audience in slow motion, and remember — you know more about your topic than they do ."
}

# Normalize user input for matching
def normalize(text):
    return text.strip().lower()

# Find closest match using fuzzy matching
def find_best_match(user_q, questions):
    normalized_q = normalize(user_q)
    match = difflib.get_close_matches(normalized_q, questions, n=1, cutoff=0.5)
    return match[0] if match else None

# Main loop
if __name__ == "__main__":
    print("Ask me something! (type 'quit' to exit)\n")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["quit", "exit"]:
            print("Bye! ")
            break
        
        match = find_best_match(user_input, qa_pairs.keys())
        if match:
            print(qa_pairs[match])
        else:
            print("Hmm… I dont have an answer for that one yet.")
