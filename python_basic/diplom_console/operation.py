from person import Person
import os, random
import csv
from faker import Faker

class DoIt:
    SEX = ['m', 'f']
    OUTFILE = '/output/diplom_data_console.csv'

    @staticmethod
    def get_surname(fname):
        sur_list = []
        with open(f'{fname}', 'r', encoding='utf-8') as f:
            for s in f.readlines():
                sur_list.append(s.strip('\n'))
        return random.choice(sur_list)

    @staticmethod
    def get_name(is_male, fake, surname_path):
        surname_female = DoIt.get_surname(f'{surname_path}ua_surname_f.txt')
        surname_male = DoIt.get_surname(f'{surname_path}ua_surname_m.txt')
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

    @staticmethod
    def str_date(date):
        return date.strftime("%d.%m.%Y") if date else ''

    def gen_data(self):
        num = int(input("Оберіть кількість записів для генерування: "))
        path = os.getcwd()
        surname_path = f'{path}/python_basic/diplom/'

        fake = Faker(['uk_UA'])

        with open(f"{path}{DoIt.OUTFILE}", 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            for _ in range(num):
                gender = random.choice(DoIt.SEX)
                name = self.get_name(gender == DoIt.SEX[0], fake, surname_path)

                born = fake.date_of_birth(None, 20, 70)
                death = fake.date_between(born) if random.choice([True, False]) else None

                csv_data = [*name,
                            self.str_date(born),
                            self.str_date(death) if death else '',
                            gender]
                writer.writerow(csv_data)

    def load_data(self):
        path = os.getcwd()
        file_path = f"{path}{DoIt.OUTFILE}"
        load_data = []
        if not os.path.exists(file_path):
            open(file_path, 'w').close()

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                last_name, first_name, mid_name, dt_born, dt_death, gender = row
                load_data.append(
                    Person(
                        last_name=last_name,
                        first_name=first_name,
                        mid_name=mid_name,
                        gender= gender == 'm',
                        dt_born=dt_born,
                        dt_death=dt_death or None)
                    )
        return load_data

    def save_data(self, data):
        path = os.getcwd()

        with open(f"{path}{DoIt.OUTFILE}", 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',', lineterminator='\n')
            for pers in data:
                csv_data = [pers.last_name, pers.first_name, pers.mid_name,
                            self.str_date(pers.born),
                            self.str_date(pers.death),
                            DoIt.SEX[not pers.gender]]
                writer.writerow(csv_data)


    def new_record(self):
        print("[ Дані про особу ]")
        last_name = input("Прізвищe: ")
        first_name = input("Ім\'я: ")
        mid_name = input("По-батькові: ")
        gender = int(input("Стать (1 - чоловік, 0 - жінка): ")) == 1
        dt_born = input("Дата народження: ")
        dt_death = input("Дата смерті: ")
        return Person(last_name=last_name,
                      first_name=first_name,
                      mid_name=mid_name,
                      gender= gender,
                      dt_born=dt_born,
                      dt_death=dt_death or None)

    def search(self, data):
        if data:
            pattern = input("Параметри пошуку: ").lower()
            count = 0
            res = []
            for pers in data:
                if pattern in pers.fio.lower():
                    count += 1
                    res.append(pers)
            print(f'Кількість знайдених записів - {count}')
            if res:
                for pers in res:
                    print('\t', pers)
        else:
            print("Немає даних для пошуку. Завантажте дані")
