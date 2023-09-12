# Даний список, що складається з даних різного типу.

# Повернути новий список, де за допомогою функції map() кожен елемент
# типу int початкового списку приведений до типу str, елементи решти
# всіх типів передаються в новий список без зміни їх типу.

# У якості вхідної функції в map використовувати lambda-функцію.

values = [1, 2, '3', 'forth', 'end', 99, True, None]


# def onlyint(x):
#     if type(x) is int:
#         return str(x)
#     return x

onlyint = lambda x: str(x) if type(x) is int else x
newlist = list(map(onlyint, values))
print(newlist)