from HW_6.eight_queens import eight_queens, random_eight_queens

if __name__ == '__main__':
    # определяем успешность расстановки ферзей на доске 8*8
    print(
        eight_queens([(1, 4), (2, 6), (3, 8), (4, 2), (5, 7), (6, 1), (7, 3), (8, 5)]))
    print(
        eight_queens([(1, 6), (2, 3), (3, 1), (4, 8), (5, 5), (6, 2), (7, 4), (8, 7)]))
    print(
        eight_queens([(1, 6), (2, 3), (3, 7), (4, 4), (5, 1), (6, 8), (7, 2), (8, 5)]))
    print(
        eight_queens([(1, 1), (2, 7), (3, 4), (4, 6), (5, 8), (6, 2), (7, 5), (8, 3)]))
    print(random_eight_queens())  # вывод 4 успешных расстановок ферзей на доске 8*8
