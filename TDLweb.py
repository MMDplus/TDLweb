import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''

st.title("My ToDo App")
st.subheader("Welcome to my todo app")

for index, __i__ in enumerate(todos):
    checkbox = st.checkbox(__i__, key=__i__)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[__i__]
        st.rerun()

st.text_input(' ',placeholder="Add a new todo:",
                on_change=add_todo, key='new_todo')
