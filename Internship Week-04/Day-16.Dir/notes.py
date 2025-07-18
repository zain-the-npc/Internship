# cli_tool.py

import argparse
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

NOTES_FILE = "notes.txt"

# --- Helper Functions ---

def add_note(note_text):
    with open(NOTES_FILE, "a") as file:
        file.write(note_text + "\n")
    print(Fore.GREEN + " Note added!")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print(Fore.YELLOW + " No notes found.")
        return

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    if not notes:
        print(Fore.YELLOW + " Your note list is empty.")
        return

    print(Fore.CYAN + " Your Notes:")
    for idx, note in enumerate(notes, start=1):
        print(f"{Fore.BLUE}{idx}. {note.strip()}")

def delete_note(index):
    if not os.path.exists(NOTES_FILE):
        print(Fore.RED + " No notes file found.")
        return

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    if index < 1 or index > len(notes):
        print(Fore.RED + " Invalid note number.")
        return

    removed = notes.pop(index - 1)

    with open(NOTES_FILE, "w") as file:
        file.writelines(notes)

    print(Fore.GREEN + f" Deleted: {removed.strip()}")

# --- CLI Interface ---

def main():
    parser = argparse.ArgumentParser(description=" Notes CLI App - Add, View, and Delete Notes")

    parser.add_argument("--add", type=str, help="Add a new note")
    parser.add_argument("--view", action="store_true", help="View all notes")
    parser.add_argument("--delete", type=int, help="Delete a note by its number")

    args = parser.parse_args()

    if args.add:
        add_note(args.add)
    elif args.view:
        view_notes()
    elif args.delete:
        delete_note(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
