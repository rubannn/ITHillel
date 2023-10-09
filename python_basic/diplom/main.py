import tkinter as tk
from functools import partial
from gendata import gen_random_data

# Создается новое окно с заголовком "Введите домашний адрес".
window = tk.Tk()
window.title("Diplom Form")

# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Помещает рамку на окно приложения.
frm_form.pack()

# Список ярлыков полей.
labels = [
    "Прізвище:",
    "Ім\'я:",
    "По-батькові:",
    "Дата народження:",
    "Дата смерті:",
    "Стать:",
    "Вік людини:",
]

# Цикл для списка ярлыков полей.
for idx, text in enumerate(labels):
    # Создает ярлык с текстом из списка ярлыков.
    label = tk.Label(master=frm_form, text=text)
    # Создает текстовое поле которая соответствует ярлыку.
    if idx == len(labels) - 1:
        entry = tk.Label(master=frm_form, width=50, text="???")
    else:
        entry = tk.Entry(master=frm_form, width=50)
    # Использует менеджер геометрии grid для размещения ярлыков и
    # текстовых полей в строку, чей индекс равен idx.
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)

# Создает новую рамку `frm_buttons` для размещения в ней
# кнопок "Отправить" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

data_rows = 15
btn_gen = tk.Button(master=frm_buttons, text="Generate Data", command=partial(gen_random_data, data_rows))
btn_gen.pack(side=tk.LEFT, padx=10)

window.mainloop()
