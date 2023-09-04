#pip freeze > requirements.txt

import streamlit as st
import functions

todos = functions.get_list()
st.set_page_config('Todos App')


def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    functions.write_list(todos)
    st.session_state["new_todo"] = ""


st.markdown("<title>kodkfhjkh</title>", True)
st.title("my todo app")
st.subheader("this is todos app")
st.write("checkbox:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # if checkox ===> if checkox == True
    if checkbox:
        todos.pop(index)
        functions.write_list(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="enter a new todo....", on_change=add_todo, key="new_todo")