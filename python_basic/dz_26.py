# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум додавання,
# віднімання, ділення, множення, зведення в ступінь та вилучення квадратного кореня.

# Обернути кожен метод у блок try/except і зробити обробку кількох винятків, як мінімум ділення на 0.
# Створити свій виняток, наприклад, зведення в негативний ступінь.

class UserError(UserWarning):
    def __init__(self):
        super().__init__("число повинно бути додатним...")


class Calc:
    @staticmethod
    def check(x):
        return isinstance(x, int|float) and (x == 0 or not isinstance(x, bool))

    def adds(self, a, b):
        try:
            if not (self.check(a) and self.check(b)):
                raise TypeError
            return a + b
        except TypeError:
            print('аргументи повинні бути числом')
            return 'error'

    def subs(self, a, b):
        try:
            if not (self.check(a) and self.check(b)):
                raise TypeError
            return a - b
        except TypeError:
            print('аргументи повинні бути числом')
            return 'error'

    def muls(self, a, b):
        try:
            if not (self.check(a) and self.check(b)):
                raise TypeError
            return a * b
        except TypeError:
            print('аргументи повинні бути числом')
            return 'error'

    def divs(self, a, b):
        try:
            if not (self.check(a) and self.check(b)):
                raise TypeError
            return a / b
        except ZeroDivisionError:
            return 'важко ділити на 0...'
        except TypeError:
            print('аргументи повинні бути числом')
            return 'error'


    def pows(self, a, pw):
        try:
            if not (self.check(a) and self.check(pw)):
                raise TypeError
            return a ** pw
        except TypeError:
            print('аргументы повинні бути числом')
            return 'error'

    def sqrts(self, a):
        try:
            if not self.check(a):
                raise TypeError
            elif a < 0:
                raise UserError
            return a ** 0.5
        except UserError as e:
            return e
        except TypeError:
            print('аргумент повинен бути числом')
            return 'error'

calc = Calc()
print(f'{calc.adds(1, 2)=}')
print(f'{calc.subs(2, 3)=}')
print(f'{calc.muls(3, 4)=}')
print(f'{calc.divs(4, 5)=}')
print(f'{calc.pows(5, 6)=}')
print(f'{calc.sqrts(6)=}')

print(f'\n{calc.divs(3, 0)=}')
print(f'{calc.sqrts(-6)=}')
print(f'{calc.sqrts("ww")=}')
print(f'{calc.pows(5, True)=}')
print(f'{calc.adds([1], 2)=}')
