from operation import *

def menu():
    print("\n\t╔═════════════════ МЕНЮ ════════════════╗")
    print("\t║ [1]. Генерування даних до файлу \t║")
    print("\t║ [2]. Завантажити дані з файлу \t║")
    print("\t║ [3]. Зберегти дані до файлу \t\t║")
    print("\t║ [4]. Новий запис \t\t\t║")
    print("\t║ [5]. Пошук \t\t\t\t║")
    print("\t║ \t\t\t\t\t║")
    print("\t║ [0]. Вихід з програми \t\t║")
    print("\t╚═══════════════════════════════════════╝")
    print("\tВведіть число яке відповідає пункту меню...")


todo = DoIt()
person_list = []
while True:
    menu()
    key = input()
    if key == '0': break
    elif key == '1': todo.gen_data()
    elif key == '2':
        person_list = todo.load_data()
        print(f'LOAD >> Кількість завантажених записів - {len(person_list)}')
    elif key == '3':
        if person_list:
            todo.save_data(person_list)
            print(f'SAVE << Кількість збережених записів - {len(person_list)}')
        else:
            print(f"Немає даних для збереження...")
    elif key == '4':
        new_person = todo.new_record()
        person_list.append(new_person)
        print(f'ADD << Дані про новий запис: {new_person}')
    elif key == '5':
        print(f'SEARCH >>', end=' ')
        todo.search(person_list)
