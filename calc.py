import tkinter as tk

class CalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")

        # Создаем текстовое поле для отображения результата
        self.result_entry = tk.Entry(self.window, width=30)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Создаем кнопки с цифрами и операторами
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("=", 5, 0, columnspan=4)

        self.expression = ""

        self.window.mainloop()

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.window, text=text, width=5, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan)

    def button_click(self, text):
        if text == "C":
            self.expression = ""
            self.result_entry.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.expression)
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, str(result))
                self.expression = str(result)
            except:
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += text
            self.result_entry.insert(tk.END, text)

if __name__ == "__main__":
    app = CalculatorApp()