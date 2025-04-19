# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# AUDREY SUN
# AUDRES6@UCI.EDU
# 32241248

import time
import notebook
from pathlib import Path

'''
    Creates a new diary notebook in JSON format within the specified directory.
    Parameters:
        command list: Contains the command, path, and diary name elements. (e.g. C "/home/john/ics 32/my notebooks" -n my_diary)
    Return values:
        new_notebook: returns a notebook object created with new username, password, and bio
        notebook_path: returns the notebook path
'''
def create_notebook(command_lst: list):
    if len(command_lst)<4:
        print("ERROR")
        return None, None
    elif command_lst[2] != '-n':
        print("ERROR")
        return None, None
    else:
        diary_name = command_lst[3]
        path = Path(command_lst[1])
        notebook_path = path / f"{diary_name}.json"
        if notebook_path.exists():
            print("ERROR")
            return None, None
        elif not path.exists():
            print("ERROR")
            return None, None
        else:
            username = input('')
            password = input('')
            bio = input('')
            new_notebook = notebook.Notebook(username, password, bio)
            new_notebook.save(str(notebook_path))
            print(f'{notebook_path.absolute()} CREATED')    
            return new_notebook, notebook_path

'''
    Deletes a notebook file at the specified path.
    Parameters:
        command list: Contains the command and notebook path elements. (e.g. D "/home/algol/ics32/lectures/l1/student.json")
    Return values:
        None
'''
def delete_notebook(command_lst: list):
    if len(command_lst)<2:
        print("ERROR")
    else:
        path = Path(command_lst[1])
        if not path.exists():
            print("ERROR")
        elif path.suffix != ".json":
            print("ERROR") 
        else:
            path.unlink()
            print(f'{path.absolute()} DELETED')

'''
    Loads an existing notebook after verifying the username and password.
    Parameters:
        command list: Contains the command and notebook path element (e.g. O "/home/algol/ics32/lectures/l1/student.json")
    Return values:
        load_notebook: returns the loaded notebook object that will later be passed into the edit and print commands. 
        path: returns the notebook path
'''
def load_notebook(command_lst: list):
    if len(command_lst)<2:
        print("ERROR")
        return None, None
    else:
        path = Path(command_lst[1])
        if not path.exists():
            print("ERROR")
            return None, None
        elif path.suffix != ".json":
            print("ERROR")
            return None, None
        else:
            username = input('')
            password = input('')
            load_notebook = notebook.Notebook('', '', '')
            load_notebook.load(path)
            if load_notebook.username == username and load_notebook.password == password:
                print("Notebook loaded.")
                print(f"{username}")
                print(f"{load_notebook.bio}")
            else:
                print("ERROR")
            return load_notebook, path

'''
    Edit notebook function allows editing of notebook metadata (username, password, bio) and diary entries
    after the user creates or loads the notebook.
    Parameters:
        command list: contains the command followed by what the user wants to edit and their new input 
        (e.g. E -usr John -pwd "123 456")
        a_notebook: The notebook object to modify, obtained from create_notebook or load_notebook functions.
        a_path: notebook path that is passed in 
    Return values:
        None
'''
def edit_notebook(command_lst: list, a_notebook: notebook, a_path: Path):
    if len(command_lst)<3:
        print("ERROR")
    else:
        if not a_notebook:
            print("ERROR")
        else:
            username = ''
            password = ''
            bio = ''
            new_diary = ''
            delete_diary_index = ''
            for i in range(len(command_lst)):
                try:
                    if i % 2 == 1:
                        if command_lst[i] not in ['-usr', '-pwd', '-bio', '-add', '-del']:
                            raise CommandNotExistError()
                    if command_lst[i] == '-usr':
                        new_username = command_lst[i+1]
                        a_notebook.username = new_username
                        a_notebook.save(str(a_path))
                    elif command_lst[i] == '-pwd':
                        new_password = command_lst[i+1]
                        a_notebook.password = new_password
                        a_notebook.save(str(a_path))
                    elif command_lst[i] == '-bio':
                        new_bio = command_lst[i+1]
                        a_notebook.bio = new_bio
                        a_notebook.save(str(a_path))
                    elif command_lst[i] == '-add':
                        diary_info = command_lst[i+1]
                        new_diary = notebook.Diary(entry = diary_info, timestamp = time.time())
                        a_notebook.add_diary(new_diary)
                        a_notebook.save(str(a_path))
                    elif command_lst[i] == '-del':
                        delete_diary_index = int(command_lst[i+1])
                        a_notebook.del_diary(delete_diary_index)
                        a_notebook.save(str(a_path))
                except CommandNotExistError:
                    print("ERROR")
                    break
                except:
                    print("ERROR")
                    break
                
'''
    Print notebook function allows users to print user's username, password, bio, all their diaries, a single diary,
    or everything in the notebook.
    Parameters:
        command list: contains the command followed by what the user wants to print (e.g. P -bio -usr -diary 0)
        a_notebook: notebook object is passed in after creating or loading the notebook. 
    Return values:
        None
'''
def print_notebook(command_lst: list, a_notebook: notebook):
    if len(command_lst)<2:
        print("ERROR")
    else:
        if not a_notebook:
            print("ERROR")
        else:
            diary_command_found = False
            for i in range(1, len(command_lst)):
                try:
                    if diary_command_found == True:
                        diary_command_found = False
                        continue
                    if command_lst[i] not in ['-usr', '-pwd', '-bio', '-diaries', '-all', '-diary']:
                            raise CommandNotExistError()
                
                    if command_lst[i] == '-usr':
                        print(a_notebook.username)
                    elif command_lst[i] == '-pwd':
                        print(a_notebook.password)
                    elif command_lst[i] == '-bio':
                        print(a_notebook.bio)
                    elif command_lst[i] == '-diaries':
                        diary_list = a_notebook.get_diaries()
                        for i in range(len(diary_list)):
                            diary_info_dict = diary_list[i]
                            print(f"{i}: {diary_info_dict['entry']}")
                    elif command_lst[i] == '-diary':
                        diary_command_found = True
                        index = int(command_lst[i+1])
                        diary_list = a_notebook.get_diaries()
                        diary_info_dict = diary_list[index]
                        print(diary_info_dict['entry'])
                    elif command_lst[i] == '-all':
                        print(a_notebook.username)
                        print(a_notebook.password)
                        print(a_notebook.bio)
                        diary_list = a_notebook.get_diaries()
                        for i in range(len(diary_list)):
                            diary_info_dict = diary_list[i]
                            print(f"{i}: {diary_info_dict['entry']}")
                except CommandNotExistError:
                    print("ERROR")
                    break
                except:
                    print("ERROR")
                    break

class CommandNotExistError(Exception):
    pass 