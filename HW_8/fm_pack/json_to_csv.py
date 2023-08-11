"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import json
import csv


def save_to_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['access_level', 'id', 'name'])
        for access_level, users in data.items():
            for get_id, name in users.items():
                writer.writerow([access_level, get_id, name])

# save_to_csv('/fm_pack/test_dir/data.json', '/fm_pack/test_dir/data.csv')
