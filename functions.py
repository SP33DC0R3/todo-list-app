FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and returns a list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def get_new_todos(filepath=FILEPATH):
    """ Creates a new text file if user doesn't have one
        or sing the program for the frist time"""
    open(filepath, 'x')


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do item's list in a text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())