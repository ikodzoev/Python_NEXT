"""
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import pickle
import csv
with open('new_json.pickle', 'rb') as f:
    data = pickle.load(f)

with open("new_c.csv", "w", encoding="utf-8") as c:
    writer = csv.writer(c)
    for row in data:
        writer.writerow(row)