import streamlit as st
from Modules import functions

todos = functions.get_todos()


def add_todo():
    to_do = st.session_state["new_todo"] + "\n"
    print(to_do)
    todos.append(to_do)
    functions.write_todos(todos)


st.title("First Web App")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Please input a todo", placeholder="Add a new to do", on_change=add_todo, key="new_todo")
