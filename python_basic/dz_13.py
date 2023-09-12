# Написати декоратор до 2-х будь-яких функцій, який би рахував та виводив час їх виконання.

# Підсказка:
# from datetime import datetime
# now = datetime.now()

from time import time
from random import randint


def worktime(func):
    def wrapper():
        start = time()
        deep = randint(500, 1000)
        result = func(deep)
        finish = time()
        print(f'Function name: {func.__name__}. Execute time is {(finish - start):.4f}')
        return result
    return wrapper


@worktime
def rand_int_list(deep):
    return [randint(-10, 10) for _ in range(deep)]


@worktime
def rand_str_list(deep):
    res = []
    for _ in range(deep):
        t = [chr(randint(ord('a'), ord('z'))) for c in range(randint(3, 7))]
        res.append(''.join(t))
    return res


rand_int_list()
rand_str_list()

# print(rand_int_list())
# print(rand_str_list())
