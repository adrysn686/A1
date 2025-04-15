# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# AUDREY SUN
# AUDRES6@UCI.EDU
# 32241248
import command_parser
import shlex

def main():
    try:
        while True:
            command_input = input('')
            if command_input == 'Q':
                break
            command_lst = shlex.split(command_input)
            command = command_lst[0] 
            if command == 'C':
                a_notebook, a_path = command_parser.create_notebook(command_lst)
            elif command == 'D':
                command_parser.delete_notebook(command_lst)
            elif command == 'O':
                a_notebook, a_path = command_parser.load_notebook(command_lst)
            elif command == 'E':
                command_parser.edit_notebook(command_lst, a_notebook, a_path)
            elif command == 'P':
                command_parser.print_notebook(command_lst, a_notebook)
            else:
                print("ERROR")
    except:
        print("ERROR")

if __name__=="__main__":
    main()
    
