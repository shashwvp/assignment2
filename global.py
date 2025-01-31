# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Shashwat Patel
# shashwvp@uci.edu
# 68749259


# O /Users/shashwatpatel/Downloads/ICS32/a2starter/myjournal.dsu
# C /Users/shashwatpatel/Downloads/ICS32/a2starter/ -n myjournal
# E -usr "mark b" -pwd "password123"
#  E -addpost "HI"
#  P -all
from Profile import Profile
from Profile import Post
from pathlib import Path
import shlex
import json

global profile
global file_name
global path


def edit_file(arr):
    global file_name
    global profile
    global path
    try:
        for i in range(len(arr)-1):
            value = arr[i]
            if value=='-usr':
                profile.username = arr[i+1]
            elif value=='-pwd':
                profile.password = arr[i+1]
            elif value=='-bio':
                profile.bio = arr[i+1]
            elif value=='-addpost':
                profile.add_post(arr[i+1])
            elif value=='-delpost':
                profile.del_post(arr[i+1])
            profile.save_profile(Path(path / file_name))
    except Exception as e:
        print(e)
        

def print_file(arr):
    global file_name
    global profile
    global path

#     -usr Prints the username stored in the profile object

# -pwd Prints the password stored in the profile object

# -bio Prints the bio stored in the profile object

# -posts Prints all posts stored in the profile object with their ID (using list index is fine)

# -post [ID] Prints post identified by ID

# -all Prints all content stored in the profile object
    try:
        for i in range(len(arr)):
            if arr[i]=='-usr':
                print(profile.username)
            elif arr[i]=='-pwd':
                print(profile.password)
            elif arr[i]=='-bio':
                print(profile.bio)
            elif arr[i]=='-posts':
                content = profile.get_posts()
                for i in range(len(content)):
                    print(f"ID:{i}: {content[i]}")
            elif arr[i]=='-post':
                if i+1<len(arr):
                    content = profile.get_posts()
                    index = arr[i+1]
                    print(content[index])
            elif arr[i]=='-all':
                absolute_path = path / file_name
                f = open(absolute_path, "r")
                line = f.readline()
                dictionary = json.loads(line)
                for key,value in dictionary.items():
                    print(f"{key}: {value}")
            profile.save_profile(Path(path / file_name))

    except Exception as e:
        print(e)
    
# Open An Exisiting File
def open_file(arr):
    global profile
    if len(arr) != 2:
        print("ERROR")
    try: 
        if Path(arr[1]).exists():
            # Output Profile Info
            print("Here is the information in your profile:")
            print("Username:", profile.username)
            print("Password:", profile.password)
            print("Bio:", profile.bio)
    except Exception as e:
        print(e)

def delete_file(arr):
    if len(arr) != 2:
        return "ERROR"

    file_path = Path(arr[1])
    if not file_path.exists() or file_path.suffix != ".dsu":
        return "ERROR"
    else:
        file_path.unlink()
        return f"{file_path} DELETED"

def create_file(arr):
    global profile 
    global file_name
    global path 
    try:
        path = Path(arr[1])
        file_name = arr[-1] + ".dsu"

        # Create file
        f = path / file_name

        if f.exists():
            print("File already exists. Try Opening it.")
        else:
            f.touch()
        
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        bio = input("Enter a bio: ")

        profile = Profile(file_name, username, password)
        profile.bio = bio
        profile.save_profile(f)


    except Exception as e:
        raise e

    # Prompt User Using Profile Class
    #  username: a unique name to associate the user with posts.

    #  password: a password to protect access to user journal entries.

    #  bio: a brief description of the user.



def read_file(arr):
    if len(arr) != 2:
        return "ERROR"

    file_path = Path(arr[1])
    if not file_path.exists() or file_path.suffix != ".dsu":
        return "ERROR"

    content = file_path.read_text().strip()
    if not content:
        return "EMPTY"
    else:
        return content

def main():
    user = input()
    while user!='Q':
        try:
            if user == "Q":  
                # break
                pass

            command = user[0]
            arr = shlex.split(user)

            if command == "C":  
                create_file(arr)

            elif command == "D":  
                delete_file(arr)

            elif command == "R":  
                read_file(arr)
            elif command=="O":
                open_file(arr)
            elif command=="E":
                edit_file(arr)
            elif command=="P":
                print_file(arr)
            else:
                print("ERROR")
            user = input()
        except Exception as e:
            print(e)
            break
if __name__ == "__main__": 
    main()



