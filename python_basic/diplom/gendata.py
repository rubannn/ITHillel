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


def get_surname(fname):
    sur_list = []
    with open(f'{fname}', 'r', encoding='utf-8') as f:
        for s in f.readlines():
            sur_list.append(s.strip('\n'))
    return random.choice(sur_list)


def get_name(is_male, fake, surname_path):
    surname_female = get_surname(f'{surname_path}ua_surname_f.txt')
    surname_male = get_surname(f'{surname_path}ua_surname_m.txt')
    name = []
    while len(name) < 2:
        if is_male:
            name = fake.name_male()
            surname = surname_male
        else:
            name = fake.name_female()
            surname = surname_female
        name = [nm for nm in name.split() if 'пан' not in nm]
    return (name[1], name[0], surname)

def gen_random_data(num):
    path = os.getcwd()
    surname_path = f'{path}/python_basic/diplom/'
    fake = Faker(['uk_UA'])

    sex = ["чоловік", "жінка"]

    with open(f"{path}/output/diplom_data.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        for x in range(num):
            gender = random.choice(sex)
            name = get_name(gender == sex[0], fake, surname_path)

            born = fake.date_of_birth(None, 20, 70)
            death = fake.date_between(born) if random.choice([True, False]) else None

            csv_data = [*name,
                        born.strftime("%d.%m.%Y"),
                        death.strftime("%d.%m.%Y") if death else '',
                        gender,
                        get_age(born, death)]
            writer.writerow(csv_data)

def load_data():
    path = os.getcwd()
    load_data = []
    with open(f"{path}/output/diplom_data.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            load_data.append(row)
    return load_data
