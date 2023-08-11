"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""

import json
import hashlib


def csv_to_json(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            values = line.strip().split(',')
            row = dict(zip(header, values))
            row['id'] = row['id'].zfill(10)
            row['name'] = row['name'].capitalize()
            row['hash'] = hashlib.sha256((row['name'] + row['id']).encode()).hexdigest()
            data.append(row)
    with open(output_file, 'w') as f:
        for row in data:
            json.dump(row, f)
            f.write('\n')


# csv_to_json('/path/to/input.csv', '/path/to/output.json')
