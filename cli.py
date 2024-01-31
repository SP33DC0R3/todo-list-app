# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_input = input("Type add, show, edit, complete or exit: ").lower()
    user_input: str = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]
        todo_mod = f"{todo} -------- created {now}\n"

        todos = functions.get_todos()

        todos.append(todo_mod)

        functions.write_todos(todos)

    elif user_input.startswith("show"):

        todos = functions.get_todos()

        # todos_without_breakline = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}.{item}")

    elif user_input.startswith("edit"):
        try:
            numbere = int(user_input[5:])
            # numbere = int(input("Enter the number of todo to edit: "))

            new_todo = input("Enter the new todo: ")

            todos = functions.get_todos()

            todos[numbere - 1] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Please enter the number of todo.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_input.startswith("complete"):
        try:
            numberc = int(user_input[8:])
            # numberc = int(input("Enter the number of todo that is completed: "))

            todos = functions.get_todos()

            index = numberc - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' is removed from the list"
            print(message)
        except ValueError:
            print("Please enter the number of todo with the option.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_input.startswith("exit"):
        break
    else:
        print("Invalid Command!")

print("Bye")