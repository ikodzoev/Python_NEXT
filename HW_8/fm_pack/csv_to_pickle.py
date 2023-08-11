"""
Задание №7
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle
with open("new_c.csv", "r", encoding="utf-8") as c:
    rider = csv.reader(c)
    data = pickle.dumps(list(rider))
    print(pickle.loads(data))