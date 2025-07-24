import streamlit as st
import functions

todos = functions.get_todos()


for i in todos:
    if todos.count(i) > 1:
        todos.remove(i)
        functions.write_todos(todos)
        st.rerun()




st.title("My ToDo App")
st.subheader("Welcome to my todo app")



for __i__ in todos:
    checkbox = st.checkbox(__i__, key=__i__)


st.text_input(' ',placeholder="Add a new todo:",
                on_change=functions.add_todo, key='new_todo')

col1, col2, col3 = st.columns(3)


with col1:
    st.button("Complete", key="Complete", on_click=functions.complete)

with col2:
    st.button("Edit",key="Edit")

with col3:
    st.button("Clear",key="Clear",on_click=functions.clear)


st.session_state