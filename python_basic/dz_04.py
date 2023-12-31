# Написати програму яка отримає ім'я та вік користувача, перевіряє вік та
# видає вітальне повідомлення залежно від віку:
# - нуль чи не число: “Помилка, повторіть введення”;
# - більше нуля до 10 не включаючи: “Привіт, шкет «Ім'я»”;
# - від 10 до 18 включаючи: "Як справи, «Ім'я»?"
# - більше 18 і менше 100: "Що бажаєте «Ім'я»?
# - інакше: "«Ім'я», ви брешете - у наш час стільки не живуть..."

# *Додаткове не обов'язкове завдання:
# Програму необхідно загорнути у вічний цикл.
# Після чергового відпрацювання коду запитувати у користувача
# "Бажаєте вийти? (Д/Y)". Якщо відповідь буде буква "Д" або буква "Y"
# у будь-якому регістрі, то зробити вихід із вічного циклу.
# В іншому випадку продовжити виконання програми знову.

while True:
    user = input("Your name: ")
    age = input("Your age: ")
    age = int(age) if age.isnumeric() else '?'
    if age in (0, '?'):
        print("Помилка, повторіть введення...")
    elif 0 < age < 10:
        print(f"Привіт, шкет «{user}»")
    elif 10 <= age <= 18:
        print(f"Як справи, «{user}»?")
    elif 18 < age < 100:
        print(f"Що бажаєте, «{user}»?")
    else:
        print(f"«{user}», ви брешете - у наш час стільки не живуть...")

    is_exit = input("Бажаєте вийти? (Д/Y): ")
    if is_exit.upper() in "ДY":
        break
    else:
        print()
