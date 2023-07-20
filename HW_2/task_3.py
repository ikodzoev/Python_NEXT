"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions."""
import fractions

a = input("Введите числитель первой дроби ")
b = input("Введите знаменатель первой дроби ")
c = input("Введите числитель второй дроби ")
d = input("Введите знаменатель второй дроби ")

num1, num2, num3, num4 = int(a), int(b), int(c), int(d)

res1 = (num1 / num2) + (num3 / num4)
res2 = (num1 / num2) * (num3 / num4)
print(f"{res1}\n{res2}")
fraction1 = fractions.Fraction(num1, num2)
fraction2 = fractions.Fraction(num3, num4)
res3 = fraction1 + fraction2
res4 = fraction1 * fraction2
print(f"{res3}\n{res4}")
