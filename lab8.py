#lab8.py

# Starter code for lab 8 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Jay Chan
# jayc10@uci.edu
# 54907952

from pathlib import Path

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

# ---------------------

class Note:
    def __init__(self, path):
        self.path = path

    def remove_note(self, remove_id):
        f = (self.path).open()
        id = 0
        lines = []
        for line in f:
            lines.append(line)
            id = id+1
        f.close()
        
        f = (self.path).open('w')
        id = 0
        removed_note = ""
        for line in lines:
            if id == int(remove_id):
                removed_note = line
            else:
                f.write(line)
            id = id+1
        f.close()
        return removed_note
    
    def read_notes(self):
        f = (self.path).open()
        output = []
        for line in f:
            output.append(line)
        f.close
        return output
    
    def save_note(self, input):
        if not (self.path).exists():
            (self.path).touch(existok=True)
        f = (self.path).open('a')
        f.write(input + '\n')
        f.close()
        
    
# ---------------------


def print_notes(notes:list[str]):
    id = 0
    for n in notes:
        print(f"{id}: {n}")
        id+=1

def delete_note(note:Note):
    try:
        remove_id = input("Enter the number of the note you would like to remove: ")
        remove_note = note.remove_note(int(remove_id))
        print(f"The following note has been removed: \n\n {remove_note}")
    except FileNotFoundError:
        print("The PyNote.txt file no longer exists")
    except ValueError:
        print("The value you have entered is not a valid integer")

def run():
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        p.touch()
    note = Note(p)
    
    print("Here are your notes: \n")
    print_notes(note.read_notes())

    user_input = input("Please enter a note (enter :d to delete a note or :q to exit):  ")

    if user_input == ":d":
        delete_note(note)
    elif user_input == ":q":
        return
    else:    
        note.save_note(user_input)
    run()


if __name__ == "__main__":
    print("Welcome to PyNote! \n")

    run()
