import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # reset input field


todos = functions.get_todos()
st.session_state["new_todo"] = ""  # initialize the input field

st.title("Todo App")
st.write("Hello, Stranger! Use me to increase your creativity :-)")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a todo..",
              on_change=add_todo, key="new_todo")
st.stop()
