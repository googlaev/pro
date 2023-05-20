import tkinter as tk

class CalorieCalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор калорий")

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

        # Создаем текстовое поле для ввода возраста
        self.age_label = tk.Label(self.window, text="Возраст:")
        self.age_label.grid(row=2, column=0)
        self.age_entry = tk.Entry(self.window, width=10)
        self.age_entry.grid(row=2, column=1)

        # Создаем текстовое поле для выбора пола
        self.gender_label = tk.Label(self.window, text="Пол:")
        self.gender_label.grid(row=3, column=0)
        self.gender_var = tk.StringVar()
        self.gender_var.set("male")
        self.male_radio = tk.Radiobutton(self.window, text="Мужской", variable=self.gender_var, value="male")
        self.male_radio.grid(row=3, column=1)
        self.female_radio = tk.Radiobutton(self.window, text="Женский", variable=self.gender_var, value="female")
        self.female_radio.grid(row=4, column=1)

        # Создаем текстовое поле для отображения результата
        self.result_label = tk.Label(self.window, text="Рекомендуемое количество калорий:")
        self.result_label.grid(row=5, column=0)
        self.result_entry = tk.Entry(self.window, width=10)
        self.result_entry.grid(row=5, column=1)

        # Создаем кнопку для расчета
        self.calculate_button = tk.Button(self.window, text="Рассчитать", command=self.calculate_calories)
        self.calculate_button.grid(row=6, column=0, columnspan=2)

        self.window.mainloop()

    def calculate_calories(self):
        # Получаем значения из текстовых полей
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        age = int(self.age_entry.get())
        gender = self.gender_var.get()

        # Рассчитываем количество калорий
        if gender == "male":
            calories = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        else:
            calories = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

        # Отображаем результат в текстовом поле
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(round(calories)))

if __name__ == "__main__":
    app = CalorieCalculatorApp()