import tkinter as tk
from tkinter import *
from functools import partial
from gendata import gen_random_data, load_data


# Создается новое окно с заголовком "Введите домашний адрес".
window = tk.Tk()
window.title("Diplom Form")

CURSOR = 0
REC_COUNT = 0
# Создается новая рамка `frm_form` для ярлыков с текстом и
# Однострочных полей для ввода информации об адресе.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3, name='frm_form')
# Помещает рамку на окно приложения.
frm_form.pack()

# Список ярлыков полей.
ed_lastname = tk.StringVar()
ed_firstname = tk.StringVar()
ed_middlename = tk.StringVar()
ed_dtborn = tk.StringVar()
ed_dtdeath = tk.StringVar()
ed_gender = tk.StringVar()
lbl_age = tk.StringVar()
lbl_rec = tk.StringVar(value="0 / 0")

labels = [
    ("Прізвище:", "last_name", ed_lastname),
    ("Ім\'я:", "first_name", ed_firstname),
    ("По-батькові:", "middle_name", ed_middlename),
    ("Дата народження:", "dt_born", ed_dtborn),
    ("Дата смерті:", "dt_death", ed_dtdeath),
    ("Стать:", "gender", ed_gender),
    ("Вік:", "age", lbl_age),
]
all_data = []

def cur_data(data, num):
    num -= 1
    ed_lastname.set(data[num][0])
    ed_firstname.set(data[num][1])
    ed_middlename.set(data[num][2])
    ed_dtborn.set(data[num][3])
    ed_dtdeath.set(data[num][4])
    ed_gender.set(data[num][5])
    lbl_age.set(data[num][6])
    lbl_rec.set(f"{CURSOR} / {REC_COUNT}")


def btn_load_click():
    global CURSOR
    global REC_COUNT
    global all_data
    all_data = load_data()
    REC_COUNT = len(all_data)
    CURSOR = 1
    cur_data(all_data, CURSOR)

def btn_next_click():
    global CURSOR
    if CURSOR == REC_COUNT:
        CURSOR = 1
    else:
        CURSOR += 1
    cur_data(all_data, CURSOR)

def btn_prev_click():
    global CURSOR
    if CURSOR == 1:
        CURSOR = REC_COUNT
    else:
        CURSOR -= 1
    cur_data(all_data, CURSOR)

def btn_new_click():
    cur_data([['' for _ in range(len(labels))]], 1)

def btn_save_click():
    all_data.append([
        [ed_lastname.get(), ed_firstname.get(), ed_middlename.get(),
         ed_dtborn.get(), ed_dtdeath.get(), ed_gender.get(), lbl_age.get()]
    ])
    print(all_data)


# Цикл для списка ярлыков полей.
obj_entry = []
for idx, item in enumerate(labels):
    text, objname, txtvar = item
    # Создает ярлык с текстом из списка ярлыков.
    label = tk.Label(master=frm_form, text=text)
    # Создает текстовое поле которая соответствует ярлыку.
    if idx == len(labels) - 1:
        entry = tk.Label(master=frm_form, width=50, text="???", name=objname, textvariable=txtvar)
    else:
        entry = tk.Entry(master=frm_form, width=50, name=objname, textvariable=txtvar)
    # Использует менеджер геометрии grid для размещения ярлыков и
    # текстовых полей в строку, чей индекс равен idx.
    label.grid(row=idx, column=0, sticky="e")
    entry.grid(row=idx, column=1)


frm_panel = tk.Frame(name='panel1')
frm_panel.pack(fill=tk.X, ipadx=5, ipady=5)

btn_prev = tk.Button(master=frm_panel, text="<<", command=btn_prev_click)
btn_prev.pack(side=tk.LEFT, padx=10, ipadx=10)

lbl_record = tk.Label(master=frm_panel, width=10, textvariable=lbl_rec)
lbl_record.pack(side=tk.LEFT, padx=10, ipadx=10)

btn_next = tk.Button(master=frm_panel, text=">>", command=btn_next_click)
btn_next.pack(side=tk.RIGHT, padx=10, ipadx=10)


frm_buttons = tk.Frame(name='panel2')
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_submit = tk.Button(master=frm_buttons, text="New", command=btn_new_click)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Save", command=btn_save_click)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

data_rows = 15
btn_gen = tk.Button(master=frm_buttons, text="Generate Data", command=partial(gen_random_data, data_rows))
btn_gen.pack(side=tk.LEFT, padx=10)

btn_load = tk.Button(master=frm_buttons, text="Load Data", command=btn_load_click)
btn_load.pack(side=tk.LEFT, padx=10)

window.mainloop()
