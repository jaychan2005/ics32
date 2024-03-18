# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jay Chan
# jayc10@uci.edu
# 54907952

from pathlib import Path
import Profile
import ui
import shlex
import ds_client

def ocommand(command):
    # load profile
    filename = command[1]
    profile = Profile.Profile()
    profile.load_profile(filename)
    # update saves from loaded file
    saves['server'] = profile.dsuserver
    saves['username'] = profile.username
    saves['password'] = profile.password
    saves['bio'] = profile.bio
    saves['_posts'] = profile._posts

def ecommand(command):
    if len(command) >= 4:
        multiple_commands(command)
    elif command[1] == '-usr':
        saves['username'] = command[2]
        upload()
        print(f'- - - - - - -\nUsername has been saved! You entered: {command[2]}\n')
    elif command[1] == '-pwd':
        saves['password'] = command[2]
        upload()
        print(f'- - - - - - -\nPassword has been saved! You entered: {command[2]}\n')
    elif command[1] == '-bio':
        saves['bio'] = command[2]
        bio()
        print(f'- - - - - - -\nBio has been saved! You entered: "{command[2]}"\n')
        msg = ''
        online(msg)
    elif command[1] == '-addpost':
        add_post(command[2])
        print(f'- - - - - - -\nPost has been added! You entered: "{command[2]}"\n')
        online(command[2])
    elif command[1] == '-delpost':
        del_post(command[2])
        print(f'- - - - - - -\nPost {command[2]} has been deleted!\n')
    else:
        ui.invalid()    

def pcommand(command):
    profile = Profile.Profile()
    profile.load_profile(saves['server'])
    if len(command) >= 4:
        multiple_commands(command)
    elif command[1] == '-usr':
        print(profile.username)
    elif command[1] == '-pwd':
        print(profile.password)
    elif command[1] == '-bio':
        print(profile.bio)
    elif command[1] == '-posts':
        print("Here are all your posts: ")
        for i in range(len(profile._posts)):
            print(f'{i} - {profile._posts[i]['entry']}')
        print()
    elif command[1] == '-post':
        try:
            print(profile._posts[int(command[2])]['entry'])
        except:
            ui.invalid()
    elif command[1] == '-all':
        print(f'Username: {profile.username}')
        print(f'Password: {profile.password}')
        print(f'Bio: {profile.bio}')
        print('Posts:')
        for i in range(len(profile._posts)):
            print(f'{i} - {profile._posts[i]['entry']}')
    else:
        ui.invalid()

def program(command):
    if command[0] == 'L':
        ui.lcommand(command)
    elif command[0] == 'D':
        ui.dcommand(command)
    elif command[0] == 'R':
        ui.rcommand(command)
    elif command[0] == 'C':
        file = command[1] + "/" + command[3] + '.dsu'
        if Path(file).exists(): # checks for existing file
            new_command = [command[0], file]
            ocommand(new_command)
            print("File already exists! Info has been loaded.")
        else:
            filename = ui.ccommand(command)
            saves['server'] = filename
            print(f"- - - - - - -\nNew journal has been created! - {filename}\n")
            print("Format: [E] [-usr] [USERNAME] / [E] [-pwd] [PASSWORD] OR [E] [-usr] [USERNAME] [-pwd] [PASSWORD]")
            print("Please enter your username and/or password using the E command with the following -usr / -pwd command inputs:")
    elif command[0] == 'O':
        ocommand(command)
        print("O command has been run, dsu file has been loaded!\n")
    elif command[0] == 'E':
        ecommand(command)
    elif command[0] == 'P':
        pcommand(command)
    else:
        ui.invalid()

