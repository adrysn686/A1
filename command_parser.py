# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# AUDREY SUN
# AUDRES6@UCI.EDU
# 32241248

import time
import notebook
from pathlib import Path

def create_notebook(command_lst: list):
    if len(command_lst)<4:
        print("ERROR")
        return None, None
    elif command_lst[2] != '-n':
        print("ERROR")
        return None, None
    else:
        username = input('')
        password = input('')
        bio = input('')
        diary_name = command_lst[3]
        path = Path(command_lst[1])
        notebook_path = path / f"{diary_name}.json"
        if notebook_path.exists():
            print("ERROR")
        elif not path.exists():
            print("ERROR")
        else:
            new_notebook = notebook.Notebook(username, password, bio)
            new_notebook.save(str(notebook_path))
            print(f'{notebook_path.absolute()} CREATED')    
            return new_notebook, notebook_path
        
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

    
def load_notebook(command_lst: list):
    if len(command_lst)<2:
        print("ERROR")
    else:
        path = Path(command_lst[1])
        if not path.exists():
            print("ERROR")
        elif path.suffix != ".json":
            print("ERROR")
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