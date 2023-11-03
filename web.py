import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + '\n')
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for x, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=x)
    if checkbox:
        todos.pop(x)
        functions.write_todos(todos)
        del st.session_state[x]
        st.experimental_rerun()

st.text_input("", placeholder="Add a new to-do...",
              on_change=add_todo, key="new_todo")
