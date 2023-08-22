"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков -
архивов
📌 list-архивы также являются свойствами экземпляра
"""


class Archive:
    """Класс для архивирования чисел и строк."""

    nums_archive = []
    strs_archive = []
    last_num = None
    last_str = None

    def __init__(self, num, new_str):
        """Инициализирует атрибуты num и new_str и обновляет архивы."""
        self.num = num
        self.new_str = new_str

        if Archive.last_num is not None:
            Archive.nums_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.strs_archive.append(Archive.last_str)

        Archive.last_num = num
        Archive.last_str = new_str

    def print_info(self):
        """Выводит информацию об объекте на печать."""
        print(f'Число: {self.num}')
        print(f'Строка: {self.new_str}')
        print(f'Архив чисел: {Archive.nums_archive}')
        print(f'Архив строк: {Archive.strs_archive}')


if __name__ == '__main__':
    arc1 = Archive(1, "Строка 1")
    arc1.print_info()

    arc2 = Archive(2, "Текст 2")
    arc2.print_info()

    arc3 = Archive(3, "Symbols 3")
    arc3.print_info()
