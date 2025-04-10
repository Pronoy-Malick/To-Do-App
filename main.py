import functions
import time


now = time.strftime("%b-%d, %Y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("Type your Choice Add, Show, Edit, Complete or Exit:- ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo+ '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"({index+1}) {item}.")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            print("THIS ARE THE EXSITING TODOs")
            print("___________________________")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"({index+1}) {item}.")

            new_todo = input("Enter the new TODO in place of the previous one:- ")
            todos[number-1] = new_todo + "\n"

            functions.write_todos(todos)

            print("The TODO list is edited according to your commands")
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            # Extracting the number of the todo to complete
            number = int(user_action[9:])
            index1 = number - 1
            todos = functions.get_todos()

            # Printing the todos
            print("THIS ARE THE EXSITING TODOs")
            print("___________________________")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"({index + 1}) {item}.")

            # Removing the todo the user wanted
            completed_todo = todos[index1].strip("\n")
            todos.pop(index1)

            # Writing the changes in the todos list
            functions.write_todos(todos)

            # Printing the completed todo
            print(f"{completed_todo}- This TODO is Completed")
        except ValueError:
            print("Wrong input...Number is Expected after Complete")
            continue
        except IndexError:
            print("There is no item with that index.....Out of Bound")
            continue

    elif user_action.startswith("exit"):
        print("Bye, See You Soon.........")
        break
    else:
        print("Command is not valid ")


