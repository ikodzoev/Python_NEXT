"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def convert_to_json(input_file, output_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            name, product = line.strip().split()
            data.append({'name': name.capitalize(), 'product': int(product)})
    with open(output_file, 'w') as f:
        for item in data:
            json.dump(item, f)
            f.write('\n')


# convert_to_json('/fm_pack/test_dir/input.txt', '/fm_pack/test_dir/output.json')
