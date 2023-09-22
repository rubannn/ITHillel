# Створити словник як ключ якого буде 6-ти значне число,
# а в якості значень кортеж що складається
# з 2-х елементів - ім'я (str), вік (int).
# Зробити близько 5-6 елементів словника.
# Записати цей словник на диск у json-файл.

import json
from random import randint
from faker import Faker
import os

path = os.getcwd()
fake = Faker(['uk_UA'])

res = []
for _ in range(16):
    tuple = (fake.name(), randint(20, 50))
    res.append({f'{randint(100_000, 999_999)}': tuple})

json_obj = json.dumps(res, indent=2)
with open(f"{path}/output/data.json", "w", encoding="utf-8") as f:
    f.write(json_obj)
