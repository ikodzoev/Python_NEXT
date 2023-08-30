"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
№ 3. Нахождение корней квадратного уравнения"""
import cmath


class InvalidEquation(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Ошибка: {self.message}"


def roots_quadratic(a, b, c):
    if a == 0:
        raise InvalidEquation("Коэффициент a не может быть равен нулю!")
    d = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    return (x1, x2)


try:
    roots = roots_quadratic(0, 2, 1)
except InvalidEquation as e:
    print(e)
