"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
import os
import shutil


def sort_files(path: str):
    # Создаем словарь с расширениями файлов для каждой группы
    file_groups = {
        'video': ['.mp4', '.avi', '.mov'],
        'images': ['.jpg', '.jpeg', '.png'],
        'text': ['.txt', '.doc', '.docx']
    }

    # Создаем папки для каждой группы, если они еще не существуют
    for group in file_groups:
        group_path = os.path.join(path, group)
        if not os.path.exists(group_path):
            os.makedirs(group_path)

    # Перемещаем файлы в соответствующие папки
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1]
            for group, extensions in file_groups.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(path, group, filename))
                    break


# sort_files('test_dir')
