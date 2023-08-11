"""Напишите декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""
import cmath
import csv


def from_csv(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(f"Корни квадратного уравнения {a}x^2 + {b}x + {c} = 0: x1 = {result[0]}, x2 = {result[1]}")

        return wrapper

    return decorator


@from_csv('data.csv')
def roots_quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    x1 = (-b - cmath.sqrt(d)) / (2 * a)
    x2 = (-b + cmath.sqrt(d)) / (2 * a)
    return (x1, x2)


roots_quadratic()
