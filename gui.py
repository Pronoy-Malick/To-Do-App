import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="clock")

label = sg.Text("Write the To-Do")

sucess_label = sg.Text("", key="sucess", text_color="green")

input_box = sg.InputText(tooltip="Enter To-Do", key= "todo")

add_button = sg.Button("Add",size=10)

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events= True, size=(45,10))

edit_button = sg.Button("Edit", size=10)

complete_button = sg.Button("Complete",size=10)

exit_button = sg.Button("Exit", size=10)

col1 = sg.Column([[clock],[label],[input_box],[sucess_label],[list_box],[complete_button],[exit_button]])
col2 = sg.Column([[add_button],[edit_button]])

window = sg.Window("My To-Do App",
                   layout=[[col1,col2]],
                   font= ("Helvetica", 15))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b-%d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=" ")
            window['sucess'].update("Todo Is Added")

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['sucess'].update("Todo Is Edited")

            except IndexError:
                sg.popup("Select a item first")

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=" ")
                window['sucess'].update("Todo Is Completed")

            except IndexError:
                sg.popup("Select a item first")

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break


window.close()

