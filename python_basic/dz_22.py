import time


class Auto():
    def __init__(self, brand, age, mark, color=None, weight=None) -> None:
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

    def __str__(self) -> str:
        return f'=={self.brand}== \n\t{self.age=} \n\t{self.mark=} \n\t{self.color=} \n\t{self.weight=}'


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color=None, weight=None) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print('attention')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color=None, weight=None) -> None:
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


truck1 = Truck('Man', 5, 'm1', 5000)
truck2 = Truck('KrAZ', 15, '03-p12', 15000, 'green', 5000)
print(truck1, truck2, sep='\n')

car1 = Car('Ford', 12, 'Focus', 180, 'red')
car2 = Car('Mazda', 7, 'CX-5', 201, weight=1500)
print(car1, car2, sep='\n')

truck2.load()
truck1.move()

car2.move()
