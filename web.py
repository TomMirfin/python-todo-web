import streamlit as st
import functions

todos = functions.get_todos()
def add_new_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    functions.add_todo(todos)


st.title("My Todo App")
st.subheader("This is my todo app")

for index, x in enumerate(todos):
    checkbox = st.checkbox(x, key=x)
    if checkbox:
        todos.pop(index)
        functions.add_todo(todos)
        del st.session_state[x]
        st.rerun()


st.text_input(label="Enter a todo", placeholder="Add a new todo...", key="new_todo", on_change=add_new_todo)