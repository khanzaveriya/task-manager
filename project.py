import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        tasks.remove(task)
    except:
        messagebox.showwarning("Warning", "Select a task!")

root = tk.Tk()
root.title("Personal Task Manager")
root.geometry("420x450")
root.configure(bg="#1e1e2f")

title = tk.Label(root, text="📝 My Tasks",
                 font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12),
                 bg="#2c2c3e", fg="white", insertbackground="white")
entry.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task",
                    bg="#4CAF50", fg="white",
                    width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(frame, text="Delete Task",
                    bg="#f44336", fg="white",
                    width=12, command=delete_task)
del_btn.grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=40, height=15,
                     bg="#2c2c3e", fg="white",
                     selectbackground="#6a5acd",
                     font=("Arial", 11))
listbox.pack(pady=15)

root.mainloop()
