import time


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


class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight) -> None:
        super().__init__(brand, age, color, mark, weight)
        # max_load

    def move(self):
        super().move()
        print('attention')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, cоlor, mark, weight) -> None:
        super().__init__(brand, age, cоlor, mark, weight)
        # max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


truck1 = Truck()
truck2 = Truck()

car1 = Car()
car2 = Car()
