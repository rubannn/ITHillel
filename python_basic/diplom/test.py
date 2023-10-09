import random

def generate_patronymic(name, gender):
    male_suffixes = ["ович", "евич", "йович", "ич"]
    female_suffixes = ["івна", "евна", "инична", "ична"]

    if gender.lower() == "male":
        suffixes = male_suffixes
    elif gender.lower() == "female":
        suffixes = female_suffixes
    else:
        raise ValueError("Некоректна стать. Використайте 'male' або 'female'.")

    # Виправлення для імені "Іван"
    if name == "Іван":
        patronymic = "ович"
    else:
        # Вибір випадкового суфіксу та генерація по-батькові
        patronymic = random.choice(suffixes)

    full_patronymic = name + patronymic
    return full_patronymic

# Приклад використання
name = "Микола"
gender = "male"
patronymic = generate_patronymic(name, gender)
print("По-батькові:", patronymic)
