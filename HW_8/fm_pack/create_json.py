"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключом для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

"""
import json


def create_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    while True:
        name = input('Введите имя: ')
        get_id = input('Введите идентификатор: ')
        access_level = int(input('Введите уровень доступа (от 1 до 7): '))
        if access_level not in data:
            data[access_level] = {}
        if get_id in data[access_level]:
            print(f'Идентификатор {get_id} уже существует!')
            continue
        data[access_level][get_id] = name
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        get_exit = input('Хотите выйти? (Yes/No): ')
        if get_exit.lower() == 'yes':
            break


# create_json('/fm_pack/test_dir/data.json')
