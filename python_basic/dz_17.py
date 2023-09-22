# Ввести з клавіатури 4 рядки та зберегти їх у 4 різні змінні.
# Створити файл і записати в нього перші 2 рядки та закрити файл.
# Потім відкрити файл на редагування і дозаписати 2 рядки, що залишилися.
# У підсумку файл має бути 4 рядки, кожен з яких
# повинен починатися з нового рядка.

import os

path = os.getcwd()

s1 = input("Input string1: ")
s2 = input("Input string2: ")
s3 = input("Input string3: ")
s4 = input("Input string4: ")

with open(f"{path}/output/dz_17.out", mode="w", encoding="utf-8") as f:
    f.write('\n'.join([s1, s2]))
    f.write('\n')

with open(f"{path}/output/dz_17.out", mode="a", encoding="utf-8") as f:
    f.write('\n'.join([s3, s4]))
    f.write('\n')
