# Creating an Empty List:
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()

    # Using Match Case: it is available after python 3.10 onwards.
    match user_action:
        case 'add':
            todo = input("Enter a todo: ").title()
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))-1
            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to edit: ")) - 1
            todos.pop(number)
        case 'exit':
            break
        case _:
            print("You entered an unknown command.")




