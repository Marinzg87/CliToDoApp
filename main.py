"""
Simple ToDoApp for Cli
"""
from modules import functions

welcome_message = "Welcome in Todo App!"
print(welcome_message)
available_actions = ("show, add /new todo/, edit /todo number/, "
                     "complete /todo number/, exit: ")

while True:
    user_command = input(available_actions)

    if user_command == 'show':
        todos = functions.get_todos()
        for index, todo in enumerate(todos):
            print(str(index + 1) + "-" + todo.strip('\n').capitalize())
            
    elif user_command == 'add':
        print("add todo")
    elif user_command == 'edit':
        print("edit todo")
    elif user_command == 'complete':
        print("complete todo")
    elif user_command == 'exit':
        break
    else:
        print("Wrong command line")
        continue
print('Bye')
