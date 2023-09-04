"""✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""
import doctest

num = int(input("Введите число: "))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(num)))


def fibonacci(n):
    """
    Генерирует числа Фибоначчи до указанного числа n.

    >>> list(fibonacci(5))
    [0, 1, 1, 2, 3]

    >>> list(fibonacci(10))
    [0, 1, 1, 2, 3, 5, 8]

    >>> list(fibonacci(1))
    [0]

    >>> list(fibonacci(0))
    []

    >>> list(fibonacci(-1))
    []
    """
    if n < 0:
        return []
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    num = int(input("Введите число: "))
    result = list(fibonacci(num))
    print(result)
# Добавим следующий код в конец файла для запуска doctest:
if __name__ == "__main__":
    doctest.testmod()
