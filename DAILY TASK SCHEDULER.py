
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Task Manager")
        self.tasks = []

        self.create_widgets()
   
    def check_credentials(self, username, password):
        # TODO: Replace this with a secure authentication mechanism in a real application
        return username == "admin" and password == "password"

    def create_widgets(self):
        # TODO: Add GUI elements here
        pass

    def add_task(self):
        # TODO: Implement task addition logic
        pass

    def delete_task(self):
        # TODO: Implement task deletion logic
        pass

    def view_tasks(self):
        # TODO: Implement task viewing logic
        pass

    def create_widgets(self):
        self.lbl_task = tk.Label(self.root, text="Enter Task:")
        self.lbl_task.grid(row=0, column=0, padx=5, pady=5)

        self.entry_task = tk.Entry(self.root, width=30)
        self.entry_task.grid(row=0, column=1, padx=5, pady=5)

        self.btn_add = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.btn_add.grid(row=0, column=2, padx=5, pady=5)

        self.list_tasks = tk.Listbox(self.root, width=50)
        self.list_tasks.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.btn_delete = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.btn_delete.grid(row=2, column=0, padx=5, pady=5)

        self.btn_view = tk.Button(self.root, text="View Tasks", command=self.view_tasks)
        self.btn_view.grid(row=2, column=1, padx=5, pady=5)
    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.list_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.list_tasks.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.list_tasks.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks added yet.")
        else:
            tasks_str = "\n".join(self.tasks)
            messagebox.showinfo("Tasks", tasks_str)
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

