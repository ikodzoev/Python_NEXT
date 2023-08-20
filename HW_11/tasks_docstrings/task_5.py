"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длину и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """Класс, представляющий прямоугольник."""

    def __init__(self, side_a, side_b=0):
        """Инициализирует атрибуты side_a и side_b."""
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """Возвращает площадь прямоугольника."""
        return self.side_a * self.side_b

    def __add__(self, other):
        """Возвращает новый прямоугольник с суммой периметров двух прямоугольников."""
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """Возвращает новый прямоугольник с разностью периметров двух прямоугольников."""
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def print_info(self):
        """Выводит информацию о прямоугольнике на печать."""
        print(f'Сторона a: {self.side_a}')
        print(f'Сторона b: {self.side_b}')
        print(f'Периметр: {self.get_perimeter()}')
        print(f'Площадь: {self.get_area()}')


if __name__ == '__main__':
    rectangle1 = Rectangle(7.3)
    rectangle1.print_info()

    rectangle2 = Rectangle(5.6, 10.2)
    rectangle2.print_info()

    rectangle3 = rectangle1 + rectangle2
    rectangle3.print_info()

    rectangle4 = rectangle3 - rectangle2
    rectangle4.print_info()

#
# class Rectangle:
#
#     def __init__(self, side_a, side_b=0):
#         self.side_a = side_a
#         if side_b == 0:
#             side_b = side_a
#         self.side_b = side_b
#
#     def get_perimeter(self):
#         return 2 * (self.side_a + self.side_b)
#
#     def get_area(self):
#         return self.side_a * self.side_b
#
#     def __add__(self, other):
#         # (self.side_a + other.side_a, self.side_b + other.side_b)
#         res = self.get_perimeter() + other.get_perimeter()
#         return Rectangle(res)
#
#     def __sub__(self, other):
#         res = abs(self.get_perimeter() - other.get_perimeter())
#         return Rectangle(res)
#
#
# rectangle1 = Rectangle(7.3)
# rectangle2 = Rectangle(5.6, 10.2)
# rectangle3 = rectangle1 + rectangle2
# rectangle4 = rectangle3 - rectangle2
#
# print(f'Периметр 1 прямоугольника = {rectangle1.get_perimeter():.2f}')
# print(f'Периметр 2 прямоугольника = {rectangle2.get_perimeter():.2f}')
#
# print(f'Периметр 3 прямоугольника = {rectangle3.get_perimeter():.2f}')
# print(f'Периметр 4 прямоугольника = {rectangle4.get_perimeter():.2f}')
