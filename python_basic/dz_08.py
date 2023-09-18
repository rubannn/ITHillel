# Зробити програму за допомогою функцій/функцій у якій потрібно буде
# вгадувати число.
# *Алгоритм програми можна зробити будь-яким, на розсуд виконавця.

# Один з варіантів:
# - з допомогою зовнішньої функції random створити довільне число,
# наприклад у діапазоні від 1 до 10.
# - У циклі запропонувати користувачеві вгадати загадане число за
# певну кількість спроб, наприклад 3.
# Якщо введене число угадано, то повідомити про це і запропонувати
# зіграти заново.
# Якщо ж не вгадано, то повідомити задумане число більше чи менше.

# Кожен із пунктів можна організувати як окремої функції, основний
# алгоритм можна розбити на ще кілька функцій.

from random import randint


def check(num, x):
    if num == x:
        print('You win!')
        return True
    txt = 'higher' if num > x else 'less'
    print(f'\tYou number should be {txt}... ')
    return False


while True:
    number = randint(1, 10)
    count = 0
    while True:
        t = int(input('Input number between 1 - 10: '))
        count += 1
        if check(number, t):
            print(f'You made {count} tries\n')
            break

    print('New game?')
    if input('Input Y/N: ').lower() in 'Nn':
        break
