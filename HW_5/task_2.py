"""✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии"""


def calc_bonus(ns, rs, bs):
    return {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(ns, rs, bs)}


names = ['Иван', 'Анна', 'Петр']
rates = [1000, 2000, 1500]
bonuses = ['10%', '15%', '12.5%']

print(f'Исходные данные:\n{names}\n{rates}\n{bonuses}')
print(f'Решение: {calc_bonus(names, rates, bonuses)}')
print({name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)})
