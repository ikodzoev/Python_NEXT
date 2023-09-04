import argparse
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Создаем файловый обработчик с кодировкой UTF-8
file_handler = logging.FileHandler('HW_15//matrix_app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)

# Добавляем файловый обработчик к логгеру
logger.addHandler(file_handler)


class Matrix:
    """
    Класс для работы с матрицами.
    """

    def __init__(self, matrix):
        """
        Инициализация матрицы.

        :param matrix: Список списков, представляющий матрицу.
        """
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


def main():
    parser = argparse.ArgumentParser(description="Работа с матрицами")
    parser.add_argument("--matrix_a", type=str, help="Матрица A в формате '1,2;3,4'")
    parser.add_argument("--matrix_b", type=str, help="Матрица B в формате '5,6;7,8'")
    args = parser.parse_args()

    try:
        matrix_a = [list(map(int, row.split(','))) for row in args.matrix_a.split(';')]
        matrix_b = [list(map(int, row.split(','))) for row in args.matrix_b.split(';')]

        A = Matrix(matrix_a)
        B = Matrix(matrix_b)

        # Вывод матриц на печать
        logger.info("Матрица A:")
        logger.info(A)
        logger.info("Матрица B:")
        logger.info(B)

        # Сравнение матриц
        logger.info("A == B: %s", A == B)
        logger.info("A == A: %s", A == A)

        # Сложение матриц
        C = A + B
        logger.info("C = A + B:")
        logger.info(C)

        # Умножение матриц
        D = A * B
        logger.info("D = A * B:")
        logger.info(D)

    except Exception as e:
        logger.error("Произошла ошибка: %s", str(e))


if __name__ == "__main__":
    main()
