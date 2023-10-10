# Створити генератор геометричної прогресії. При заданні початку
# прогресії -2 та кроку прогресії -5, генератор видає таку послідовність:

# -2, 10, -50, 250, -1250, 6250, ...

# При заданні початку прогресії 10 і кроку прогресії 3,
# генератор видає таку послідовність:

# 10, 30, 90, 270, 810, 2430, ...

def geom_generator(n, a, q):
    k = 0
    res = a
    while k < n:
        yield res
        res *= q
        k += 1


limit = 7
print([elem for elem in geom_generator(limit, -2, -5)])
print()
print([elem for elem in geom_generator(limit, 10, 3)])
