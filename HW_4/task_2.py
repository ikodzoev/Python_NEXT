"""Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хэшируем,
используйте его строковое представление."""


def key_value_dict(**args):
    result = {}
    for key, value in args.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


print(key_value_dict(а=1, б=2, в=3, г=4, д=5))
