from datetime import date, datetime
import re

class Person:
    GENDER = ["жінка", "чоловік"]

    def __init__(self, first_name, gender, dt_born, last_name=None, mid_name=None, dt_death = None) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.mid_name = mid_name
        self.gender = gender
        self.born = self.date_valid(dt_born)
        self.death = self.date_valid(dt_death)

    @staticmethod
    def date_valid(str_date):
        if not str_date:
            return None
        try:
            str_date = '.'.join(re.split('\.| |-|/', str_date))
            res = datetime.strptime(str_date, '%d.%m.%Y')
        except ValueError:
            print('невірний формат дати')
            return None
        return res

    @property
    def fio(self):
        return f"{self.last_name or ''} {self.first_name} {self.mid_name or ''}".strip()

    @property
    def age(self):
        if self.born:
            today = self.death if self.death else date.today()
            return today.year - self.born.year - ((today.month, today.day) < (self.born.month, self.born.day))
        return None

    def __str__(self):
        if self.age and self.age >= 0:
            txt_age = 'роки' if self.age % 10 in (2, 3, 4) and self.age % 100 not in (12, 13, 14) \
                    else 'рік' if self.age % 10 == 1 and self.age % 100 != 11 \
                    else 'років'
            txt_born = 'Народи' + ('вся' if self.gender else 'лась')
            txt_born = f'{txt_born}: {self.born.strftime("%d.%m.%Y")}.'

            txt_death = ''
            if self.death:
                txt_death = 'Помер' if self.gender else 'Померла'
                txt_death = f'{txt_death}: {self.death.strftime("%d.%m.%Y")}.'

            return f'{self.fio} {self.age} {txt_age}, {Person.GENDER[self.gender]}. {txt_born} {txt_death}'
        return f'{self.fio}, {Person.GENDER[self.gender]}.'


# b = '13 07 1963'
# d = '22.11.1994'
# p1 = Person(first_name='Ярина', last_name='Вітрук', mid_name='Остапівна', dt_born=b, dt_death=d, gender=False)

# b = '10.07.1972'
# d = '28.02.2016'
# p2 = Person(first_name='Кирило', dt_born=b, dt_death=d, gender=True)
# print(p1, p2, sep='\n')
