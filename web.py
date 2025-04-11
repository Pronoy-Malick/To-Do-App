import streamlit as st
import functions

todos =functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My TODO App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    st.checkbox(todo)

st.text_input(label="", placeholder="Add New TODO",
              on_change=add_todo, key="new_todo")
