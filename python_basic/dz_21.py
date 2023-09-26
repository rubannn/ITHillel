# Створити батьківський клас auto, який має атрибути:
# brand, age, cоlor, mark і weight.
# А також методи: move, birthday і stop.
# Методи move і stop виводять повідомлення на екран «move» та «stop»,
# а birthday збільшує атрибут age на 1.
# Атрибути brand, age та mark є обов'язковими під час оголошення об'єкта.

class Auto():
    def __init__(self, brand, age, color, mark, weight) -> None:
        self.brand = brand,
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
