"""Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра."""

from datetime import date

from HW_4.task_3 import percent_tax, check_bank, take_bank, list_operation, add_bank, exit_bank


class Bank:
    def __init__(self):
        self.summ = 0
        self.count = 0
        self.percent_take = 0.015
        self.percent_add = 0.03
        self.percent_tax = 0.01
        self.list_operation = []

    def add_bank(self, get_cash: float) -> None:
        self.summ += get_cash
        self.count += 1
        if self.count % 3 == 0:
            self.summ = self.summ + self.percent_add * self.summ
            print("Начислены проценты в размере: ", self.percent_add * self.summ)

    def take_bank(self, get_cash: float) -> None:
        self.summ -= get_cash
        self.count += 1

        if get_cash * self.percent_take < 30:
            self.summ -= 30
            print("Списаны проценты за cash: ", 30)
        elif get_cash * self.percent_take > 600:
            self.summ -= 600
            print("Списаны проценты за cash: ", 600)
        else:
            self.summ -= get_cash * self.percent_take
            print("Списаны проценты за cash: ", get_cash * self.percent_take)
        if self.count % 3 == 0:
            self.summ = self.summ + self.percent_add * self.summ
            print("Начислены проценты в размере: ", self.percent_add * self.summ)

    def exit_bank(self):
        print("Храните деньги в сберегательной кассе!\n")
        exit()

    def check_bank(self) -> int:
        while True:
            get_cash = int(input("Введите сумму операции, кратную 50\n"))
            if get_cash % 50 == 0:
                return get_cash

    def run(self):
        while True:
            action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

            if action == '1':
                if self.summ > 5_000_000:
                    tax = self.summ * percent_tax
                    self.summ -= tax
                    print("Списан налог на роскошь: ", tax)
                cash = check_bank()
                if cash < self.summ:
                    take_bank(cash)

                    list_operation.append([str(date.today()), -1 * cash])
                else:
                    print("Недостаточно средств!\n")
                if self.summ > 5_000_000:
                    tax = self.summ * percent_tax
                    self.summ -= tax
                    print("Списан налог на роскошь: ", tax)
                print("Баланс = ", self.summ)
            elif action == '2':
                cash = check_bank()
                add_bank(cash)
                if self.summ > 5_000_000:
                    tax = self.summ * percent_tax
                    self.summ -= tax
                    print("Списан налог на роскошь: ", tax)
                print("Баланс = ", self.summ)

                list_operation.append([str(date.today()), cash])

            elif action == '3':
                print("Баланс = ", self.summ)
            elif action == '4':
                print(list_operation)
            else:
                exit_bank()


bank = Bank()
bank.run()
