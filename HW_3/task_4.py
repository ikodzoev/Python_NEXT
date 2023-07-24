"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака."""

import random

a = {"вода": 55, "повербанк": 35, "хлеб": 25, "чай": 40, "яйца": 45, "горелка": 20, "фотоаппарат": 30}

max_load = 200
counter = 0
get_list = []
while counter < max_load:
    key, value = random.choice(list(a.items()))
    if key in get_list:
        continue
    if counter + value > max_load:
        break
    counter += value
    get_list += (str(key), str(value))

print(get_list, "=", counter)
