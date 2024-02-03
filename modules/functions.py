FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        local_todos = file.readlines()
    return local_todos
