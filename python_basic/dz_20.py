# Прочитати збережений csv-файл із попереднього завдання
# та зберегти дані в excel-файл.
# Крім віку - стовпець з цими даними не потрібний.

# *Додаткове завдання не обов'язкове до виконання:
# розгорнути таблицю на дев'яносто градусів (стовпці стають рядками,
# а рядки стовпцями).
# До завдання прикріплений приклад як має виглядати змісту підсумкового файлу.

# pip install pyexcel
# pip install pyexcel-xlsx

import csv
import os
import pyexcel as pe

path = f'{os.getcwd()}/output/'
csv_file = f'{path}data.csv'
xlxs_file = f'{path}data.xlsx'

newdata = [['id', 'name', 'phone']]
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        newdata.append([row['id'], row['name'], row['phone']])
    newdata = list(zip(*newdata))

headers = [''] + [f'person {i+1:03d}' for i in range(len(newdata[0]) - 1)]
sheet = pe.Sheet()
sheet.row += headers
for row in newdata:
    sheet.row += [c for c in row]
sheet.save_as(xlxs_file)
