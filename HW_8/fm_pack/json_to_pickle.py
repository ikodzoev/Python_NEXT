"""
Задание №5
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import json
import os
import pickle
for el in os.listdir():
    if el.endswith(".json"):
        with open(el, "r", encoding="utf-8") as j:
            res = json.load(j)
        path = ''.join(el.split(".")[:-1]) + ".pickle"
        with open(path, "wb") as p:
            pickle.dump(res,p)