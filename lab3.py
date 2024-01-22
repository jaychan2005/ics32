#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Jay Chan
# jayc10@uci.edu
# 54907952

from pathlib import Path

def intro():
    print("Welcome to PyNote!")
    print("Here are your notes:")

def resume():
    # Personalized to my computer
    myPath = Path(r"C:\Users\jaych\Desktop\ics32\pynote.txt")
    if myPath.exists():
        with open('pynote.txt') as my_file:
            print('\n' + my_file.read())
    else:
        with open('pynote.txt', 'x'):
            print('')

def save():
    user_input = input("Please enter a new note (enter q to exit): ")
    while user_input != 'q':
        with open('pynote.txt', 'a') as file:
            file.write(user_input + '\n')
            user_input = input("Please enter a new note (enter q to exit): ")

if __name__ == "__main__":
    intro()
    resume()
    save()
