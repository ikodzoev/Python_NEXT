import pytest


def fibonacci(n):
    if n < 0:
        return []
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def test_fibonacci_5():
    result = fibonacci(5)
    assert result == [0, 1, 1, 2, 3]


def test_fibonacci_10():
    result = fibonacci(10)
    assert result == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_1():
    result = fibonacci(1)
    assert result == [0]


def test_fibonacci_0():
    result = fibonacci(0)
    assert result == []


def test_fibonacci_negative():
    result = fibonacci(-1)
    assert result == []
