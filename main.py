# Creating an Empty List:
todos = []

while True:
    user_action = input("Type add, show or exit:")

    # Using Match Case: it is available after python 3.10 onwards.
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break




