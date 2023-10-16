from operation import *
import msvcrt

def menu():
    mnu_width = 55
    mnu = [
        (['╔','═','╗'], "", "<"),
        (['║','','║'], "-= МЕНЮ =-", "^"),
        (['╠','═','╣'], "", "<"),
        (['║','','║'], " [1]. Генерування даних до файлу", "<"),
        (['║','','║'], " [2]. Завантажити дані з файлу", "<"),
        (['║','','║'], " [3]. Зберегти дані до файлу", "<"),
        (['║','','║'], " [4]. Новий запис", "<"),
        (['║','','║'], " [5]. Пошук", "<"),
        (['║','','║'], " [6]. Друк поточних даних", "<"),
        (['╠','═','╣'], "", "<"),
        (['║','','║'], " [0]. Вихід з програми", "<"),
        (['╚','═','╝'], "", "<")
    ]

    for border, txt, op in mnu:
        left, symbol, right = border
        print(f"\t{left}{txt:{symbol}{op}{mnu_width}}{right}")

def goto_menu():
    print("\nДля повернення до головного меню натиснить клавішу \"Esc\"...")
    while True:
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            break


def main():
    todo = DoIt()
    person_list = []
    while True:
        menu()
        key = input("\tВведіть число яке відповідає пункту меню...  ")
        if key == "0":
            break
        elif key == "1":
            todo.gen_data()
        elif key == "2":
            person_list = todo.load_data()
        elif key == "3":
            if person_list:
                todo.save_data(person_list)
            else:
                print(f"Немає даних для збереження...")
        elif key == "4":
            new_person = todo.new_record()
            person_list.append(new_person)
            print(f"ADD << Дані про новий запис: {new_person}")
        elif key == "5":
            todo.search(person_list)
        elif key == "6":
            todo.show(person_list)

        goto_menu()


if __name__ == "__main__":
    main()
