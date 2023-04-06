from functions import get_todos, write_todos
import time


now = time.strftime("%b,%d,%Y,%H:%H:%S")
print('it is now: ', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')  # append the new todos to the txt file

        write_todos(todos, 'todos.txt')

    elif user_action.startswith('show') or user_action.startswith('display'):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = item.title()
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, 'todos.txt')

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete') or user_action.startswith('finish'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1  # Because our lists start at 0 and not 1
            todo_to_remove = todos[index].strip('\n')  # removing new line
            todos.pop(index)

            write_todos(todos, 'todos.txt')

            message = f'Todo: {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command not recognised. Try again')

print("Exiting todo program - Bye!")
