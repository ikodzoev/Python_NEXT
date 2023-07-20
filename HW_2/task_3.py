"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions."""
import fractions

a: str = str(input("Введите числитель первой дроби "))
b: str = str(input("Введите знаменатель первой дроби "))
c: str = str(input("Введите числитель второй дроби "))
d: str = str(input("Введите знаменатель второй дроби "))
num1: int = int(a)
num2: int = int(b)
num3: int = int(c)
num4: int = int(d)

res1 = (num1 / num2) + (num3 / num4)
res2 = (num1 / num2) * (num3 / num4)
print(res1)
print(res2)
fraction1 = fractions.Fraction(num1, num2)
fraction2 = fractions.Fraction(num3, num4)
res3 = fraction1 + fraction2
res4 = fraction1 * fraction2
print(res3)
print(res4)
