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


col1, col2, col3, a, b, c = st.columns(6)

with col1:
    st.button("Complete", key="Complete", on_click=functions.complete)

with col2:
    st.button("Clear",key="Clear",on_click=functions.clear)

with st.expander("Edit"):
    select = st.radio("Select a todo to edit:",
                       todos, key="selected_todo")
    text = st.session_state["selected_todo"]
    st.text_input("Edit todo here:",
                   value=text, key="edited_todo",
                   on_change= functions.edit)
    text = ""
