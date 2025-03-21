import streamlit as st
import pandas as pd
from datetime import datetime

# Set the page configuration
st.set_page_config(page_title="Expert To-Do List App", layout="centered", initial_sidebar_state="collapsed")

# Set custom CSS for the app
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        margin: 5px;
    }
    .stTextInput input {
        padding: 10px;
        border: 2px solid #ccc;
        font-size: 16px;
    }
    .css-12w0qpk {
        font-family: Arial, sans-serif;
        font-size: 20px;
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and intro text
st.title("📝 Expert To-Do List App")
st.write("Organize your tasks like a pro! Manage your daily to-do's with ease and style.")

# Initialize session state for storing tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# Function to add task to the list
def add_task():
    task_description = st.session_state["new_task"]
    if task_description:
        task = {"task": task_description, "status": "Pending", "timestamp": datetime.now()}
        st.session_state["tasks"].append(task)

# Function to mark a task as completed
def complete_task(index):
    st.session_state["tasks"][index]["status"] = "Completed"

# Input for new tasks
st.text_input("Enter a new task:", key="new_task")
st.button("Add Task", on_click=add_task)

# Display the to-do list in a DataFrame-style table
if st.session_state["tasks"]:
    df = pd.DataFrame(st.session_state["tasks"])
    df["Time Added"] = df["timestamp"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
    df.drop("timestamp", axis=1, inplace=True)
    st.write("### Your To-Do List:")
    st.dataframe(df[["task", "status", "Time Added"]])

    # Buttons to mark tasks as completed
    for index, task in enumerate(st.session_state["tasks"]):
        if task["status"] == "Pending":
            if st.button(f"Mark as completed - {task['task']}"):
                complete_task(index)

# Summary Section
st.write("## Task Summary:")
pending_tasks = len([task for task in st.session_state["tasks"] if task["status"] == "Pending"])
completed_tasks = len([task for task in st.session_state["tasks"] if task["status"] == "Completed"])
st.write(f"### Total Tasks: {len(st.session_state['tasks'])}")
st.write(f"### Pending Tasks: {pending_tasks}")
st.write(f"### Completed Tasks: {completed_tasks}")

# Add a motivational quote at the bottom
st.write("---")
st.write("**💡 Pro Tip:** *Stay focused and complete your tasks one step at a time. You got this!*")