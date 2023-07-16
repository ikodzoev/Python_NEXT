"""
Задание №5
Работа в консоли в режиме интерпретатора Python.
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""

n = int(input("Введите n: "))
e = int(input("Введите e: "))

sum_val = 0
el = 0

while el <= n:
    el += 1
    if el % 2 == 0:
        if el % e == 0:
            continue
        sum_val += el

print(sum_val)


while el <= n:
    if el % 2 == 0 and el % e == 0:
        sum_val += el

print(sum_val)
