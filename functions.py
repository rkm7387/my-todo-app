def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write to do item in the text file."""
    with open("todos.txt", 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hey i am in function:")