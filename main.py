while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()

    # Using Match Case: it is available after python 3.10 onwards.
    match user_action:
        case 'add':
            todo = input("Enter a todo: ").title() + "\n"

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))-1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to edit: ")) - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.pop(number)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

        case _:
            print("You entered an unknown command.")




