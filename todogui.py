import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f7")

        self.tasks = []

        self.setup_ui()

    def setup_ui(self):

        title_label = tk.Label(
            self.root,
            text = "To-Do List",
            font = ("Helvetica", 22, "bold"),
            bg = "#f0f4f7",
            fg = "#333"
        )
        title_label.pack(pady=10)

        input_frame = tk. Frame (self.root, bg="#f0f4f7")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            font = ("Helvetica", 12),
            width = 30
        )
        self.task_entry.pack(side="left", padx=(0, 10))

        add_button = tk.Button(

            input_frame,
            text = "Add Task",
            font = ("Helvetica", 11, "bold"),
            bg="#27ae60",
            fg = "white",
            padx = 10,
            command = self.add_task
        )

        add_button.pack(side="left")

        list_frame = tk. Frame (self.root, bg="#f0f4f7")
        list_frame.pack(pady=10, fill = "both", expand=True)

        self.task_listbox = tk.Listbox(
            list_frame,
            font = ("Helvetica", 12),
            width = 45,
            height = 10,
            activestyle = "none"
        )

        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk. Scrollbar (list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        self.info_label = tk.Label(
            self.root,
            text = "",
            font = ("Helvetica", 11),
            bg="#f0f4f7",
            fg="#007acc"

        )
        self.info_label.pack(pady=5)
        button_frame = tk. Frame (self.root, bg="#f0f4f7")

        button_frame.pack(pady=10)
        mark_done_button = tk. Button(
            button_frame,
            text = "Mark as Done",
            font = ("Helvetica", 11, "bold"),
            bg="#2980b9",
            fg = "white",
            padx = 10,
            command=self.mark_done
        )

        mark_done_button.pack(side="left", padx=5)

        delete_button = tk.Button(
            button_frame,
            text = "Delete Task",
            font = ("Helvetica", 11, "bold"),
            bg="#c0392b",
            fg = "white",
            padx=10,
            command=self.delete_task

        )

        delete_button.pack(side="left", padx=5)

        clear_button = tk.Button(
            button_frame,
            text = "Clear All",
            font = ("Helvetica", 11, "bold"),
            bg="#7f8c8d",
            fg = "white",
            padx=10,
            command = self.clear_all
        )
        clear_button.pack(side="left", padx=5)

    def refresh_listbox(self):
            self.task_listbox.delete(0, tk. END)
            for index, task in enumerate(self.tasks, start=1):
                status = "✅" if task["done"] else "❌"
                display_text = f"{index}.{task['task']} [{status}]"
                self.task_listbox.insert(tk.END, display_text)

    def add_task(self):

        task_text = self.task_entry.get().strip()
        if not task_text:
            self.info_label.config(text = "Please enter a task first.")
            return
        
        self.tasks.append({"task" : task_text, "done": False})
        self.task_entry.delete(0, tk.END)
        self.info_label.config(text = f"Task '{task_text}' added!")
        self.refresh_listbox()
    
    def get_selected_index(self):

        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a task first.")
            return None
        return selection[0]
    
    def mark_done(self):

        index = self.get_selected_index()
        if index is None:
            return
        self.tasks[index] ["done"] = True
        self.info_label.config(text = "Task marked as done!")
        self.refresh_listbox()

    def delete_task(self):

        index = self.get_selected_index()
        if index is None:
            return
        removed = self.tasks.pop(index)
        self.info_label.config(text = f"Deleted task: {removed['task']}")
        self.refresh_listbox()

    def clear_all(self):

        if not self.tasks:
            self.info_label.config(text = "No tasks to clear.")
            return
        if messagebox.askyesno ("Clear All", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.refresh_listbox()
            self.info_label.config(text = "All tasks cleared!")

if __name__ == "__main__":
        root = tk.Tk()
        app = TodoApp(root)
        root.mainloop()    