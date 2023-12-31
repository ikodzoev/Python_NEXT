""" ✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня."""

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b ** 2 - 4 * a * c

if d == 0:
    x = -b / (2 * a)
    print("Один действительный корень: ", x)
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(x1, x2)
