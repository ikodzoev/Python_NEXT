"""✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

friends = {
    'Олег': ('фонарик', 'тушенка', 'удочка', 'спальник', 'фотоаппарат', 'лопата', 'отвертка', 'топор'),
    'Николай': ('котелок', 'пила', 'удочка', 'нож', 'спальник', 'лопата', 'фонарик', 'фотоаппарат'),
    'Иван': ('фонарик', 'палатка', 'удочка', 'спальник', 'лопата', 'горелка', 'нож', 'тушенка'),
}

all_set = set()
uniq_set = set()
two_set = set()

for friend, items in friends.items():
    all_set.update(items)
    for item in items:
        if sum(item in friend_items for friend_items in friends.values()) == 1:
            uniq_set.add(item)
        elif sum(item in friend_items for friend_items in friends.values()) == 2:
            two_set.add(item)

common_set = set.intersection(*map(set, friends.values()))

print(f'Какие вещи взяли все три друга: {common_set}')
print(f'Уникальные вещи, которые есть только у одного: {uniq_set}')

for item in two_set:
    for friend, items in friends.items():
        if item not in items:
            print(f'Какие вещи имеют все друзья, но не {friend}: {item}')
