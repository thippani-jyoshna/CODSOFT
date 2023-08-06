
import tkinter as tk
from tkinter import messagebox

def add_or_edit_task():
    global editing_task_index
    task = task_entry.get().strip()
    if task:
        if editing_task_index is None:  # Add new task
            tasks.append(task)
        else:  # Edit existing task
            tasks[editing_task_index] = task

        update_task_listbox()
        task_entry.delete(0, tk.END)
        editing_task_index = None  # Reset editing index
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        global editing_task_index
        editing_task_index = selected_task_index[0]
        task_to_edit = tasks[editing_task_index]
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task_to_edit)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_listbox()

def update_task_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

tasks = []
editing_task_index = None

# Entry widget to enter tasks
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=5)

# Button to add or edit tasks
add_button = tk.Button(app, text="Add Task", command=add_or_edit_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=50)
listbox.pack(pady=5)

# Button to edit a task
edit_button = tk.Button(app, text="Edit", command=edit_task)
edit_button.pack(side=tk.LEFT, padx=5)

# Button to delete a task
delete_button = tk.Button(app, text="Delete", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

app.mainloop()
