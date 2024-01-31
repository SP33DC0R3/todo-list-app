import functions
import PySimpleGUI as psg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", 'x') as file:
        pass


psg.theme('DarkGreen4')

clock = psg.Text('', key='clock')
label = psg.Text("Enter a To-Do")
input_box = psg.InputText(tooltip="Enter A To-Do", key="todo")
list_box = psg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")


window = psg.Window('My To-Do App',
                    [[clock],
                     [label],
                     [input_box, add_button],
                     [list_box, edit_button, complete_button],
                     [exit_button]],
                    font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Please select an item First", title="ERROR", font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                psg.popup("Please select an item First", title="ERROR", font=("Helvetica", 15))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WIN_CLOSED:
            break

window.close()