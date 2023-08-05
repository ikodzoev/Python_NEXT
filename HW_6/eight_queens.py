"""Задача № 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Задача № 2. Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""

import random


def eight_queens(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(
                    queens[i][1] - queens[j][1]):
                return False
    return True


def random_eight_queens():
    def is_valid(queens):
        for i in range(8):
            for j in range(i + 1, 8):
                if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(
                        queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                    return False
        return True

    cool_positions = []
    while len(cool_positions) < 4:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        if is_valid(queens) and queens not in cool_positions:
            cool_positions.append(queens)
    return cool_positions


if __name__ == '__main__':
    print(random_eight_queens())
