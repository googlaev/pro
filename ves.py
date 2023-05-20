import tkinter as tk

class WeightHeightCalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор веса и роста")

        # Создаем текстовое поле для ввода веса
        self.weight_label = tk.Label(self.window, text="Вес (кг):")
        self.weight_label.grid(row=0, column=0)
        self.weight_entry = tk.Entry(self.window, width=10)
        self.weight_entry.grid(row=0, column=1)

        # Создаем текстовое поле для ввода роста
        self.height_label = tk.Label(self.window, text="Рост (см):")
        self.height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(self.window, width=10)
        self.height_entry.grid(row=1, column=1)

        # Создаем текстовое поле для отображения результата
        self.result_label = tk.Label(self.window, text="Индекс массы тела (BMI):")
        self.result_label.grid(row=2, column=0)
        self.result_entry = tk.Entry(self.window, width=10)
        self.result_entry.grid(row=2, column=1)

        # Создаем кнопку для расчета
        self.calculate_button = tk.Button(self.window, text="Рассчитать", command=self.calculate_bmi)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()

    def calculate_bmi(self):
        # Получаем значения из текстовых полей
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())

        # Рассчитываем индекс массы тела
        bmi = weight / ((height/100) ** 2)

        # Отображаем результат в текстовом поле
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(round(bmi, 2)))

if __name__ == "__main__":
    app = WeightHeightCalculatorApp()