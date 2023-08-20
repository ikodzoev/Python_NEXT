"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
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

    def __eq__(self, other):
        """Возвращает True, если площади двух прямоугольников равны, иначе False."""
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """Возвращает True, если площади двух прямоугольников не равны, иначе False."""
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        """Возвращает True, если площадь первого прямоугольника больше площади второго, иначе False."""
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """Возвращает True, если площадь первого прямоугольника больше или равна площади второго, иначе False."""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        """Возвращает True, если площадь первого прямоугольника меньше площади второго, иначе False."""
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """Возвращает True, если площадь первого прямоугольника меньше или равна площади второго, иначе False."""
        return self.get_area() <= other.get_area()

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

    print(f'({rectangle1.get_area():.2f} == {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
    print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
    print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
    print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
    print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
    print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)

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
#     def __eq__(self, other):  # равно ==
#         return self.get_area() == other.get_area()
#
#     def __ne__(self, other):  # неравно !=
#         return self.get_area() != other.get_area()
#
#     def __gt__(self, other):  # больше >
#         return self.get_area() > other.get_area()
#
#     def __ge__(self, other):  # больше или равно >=
#         return self.get_area() >= other.get_area()
#
#     def __lt__(self, other):  # метод меньше <
#         return self.get_area() < other.get_area()
#
#     def __le__(self, other):  # меньше или равно <=
#         return self.get_area() <= other.get_area()
#
#
#
# rectangle1 = Rectangle(7.3)
# rectangle2 = Rectangle(5.6, 10.2)
#
# print(f'площадь 1 прямоугольника = {rectangle1.get_area():.2f}')
# print(f'площадь 2 прямоугольника = {rectangle2.get_area():.2f}')
# # print(rectangle1 == rectangle2)
# print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
# print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
# print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
# print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
# print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
# print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)
