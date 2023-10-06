import random
from faker import Faker
from datetime import datetime, date
import csv
import os


def get_age(born, death):
    if death:
        today = death
    else:
        today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

path = os.getcwd()
fake = Faker(['uk_UA'])

sex = ["чоловік", "жінка"]
num = 50

with open(f"{path}/output/diplom_data.csv", 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\n')
    for x in range(num):
        gender = random.choice(sex)
        if gender == sex[0]:
            name = fake.name_male()
        else:
            name = fake.name_female()
        born = fake.date_of_birth(None, 20, 70)
        death = fake.date_between(born) if random.choice([True, False]) else None
        name = [nm for nm in name.split() if 'пан' not in nm]
        csv_data = [*name, born, death, gender, get_age(born, death)]
        writer.writerow(csv_data)
