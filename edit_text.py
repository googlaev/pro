import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class TextEditorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Текстовый редактор")

        # Создаем текстовое поле для ввода и отображения текста
        self.text_box = tk.Text(self.window, height=30, width=60)
        self.text_box.pack()

        # Создаем меню
        self.menu_bar = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Выход", command=self.window.quit)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Отменить", command=self.undo)
        self.edit_menu.add_command(label="Вырезать", command=self.cut)
        self.edit_menu.add_command(label="Копировать", command=self.copy)
        self.edit_menu.add_command(label="Вставить", command=self.paste)
        self.menu_bar.add_cascade(label="Правка", menu=self.edit_menu)

        self.window.config(menu=self.menu_bar)

        self.window.mainloop()

    def open_file(self):
        file_path = askopenfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            self.text_box.delete(1.0, tk.END)
            with open(file_path, "r") as file:
                text = file.read()
                self.text_box.insert(tk.END, text)

    def save_file(self):
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                text = self.text_box.get(1.0, tk.END)
                file.write(text)

    def undo(self):
        self.text_box.edit_undo()

    def redo(self):
        self.text_box.edit_redo()

    def cut(self):
        self.text_box.event_generate("<<Cut>>")

    def copy(self,):
        self.text_box.event_generate("<<Copy>>")

    def paste(self):
        self.text_box.event_generate("<<Paste>>")

if __name__ == "__main__":
    app = TextEditorApp()