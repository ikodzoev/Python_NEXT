"""✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало."""


def name_num(names_file: str, numbers_file: str, result_file: str):
    with open(names_file, 'r') as nf, open(numbers_file, 'r') as numf, open(result_file, 'w') as rf:
        names = nf.readlines()
        numbers = numf.readlines()

        # Находим длину более длинного файла
        max_len = max(len(names), len(numbers))

        for i in range(max_len):
            # Возвращаемся в начало более короткого файла при достижении его конца
            name = names[i % len(names)].strip()
            num1, num2 = map(float, numbers[i % len(numbers)].split('|'))

            # Перемножаем пару чисел
            result = num1 * num2

            # Сохраняем имя и произведение в результирующий файл
            if result < 0:
                rf.write(f'{name.lower()}|{abs(result):.2f}\n')
            else:
                rf.write(f'{name.upper()}|{round(result)}\n')


name_num('names.txt', 'numbers.txt', 'result.txt')
