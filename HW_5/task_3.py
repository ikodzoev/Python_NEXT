"""✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""

num = int(input("Введите число: "))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(num)))