def admin(command):
    if command[0] == 'L':
        ui.lcommand(command)
    elif command[0] == 'D':
        ui.dcommand(command)
    elif command[0] == 'R':
        ui.rcommand(command)
    elif command[0] == 'C':
        file = command[1] + "/" + command[3] + '.dsu'
        if Path(file).exists(): # checks for existing file
            new_command = [command[0], file]
            ocommand(new_command)
        else:
            filename = ui.ccommand(command)
            saves['server'] = filename
            
    elif command[0] == 'O':
        ocommand(command)
    elif command[0] == 'E':
        ecommand(command)
    elif command[0] == 'P':
        pcommand(command)
    else:
        ui.invalid()

def multiple_commands(command):
    # recursive function
    if command[0] == 'E':
        commandnumber = (len(command) - 1) // 2
        for i in range(commandnumber):
            new = []
            new.append(command[0])
            new.append(command[2*i + 1])
            new.append(command[2*i + 2])
            program(new)
    elif command[0] == 'P':
        for i in range(len(command)):
            if '-' in command[i]:
                new = []
                new.append(command[0])
                new.append(command[i])
                if command[i] == '-post':
                    new.append(command[i + 1])
                program(new)
            else:
                continue
    else:
        ui.invalid()

def upload():
    if len(saves) >= 3:
        new_profile = Profile.Profile(saves['server'], saves['username'], saves['password'])
        new_profile.save_profile(saves['server'])
        print('☆ Profile has been successfully uploaded! ☆\n')
        print('It is recommended that you add a bio using [E] [-bio] ["BIO"]: ')

def bio():
    new_profile = Profile.Profile(saves['server'], saves['username'], saves['password'])
    new_profile.bio = saves['bio']
    new_profile.save_profile(saves['server'])

def add_post(new_post):
    post = Profile.Post()
    post.set_entry(new_post)
    new_profile = Profile.Profile(saves['server'], saves['username'], saves['password'])
    try:
        new_profile.bio = saves['bio']
    except:
        pass
    try: # load existing
        new_profile._posts = saves['_posts']
    except: # initialize
        pass
    new_profile.add_post(post)
    saves['_posts'] = new_profile._posts # save into main file
    new_profile.save_profile(saves['server'])
    
def del_post(index):
    new_profile = Profile.Profile(saves['server'], saves['username'], saves['password'])
    new_profile.bio = saves['bio']
    try: # load existing
        new_profile._posts = saves['_posts']
    except: # initialize
        pass
    new_profile.del_post(int(index))
    saves['_posts'] = new_profile._posts # save into main file
    new_profile.save_profile(saves['server'])
    
    
def online(message):
    answer = input("Would you like this to be posted on ICS 32 Distributed Social? (y/n): ")
    if answer == 'y' or answer == 'Y':
        server = "168.235.86.101"
        port = 3021
        try:
            ds_client.send(server, port, saves['username'], saves['password'], message, saves['bio'])
        except:
            ds_client.send(server, port, saves['username'], saves['password'], message)
    else:
        print('n or incorrect format detected, will not post.')
    

if __name__ == "__main__":
    # startup
    print("Welcome to user interface!\n\nPlease format your commands in this manner:\n[COMMAND] [INPUT] [[-]OPTION] [INPUT]\n\nBegin with either command 'C' to create or command 'L' to load a dsu file:")
    initial = input().split()
    saves = {}
    if initial[0] == 'Q':
        quit()
    elif initial == ['admin']:
        pass
    else:
        program(initial)
    # program
    if initial[0] == 'admin': # run admin (no interface)
        original = input()
        if original[0] == 'O' or original[0] == 'C':
            command = original.split()
        else:
            command = shlex.split(original)
        while True:
            if command[0] == 'Q':
                break
            else:
                admin(command)
            original = input()
            if original[0] == 'O' or original[0] == 'C':
                command = original.split()
            else:
                command = shlex.split(original)
    else: # run regular (interface)
        original = input()
        if original[0] == 'O' or original[0] == 'C':
            command = original.split()
        else:
            command = shlex.split(original)
        while True:
            if command[0] == 'Q':
                break
            else:
                program(command)
            original = input()
            if original[0] == 'O' or original[0] == 'C':
                command = original.split()
            else:
                command = shlex.split(original)
