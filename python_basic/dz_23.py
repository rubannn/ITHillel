# Для класу Circle, розглянутому на уроці, додати метод віднімання двох кіл.
# Віднімання радіусов зробити по модулю. Якщо два кола з однаковим значенням
# радіуса віднімаються, то результатом віднімання буде об'єкт классу Point.

import math

class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Circle(Point):
    def __init__(self, radius, x=0, y=0) -> None:
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __eq__(self, other) -> bool:
        return self.radius == other.radius

    def __add__(self, other):
        dot = super().__add__(other)
        return Circle(self.radius + other.radius, dot.x, dot.y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        r = abs(self.radius - other.radius)
        if r == 0:
            return Point(x, y)
        return Circle(r, x, y)

    def __str__(self):
        return f'Circle({self.x}, {self.y}, radius={self.radius})'


c1 = Circle(5, 1, 1)
c2 = Circle(3, 2, 2)

print(c1 + c2, type(c1 + c2))

c3 = Circle(5, 7, 13)
print(c1 - c2, type(c1 - c2))
print(c1)
print(c1 - c3, type(c1 - c3))
print(c1)
