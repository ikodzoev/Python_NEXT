"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""

from datetime import date

summ = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01


def add_bank(get_cash: float) -> None:
    global summ
    global count
    summ += get_cash
    count += 1
    if count % 3 == 0:
        summ = summ + percent_add * summ
        print("Начислены проценты в размере: ", percent_add * summ)


def take_bank(get_cash: float) -> None:
    global summ
    global count
    summ -= get_cash
    count += 1

    if get_cash * percent_take < 30:
        summ -= 30
        print("Списаны проценты за cash: ", 30)
    elif get_cash * percent_take > 600:
        summ -= 600
        print("Списаны проценты за cash: ", 600)
    else:
        summ -= get_cash * percent_take
        print("Списаны проценты за cash: ", get_cash * percent_take)
    if count % 3 == 0:
        summ = summ + percent_add * summ
        print("Начислены проценты в размере: ", percent_add * summ)


def exit_bank():
    print("Храните деньги в сберегательной кассе!\n")
    exit()


def check_bank() -> int:
    while True:
        get_cash = int(input("Введите сумму операции, кратную 50\n"))
        if get_cash % 50 == 0:
            return get_cash


list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        if summ > 5_000_000:
            summ = summ - summ * percent_tax
            print("Списан налог на роскошь: ", summ * percent_tax)
        cash = check_bank()
        if cash < summ:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Недостаточно средств!\n")
        if summ > 5_000_000:
            summ = summ - summ * percent_tax
            print("Списан налог на роскошь: ", summ * percent_tax)
        print("Баланс = ", summ)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if summ > 5_000_000:
            summ = summ - summ * percent_tax
            print("Списан налог на роскошь: ", summ * percent_tax)
        print("Баланс = ", summ)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", summ)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
