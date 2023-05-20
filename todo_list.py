import tkinter as tk

class TodoListApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Список дел")

        # Создаем текстовое поле для ввода новых задач
        self.task_entry = tk.Entry(self.window, width=30)
        self.task_entry.grid(row=0, column=0)

        # Создаем кнопку "Добавить задачу"
        self.add_task_button = tk.Button(self.window, text="Добавить задачу", command=self.add_task)
        self.add_task_button.grid(row=0, column=1)

        # Создаем список задач
        self.task_listbox = tk.Listbox(self.window, height=10, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2)

        # Создаем кнопку "Удалить задачу"
        self.delete_task_button = tk.Button(self.window, text="Удалить задачу", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=0)

        # Создаем кнопПродолжение кода:

        # Создаем кнопку "Очистить список"
        self.clear_list_button = tk.Button(self.window, text="Очистить список", command=self.clear_list)
        self.clear_list_button.grid(row=2, column=1)

        self.window.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            self.task_listbox.delete(task_index)

    def clear_list(self):
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    app = TodoListApp()