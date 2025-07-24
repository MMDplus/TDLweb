FILEPATH = "TDLsave.txt"
import streamlit as st

def get_todos(filepath=FILEPATH):
    """ the funsction get the todos from file and 
    return the list of todos
        """
    
    with open(filepath, 'r', encoding='utf-8') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_local, filepath=FILEPATH):
    with open(filepath, 'w',encoding='utf-8') as file:
        file.writelines(todos_local)


def complete():
    todos = get_todos()
    for __i__ in todos[:]:
        if st.session_state[__i__]:
            todos.remove(__i__)
            write_todos(todos)
            del st.session_state[__i__]


def add_todo():
    todos = get_todos()
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    write_todos(todos)
    st.session_state['new_todo'] = ''

def clear():
    todos = get_todos()
    for __i__ in todos[:]:
        del st.session_state[__i__]
    todos.clear()
    write_todos(todos)

def edit():
    todos = get_todos()
    todo_to_edit = st.session_state['selected_todo']
    index = todos.index(todo_to_edit)
    new_todo = st.session_state["edited_todo"]
    todos[index] = new_todo + '\n'
    write_todos(todos)