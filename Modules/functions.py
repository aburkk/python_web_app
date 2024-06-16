FILEPATH = 'Text Files/list.txt'


def get_todos(filepath=FILEPATH):
    """Return the items in the text file in described path"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
