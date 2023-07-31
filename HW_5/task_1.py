"""✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""

import os


def split_path(abs_path):
    abs_path, filename = os.path.split(abs_path)
    filename, extension = os.path.splitext(filename)
    return abs_path, filename, extension


string = "D:/GB/Study/Pythons/Python_NEXT/requirements.txt"
print(f'Исходная строка: {string} \nКортеж: {split_path(string)}')
