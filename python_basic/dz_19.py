import json
import random
import csv
import os


def gen_phones(count):
    code = ['095', '066', '098', '096', '050', '097']
    phone_exists = random.choices([True, False], weights=[0.75, 0.25], k=count)
    res = []
    for is_have in phone_exists:
        if is_have:
            num = random.randint(1, 10**7 - 1)
            num = f'{num // 10**5:02d}-{num // 10**3 % 100:02d}-{num % 1000:03d}'
            res.append(f'({random.choices(code)[0]}) {num}')
        else:
            res.append(None)
    return res


path = os.getcwd()
with open(f"{path}/output/data.json", 'r') as f:
    json_obj = json.load(f)

phones = gen_phones(len(json_obj))

with open(f"{path}/output/data.csv", 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['ID', 'Ім\'я', 'Вік', 'Телефон'])
    for jsn_num, jsn in enumerate(json_obj):
        for item in jsn:
            id, name, age = item, *jsn[item]
            csv_data = [id, name, age, phones[jsn_num]]
        writer.writerow(csv_data)
