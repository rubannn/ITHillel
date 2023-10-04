# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум додавання,
# віднімання, ділення, множення, зведення в ступінь та вилучення квадратного кореня.

class Calc:
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __pow__(self, st):
        return self.value ** st
