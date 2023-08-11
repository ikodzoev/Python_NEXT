"""✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл"""

import random
import string


def pseudo_names(filename: str, num_names: int):
    vowels = 'AEIOU'
    consonants = ''.join(set(string.ascii_uppercase) - set(vowels))

    with open(filename, 'w') as f:
        for _ in range(num_names):
            # Генерируем случайную длину имени в диапазоне от 4 до 7
            name_len = random.randint(4, 7)

            # Генерируем случайное имя с заглавной буквой
            name = random.choice(string.ascii_uppercase)
            for _ in range(name_len - 1):
                if name[-1] in vowels:
                    name += random.choice(consonants)
                else:
                    name += random.choice(vowels + consonants)

            # Сохраняем сгенерированное имя в файл
            f.write(name + '\n')


# пример генерации файла для записи в него 10 псевдоимён:
pseudo_names('names.txt', 10)
