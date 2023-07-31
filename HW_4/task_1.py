"""Напишите функцию для транспонирования матрицы"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Исходная матрица:\n", matrix)


def matrix_transpose_1(get_matrix):
    do_matrix = []
    for i in range(len(get_matrix[0])):
        do_matrix.append([0 for j in range(len(get_matrix))])
    for i in range(len(get_matrix)):
        for j in range(len(get_matrix[0])):
            do_matrix[j][i] = get_matrix[i][j]
    print(do_matrix)


def matrix_transpose_2(get_matrix: list) -> list:
    return [list(row) for row in zip(*get_matrix)]


transposed_matrix = matrix_transpose_2(matrix)
print("Транспонированная матрица, вариант 1:")
matrix_transpose_1(matrix)
print("Транспонированная матрица, вариант 2:\n", transposed_matrix)
