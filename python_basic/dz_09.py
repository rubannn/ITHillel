# Наведено список чисел. Порахувати скільки разів трапляється кожне число.
# Використовувати функцію підрахунку.

# Підказка: для зберігання даних використовувати словник (ключ - саме число,
# а значення - скільки разів воно трапляється). Для перевірки знаходження
# елемента у словнику використовувати метод get(), або оператор in.

# *Додаткові не обов'язкові умови:

# - Початковий список розміром 200 елементів формується з чисел
# від 1 до 10 включно взятих випадковим чином;
# - сформувати підсумковий словник (де ключ це саме число, а значення це
# у повторень даного числа в первісному списку) за допомогою
# конструкції "генератор словників";
# - підсумковий висновок відсортувати по порядку зростання числа, наприклад:
# Число 1 зустрічається у первісному списку 10 разів
# Число 2 зустрічається у початковому списку 3 рази
# Число 3 зустрічається у початковому списку 14 разів
# Число 4 зустрічається у початковому списку 1 раз
# і т.д.

# - використовувати лямбда-функцію для того, щоб визначити яке слово треба
# написати для конкретного числа: "раз", "разів" або "раза"

from random import randint


def newcounter(lst, x):
    return sum([1 for t in lst if t == x])

word = lambda x: 'рази' if x % 10 in (2, 3, 4) else 'раз' if x in (1, ) else 'разів'

numlist = []
for _ in range(200):
    numlist.append(randint(1, 10))

numdict = {x: newcounter(numlist, x) for x in set(numlist)}
for el, cnt in numdict.items():
    print(f"Число {el} зустрічається у первісному списку {cnt} {word(cnt)}")