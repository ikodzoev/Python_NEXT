"""Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции. """

import random


def fill_file(filename: str, num_lines: int):
    with open(filename, 'a') as f:
        for _ in range(num_lines):
            int_num = random.randint(-1000, 1000)
            float_num = random.uniform(-1000, 1000)
            f.write(f'{int_num}|{float_num:.2f}\n')


# пример файла для заполнения под именем numbers.txt с 10-ю строками:
fill_file('numbers.txt', 10)
