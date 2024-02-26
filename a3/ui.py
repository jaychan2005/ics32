# ui.py

# Imported from my assignment 2

# Replace the following placeholders with your information.

# Jay Chan
# jayc10@uci.edu
# 54907952

from pathlib import Path
import Profile

def lcommand(command):
    path = command[1]
    myPath = Path(path)
    if len(command) == 2:
        printlist(myPath)
    try:        
        if command[2] == '-r':
            # Output directory content recursively.
            if len(command) > 3:
                if command[3] == '-f':
                    try:
                        roptionf(myPath)
                    except:
                        invalid()
                elif command[3] == '-s':
                    try:
                        given = command[4]
                        roptions(myPath, given)
                    except:
                        invalid()
                elif command[3] == '-e':
                    try:
                        given = command[4]
                        roptione(myPath, given)
                    except:
                        invalid()
                else:
                    invalid()
            else:
                for file in myPath.iterdir():
                    if file.is_file():
                        print(file)
                for file in myPath.iterdir():
                    if file.is_dir():
                        print(file)
                        roption(file)
        elif command[2] == '-f':
            # Output only files, excluding directories in the results.
            try:
                foption(myPath)
            except:
                invalid()
        elif command[2] == '-s':
            # Output only files that match a given file name.
            try:
                given = command[3]
                soption(myPath, given)
            except:
                invalid()
        elif command[2] == '-e':
            # Output only files that match a given file extension.
            given = command[3]
            eoption(myPath, given)
        else:
            invalid()
    except:
        pass
    

def printlist(directory):
    for file in directory.iterdir():
        if file.is_file():
            print(file)
    for file in directory.iterdir():
        if file.is_dir():
            print(file)


def roption(directory):
    for file in directory.iterdir():
        if file.is_dir():
            print(file)
            roption(file)
        else:
            print(file)


def roptionf(directory):
    for file in directory.iterdir():
        if file.is_dir():
            roptionf(file)
        else:
            print(file)


def roptions(directory, name):
    for file in directory.iterdir():
        if file.is_dir():
            roptions(file, name)
        else:
            subsections = str(file).split('\\')
            if subsections[-1] == name:
                print(file)
    

def roptione(directory, extension):
    for file in directory.iterdir():
        if file.is_dir():
            roptione(file, extension)
        else:
            subsections = str(file).split('.')
            if subsections[-1] == extension:
                print(file)
                

def foption(directory):
    for file in directory.iterdir():
        if file.is_file():
            print(file)


def soption(directory, name):
    for file in directory.iterdir():
        if file.is_file():
            subsections = str(file).split('\\')
            if subsections[-1] == name:
                print(file)


def eoption(directory, extension):
    for file in directory.iterdir():
        if file.is_file():
            subsections = str(file).split('.')
            if subsections[-1] == extension:
                print(file)


def ccommand(command):
    path = command[1]
    filename = command[3] + '.dsu'
    filepath = path + '/' + filename
    Path(filepath).touch()
    return filepath


def dcommand(commandinput):
    path = dsu(commandinput)
    delete = Path(path)
    delete.unlink()
    print(path + " DELETED")


def rcommand(commandinput):
    path = dsu(commandinput)
    with open(path) as file:
        output = file.read()
        if output == "":
            print("EMPTY")
        else:
            print(output)


def dsu(command):
    path = command[1]
    filetype = path.split('.')
    filetype = filetype[-1]
    while True:
        if filetype == 'dsu':
            break
        else:
            print("ERROR")
            command = input()
            path = command[1]
            filetype = path.split('.')
            filetype = path[-1]
    return path

        
def invalid():
    print("Error, invalid format.")

