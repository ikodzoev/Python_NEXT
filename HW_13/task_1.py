"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
№ 1. Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения,
*умножения матриц"""


class InvalidMatrix(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Ошибка: {self.message}"


class Matrix:
    """
    Класс для работы с матрицами.
    """

    def __init__(self, matrix):
        """
        Инициализация матрицы.

        :param matrix: Список списков, представляющий матрицу.
        """
        if not all(isinstance(row, list) for row in matrix):
            raise InvalidMatrix("Матрица должна быть списком списков!")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise InvalidMatrix("Все строки матрицы должны иметь одинаковую длину!")
        self.matrix = matrix

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        :return: Строковое представление матрицы.
        """
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        """
        Сравнение двух матриц на равенство.

        :param other: Другая матрица для сравнения.
        :return: True, если матрицы равны, иначе False.
        """
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __add__(self, other):
        """
        Сложение двух матриц.

        :param other: Другая матрица для сложения.
        :return: Новая матрица, являющаяся суммой двух матриц.
        :raises TypeError: Если other не является экземпляром класса Matrix.
        :raises ValueError: Если размерности матриц не совпадают.
        """
        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
                result = [[0 for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        result[i][j] = self.matrix[i][j] + other.matrix[i][j]
                return Matrix(result)
            else:
                raise ValueError("Матрицы должны иметь одинаковые размеры!")
        else:
            raise TypeError("Можно складывать только две матрицы!")

    def __mul__(self, other):
        """
        Умножение двух матриц.

        :param other: Другая матрица для умножения.
        :return: Новая матрица, являющаяся произведением двух матриц.
        :raises TypeError: Если other не является экземпляром класса Matrix.
        :raises ValueError: Если число столбцов первой матрицы не равно числу строк второй матрицы.
        """
        if isinstance(other, Matrix):
            if len(self.matrix[0]) == len(other.matrix):
                result = [[0 for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
                for i in range(len(self.matrix)):
                    for j in range(len(other.matrix[0])):
                        for k in range(len(other.matrix)):
                            result[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return Matrix(result)
            else:
                raise ValueError(
                    "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!")
        else:
            raise TypeError("Можно умножать только две матрицы!")


try:
    m = Matrix([[1, 2], [3]])
except InvalidMatrix as e:
    print(e)
