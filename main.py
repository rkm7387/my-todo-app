while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()

    # Using Match Case: it is available after python 3.10 onwards.

    if "add" in user_action:
        todo = user_action[4:]

        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif "edit" in user_action:

        number = int(user_action[5:])-1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter the new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:

        number = int(user_action[9:]) - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.pop(number)

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break

    else:
        print("Command is not valid🙂")






