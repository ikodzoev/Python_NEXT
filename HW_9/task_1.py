"""Нахождение корней квадратного уравнения"""
import cmath


def roots_quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    return (x1, x2)


# Пример:
a = 1
b = 5
c = 6
x1, x2 = roots_quadratic(a, b, c)
print(f"Корни квадратного уравнения {a}x^2 + {b}x + {c} = 0: x1 = {x1}, x2 = {x2}")
