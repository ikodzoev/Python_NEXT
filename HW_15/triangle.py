""""Задача № 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним."""""
import argparse
import logging

# a = int(input("Введите длину стороны треугольника а: "))
#
# b = int(input("Введите длину стороны треугольника b: "))
#
# c = int(input("Введите длину стороны треугольника c: "))
# if a + b > c and a + c > b and b + c > a:
#     print("Такой треугольник существует: ")
#     if a == b == c:
#         print("Равносторонний.")
#     if a == b or a == c or b == c:
#         print("Равнобедренный.")
#     else:
#         print("Разносторонний.")
# else:
#     print("Такой треугольник не существует.")

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Создаем файловый обработчик с кодировкой UTF-8
file_handler = logging.FileHandler('HW_15//triangle_app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)

# Добавляем файловый обработчик к логгеру
logger.addHandler(file_handler)


def check_triangle(a, b, c):
    """
    Проверяет, существует ли треугольник с заданными сторонами и определяет его тип.

    :param a: Длина стороны a.
    :param b: Длина стороны b.
    :param c: Длина стороны c.
    """
    if a + b <= c or a + c <= b or b + c <= a:
        logger.error("Треугольник не существует.")
    elif a <= 0 or b <= 0 or c <= 0:
        logger.error("Стороны треугольника должны быть больше нуля.")
        # exit()
    else:
        logger.info("Треугольник существует.")
        if a == b == c:
            print("Равносторонний.")
        elif a == b or a == c or b == c:
            print("Равнобедренный.")
        else:
            print("Разносторонний.")


def main():
    parser = argparse.ArgumentParser(description="Проверка типа треугольника")
    parser.add_argument("a", type=int, help="Длина стороны a")
    parser.add_argument("b", type=int, help="Длина стороны b")
    parser.add_argument("c", type=int, help="Длина стороны c")
    args = parser.parse_args()

    check_triangle(args.a, args.b, args.c)


if __name__ == "__main__":
    main()
