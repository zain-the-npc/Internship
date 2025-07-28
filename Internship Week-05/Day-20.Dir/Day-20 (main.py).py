
import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Import passages from passages.py
from passages import easy_passages, intermediate_passages, hard_passages

# --- Configuration ---
TEST_DURATION_SECONDS = 60 # Set the duration of the typing test
EASY_WORD_LENGTH = 5 # Standard for WPM calculation (5 chars/word)

# --- Utility Functions ---

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    """Displays a countdown before the test starts."""
    clear_console()
    print("Prepare to type...")
    for i in range(seconds, 0, -1):
        print(f"Starting in: {Fore.CYAN}{i}{Style.RESET_ALL}...", end='\r')
        time.sleep(1)
    clear_console()
    print(f"{Fore.GREEN}GO!{Style.RESET_ALL}\n")
    time.sleep(0.5)

def display_final_comparison(passage, typed_text):
    """
    Displays the target passage and the user's typed text for comparison.
    Green for correct, Red for incorrect.
    This is called AFTER the test is done.
    """
    print(f"{Fore.YELLOW}Original Passage:{Style.RESET_ALL}\n")
    print(passage)
    print("\n" + "=" * len(passage))
    print(f"\n{Fore.CYAN}Your Typed Text (with corrections):{Style.RESET_ALL}\n")

    for i, char in enumerate(passage):
        if i < len(typed_text):
            if typed_text[i] == char:
                print(f"{Fore.GREEN}{char}{Style.RESET_ALL}", end='')
            else:
                print(f"{Fore.RED}{char}{Style.RESET_ALL}", end='')
        else:
            # If target passage is longer than typed, show remaining target chars in default color
            print(f"{Fore.WHITE}{char}{Style.RESET_ALL}", end='')

    # If typed text is longer than target, show extra typed characters in red
    if len(typed_text) > len(passage):
        print(f"{Fore.RED}{typed_text[len(passage):]}{Style.RESET_ALL}", end='')
    print("\n")


def calculate_results(target_text, typed_text, time_taken):
    """Calculates WPM, accuracy, and errors."""
    correct_chars = 0
    errors = 0
    total_chars_in_target = len(target_text)

    # Compare typed text with target text up to the length of the shorter string
    for i in range(min(total_chars_in_target, len(typed_text))):
        if typed_text[i] == target_text[i]:
            correct_chars += 1
        else:
            errors += 1

    # Add errors for any extra characters typed beyond the target text length
    if len(typed_text) > total_chars_in_target:
        errors += (len(typed_text) - total_chars_in_target)

    # Accuracy is based on correctly typed characters out of the target text's length
    accuracy = (correct_chars / total_chars_in_target) * 100 if total_chars_in_target > 0 else 0

    # WPM calculation: (total correct characters / 5) / time in minutes
    words_typed = correct_chars / EASY_WORD_LENGTH
    minutes = time_taken / 60
    wpm = words_typed / minutes if minutes > 0 else 0

    return wpm, accuracy, errors, time_taken, correct_chars


# --- Main Test Function ---

def run_test():
    """Runs the full typing test."""
    clear_console()
    print(f"{Fore.MAGENTA}--- Welcome to the Python Typing Test! ---{Style.RESET_ALL}")

    while True:
        print(f"\n{Fore.BLUE}Select Difficulty:{Style.RESET_ALL}")
        print(f"  {Fore.GREEN}1. Easy{Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}2. Intermediate{Style.RESET_ALL}")
        print(f"  {Fore.RED}3. Hard{Style.RESET_ALL}")

        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            passages_to_use = easy_passages
            difficulty_name = "Easy"
            break
        elif choice == '2':
            passages_to_use = intermediate_passages
            difficulty_name = "Intermediate"
            break
        elif choice == '3':
            passages_to_use = hard_passages
            difficulty_name = "Hard"
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1, 2, or 3.{Style.RESET_ALL}")
            time.sleep(1)
            clear_console()

    print(f"\nYou selected {Fore.CYAN}{difficulty_name}{Style.RESET_ALL} difficulty.")
    input("Press Enter to start the test...")

    # Select a random passage based on chosen difficulty
    target_passage = random.choice(passages_to_use)

    countdown(3) # 3-second countdown

    # --- Core Change: Input Handling ---
    clear_console()
    print(f"{Fore.YELLOW}Type the following text (Press Enter when done or time runs out):{Style.RESET_ALL}\n")
    print(target_passage)
    print("\n" + "=" * len(target_passage))
    print(f"\n{Fore.CYAN}Start typing below:{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}You have {TEST_DURATION_SECONDS} seconds. Hit Enter to submit.{Style.RESET_ALL}\n")

    start_time = time.time()

    # This is the best we can do for "continuous" typing with standard input()
    # without blocking issues or complex console manipulation libraries.
    try:
        # Prompt for user input. This will block until Enter is pressed.
        # The user should type the entire passage or as much as they can.
        # We add a dummy visual timer loop below this that won't interfere.
        typed_text = input("> ") # User types everything they want, then presses Enter
    except EOFError: # Handles Ctrl+D/Ctrl+Z
        typed_text = ""
        print(f"\n{Fore.RED}Input stream closed. Test ended.{Style.RESET_ALL}")
    except KeyboardInterrupt: # Handles Ctrl+C
        typed_text = ""
        print(f"\n{Fore.RED}Test interrupted by user. Test ended.{Style.RESET_ALL}")

    end_time = time.time()
    actual_time_taken = end_time - start_time

    # Final time taken should be capped at the test duration if they took too long,
    # or the actual time if they finished early.
    final_time_taken = min(actual_time_taken, TEST_DURATION_SECONDS)

    # Calculate results
    wpm, accuracy, errors, _, correct_chars = calculate_results(
        target_passage, typed_text, final_time_taken
    )

    clear_console()
    print(f"{Fore.CYAN}--- Test Over! ---{Style.RESET_ALL}\n")
    display_final_comparison(target_passage, typed_text) # Show final comparison

    print("\n" + "=" * 30)

    print(f"\n{Fore.GREEN}Results:{Style.RESET_ALL}")
    print(f"  Difficulty: {Fore.CYAN}{difficulty_name}{Style.RESET_ALL}")
    print(f"  Time Taken: {Fore.YELLOW}{final_time_taken:.2f} seconds{Style.RESET_ALL}")
    print(f"  Words Per Minute (WPM): {Fore.YELLOW}{wpm:.2f}{Style.RESET_ALL}")
    print(f"  Accuracy: {Fore.YELLOW}{accuracy:.2f}%{Style.RESET_ALL}")
    print(f"  Errors: {Fore.YELLOW}{errors}{Style.RESET_ALL}")
    print(f"  Correct Characters: {Fore.YELLOW}{correct_chars}{Style.RESET_ALL}")
    print(f"  Target Length: {Fore.YELLOW}{len(target_passage)}{Style.RESET_ALL}")
    print(f"  Typed Length: {Fore.YELLOW}{len(typed_text)}{Style.RESET_ALL}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    run_test()