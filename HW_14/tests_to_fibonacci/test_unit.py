import unittest


def fibonacci(n):
    if n < 0:
        return []
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


class TestFibonacciGenerator(unittest.TestCase):

    def test_fibonacci_5(self):
        result = fibonacci(5)
        self.assertEqual(result, [0, 1, 1, 2, 3])

    def test_fibonacci_10(self):
        result = fibonacci(10)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_1(self):
        result = fibonacci(1)
        self.assertEqual(result, [0])

    def test_fibonacci_0(self):
        result = fibonacci(0)
        self.assertEqual(result, [])

    def test_fibonacci_negative(self):
        result = fibonacci(-1)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
