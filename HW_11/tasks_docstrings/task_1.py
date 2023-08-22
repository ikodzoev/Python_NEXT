"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания
(time.time)
"""

import time
from datetime import datetime


class MyStr(str):
    """Класс, наследующий от str и добавляющий дополнительные атрибуты и методы."""

    def __new__(cls, value, author_name):
        """Создает новый экземпляр класса MyStr с заданными значениями value и author_name."""
        my_srt = super().__new__(cls, value)
        my_srt.author_name = author_name
        my_srt.creation_time = datetime.now()
        return my_srt

    def print_info(self):
        """Выводит информацию об объекте на печать."""
        print(f'Значение: {self}')
        print(f'Автор: {self.author_name}')
        print(f'Время создания: {self.creation_time}')


if __name__ == '__main__':
    s = MyStr('Новая Строка Теста', 'Sergey')
    s.print_info()
    print(s.lower())
