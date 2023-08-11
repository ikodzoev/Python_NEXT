"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. """

from pathlib import Path
import json
import csv
import pickle


def get_dir_info(dir_path):
    dir_path = Path(dir_path)
    result = []
    for path in dir_path.rglob('*'):
        if path.is_file():
            result.append({
                'name': path.name,
                'path': str(path),
                'type': 'file',
                'parent': str(path.parent),
                'size': path.stat().st_size
            })
        elif path.is_dir():
            dir_size = sum(p.stat().st_size for p in path.glob('**/*') if p.is_file())
            result.append({
                'name': path.name,
                'path': str(path),
                'type': 'directory',
                'parent': str(path.parent),
                'size': dir_size
            })
    return result


def save_to_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def save_to_csv(data, file_path):
    with open(file_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'path', 'type', 'parent', 'size'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def save_to_pickle(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


# dir_info = get_dir_info('/HW_7')
# save_to_json(dir_info, 'D:/GB/Study/Pythons/Python_NEXT/HWs/HW_7/output.json')
# save_to_csv(dir_info, 'D:/GB/Study/Pythons/Python_NEXT/HWs/HW_7/output.csv')
# save_to_pickle(dir_info, 'D:/GB/Study/Pythons/Python_NEXT/HWs/HW_7/output.pickle')
