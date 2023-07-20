""" ✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня."""
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d: complex = b * b - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Два различных вещественных корня: ", x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print("Один действительный корень: ", x)
else:
    get_real = -b / (2 * a)
    get_imag = math.sqrt(abs(d)) / (2 * a)
    x1 = complex(get_real, get_imag)
    x2 = complex(get_real, -get_imag)
    print("Комплексные корни: ", x1, x2)
