import tkinter as tk
from tkinter import ttk

# Определение основного окна
root = tk.Tk()
root.title("Мое приложение")

# Создание виджета ноутбука
notebook = ttk.Notebook(root)

# Создание первой вкладки
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Вкладка 1")
tk.Label(tab1, text="Содержимое первой вкладки", padx=30, pady=30).pack()

# Создание второй вкладки
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Вкладка 2")
tk.Label(tab2, text="Содержимое второй вкладки", padx=30, pady=30).pack()

# Создание третьей вкладки
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Вкладка 3")
tk.Label(tab3, text="Содержимое третьей вкладки", padx=30, pady=30).pack()

# Создание четвертой вкладки
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Вкладка 4")
tk.Label(tab4, text="Содержимое четвертой вкладки", padx=30, pady=30).pack()

# Упаковка виджета ноутбука
notebook.pack(expand=True, fill="both")

# Запуск основного цикла приложения
root.mainloop()