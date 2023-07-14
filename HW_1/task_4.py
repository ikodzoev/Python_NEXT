""""Задача № 4. Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2."""""
import math

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

disc = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % disc)
if disc > 0:
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif disc == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Решения не существует")
