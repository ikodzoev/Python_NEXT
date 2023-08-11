"""Напишите декоратор, сохраняющий переданные параметры и результаты работы функции в json файл"""
import json


def log_to_json(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            get_result = func(*args, **kwargs)
            data = {
                'function': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': get_result
            }
            with open(file_path, 'a') as f:
                json.dump(data, f)
                f.write('\n')
            return get_result

        return wrapper

    return decorator


# Пример:
@log_to_json('log.json')
def add(a, b):
    return a + b


result = add(1, 2)
print(f"Результат: {result}")
