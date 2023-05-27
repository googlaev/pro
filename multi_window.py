import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Главное окно")
        self.btn1 = tk.Button(self.master, text="Открыть окно 1", command=self.open_window1)
        self.btn1.pack(pady=10)
        self.btn2 = tk.Button(self.master, text="Открыть окно 2", command=self.open_window2)
        self.btn2.pack(pady=10)

    def open_window1(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window1(self.new_window)

    def open_window2(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Window2(self.new_window)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Окно 1")
        self.label = tk.Label(self.master, text="Это окно 1")
        self.label.pack(pady=10)
        self.btn = tk.Button(self.master, text="Закрыть", command=self.close_window)
        self.btn.pack(pady=10)

    def close_window(self):
        self.master.destroy()

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Окно 2")
        self.label = tk.Label(self.master, text="Это окно 2")
        self.label.pack(pady=10)
        self.btn = tk.Button(self.master, text="Закрыть", command=self.close_window)
        self.btn.pack(pady=10)

    def close_window(self):
        self.master.destroy()

# Создание главного окна
root = tk.Tk()
app = App(root)

# Запуск основного цикла приложения
root.mainloop()