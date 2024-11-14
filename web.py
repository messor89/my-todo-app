import streamlit as st
import functions as functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

def remove_todo():
    selected_indexes = [i for i, todo in enumerate(todos) if st.session_state.get(f"checkbox_{i}")]
    for index in sorted(selected_indexes, reverse=True):
        todos.pop(index)
    functions.write_todos(todos)
    st.rerun()

st.title("My ToDo App")
st.subheader("This is my todo app")

# Display each to-do item with a checkbox, initializing session state if needed
for index, todo in enumerate(todos):
    if f"checkbox_{index}" not in st.session_state:
        st.session_state[f"checkbox_{index}"] = False
    st.checkbox(todo, key=f"checkbox_{index}")

# Add input for a new to-do
st.text_input(label="Add new todo", placeholder="Type here...",
              on_change=add_todo, key="new_todo")
if st.button("Add"):
    add_todo()
# Remove button
if st.button("Remove"):
    remove_todo()

# Optional: Display session state for debugging
st.write(st.session_state)
