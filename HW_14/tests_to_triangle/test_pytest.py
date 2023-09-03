import pytest


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Равносторонний.'
        elif a == b or a == c or b == c:
            return 'Равнобедренный.'
        else:
            return 'Разносторонний.'
    else:
        return 'Такой треугольник не существует.'


def test_equilateral_triangle():
    assert is_triangle(3, 3, 3) == 'Равносторонний.'


def test_isosceles_triangle():
    assert is_triangle(2, 2, 3) == 'Равнобедренный.'


def test_scalene_triangle():
    assert is_triangle(3, 4, 5) == 'Разносторонний.'


def test_nonexistent_triangle():
    assert is_triangle(1, 2, 3) == 'Такой треугольник не существует.'


if __name__ == '__main__':
    pytest.main()
