import functions
import FreeSimpleGUI as sg

label = sg.Text("Write the To-Do")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("ADD")

window = sg.Window("My To-Do App", layout=[[label, input_box, add_button]])
window.read()
window.close()

