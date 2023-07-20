"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

hex_num = "0123456789abcdef"
dec_num = int(input("Введите число: "))
# print(hex(dec_num))
hex_str = ""
while dec_num > 0:
    hex_str = hex_num[dec_num % 16] + hex_str
    dec_num = dec_num // 16
print(hex_str)
