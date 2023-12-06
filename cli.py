import functions
import time


while True:
    user_action = input("Type add, show, edit, complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos )

    elif user_action.startswith("show"):

        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])-1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid🙂")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1

            todos = functions.get_todos()

            todos.pop(number)

            functions.write_todos(todos)

        except IndexError:
            print("There is no item with that number:")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid🙂")






