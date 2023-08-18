"""Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк."""
import csv
import random


def generate_csv(file_path, num_rows):
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        for _ in range(num_rows):
            row = [random.randint(0, 100) for _ in range(3)]
            writer.writerow(row)


# Пример:
generate_csv('output.csv', 1000)
