from pathlib import Path

def create(path, file):
    return Path(path) / file


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def save_note(note: str, path, file):
    # create path obj to notes storage file
    p = create(path, file)
    # check if storage file exists, if not create it.
    if not p.exists():
        p.touch(exist_ok=True)
    # open and write user note to file
    f = p.open('a')
    f.write(note + '\n')
    f.close()


def read_notes(path, file):
    p = create(path, file)
    # check if storage file exists, if not return.
    if not p.exists():
        return
    print("Here are your notes: \n")
    # open and write user note to file
    f = p.open()
    for line in f:
        print(line)
    f.close()


def remove_note(path, file) -> str:
    p = create(path, file)
    # check if storage file exists, if not return.
    if not p.exists():
        raise FileNotFoundError("Notes file has been deleted unexpectedly")
    print("Here are your notes: \n")
    # open and write user note to file
    f = p.open()
    id = 1
    lines = []
    # print each note with an id and store each line in a list
    for line in f:
        lines.append(line)
        print(f"{id}: {line}")
        id = id+1
    f.close()
    remove_id = input("Enter the number of the note you would like to remove: ")
    if not is_int(remove_id):
        print ("Not a valid number, cancelling operation.")
        return ""
    # open as write to overwrite existing notes, add notes back while skipping user selection 
    f = p.open('w')
    id = 1
    removed_note = ""
    for line in lines:
        if id == int(remove_id):
            removed_note = line
        else:
            f.write(line)
        id = id+1
    f.close()
    return removed_note
