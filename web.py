import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


sl.title("My To-Do App")
sl.subheader("This is my todo app.")
sl.text("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        print(index)
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.rerun()


sl.text_input(label="Add a new Todo", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')