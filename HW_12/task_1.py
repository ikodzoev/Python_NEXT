"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых."""

import csv
import os


class FullNameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not all(x.istitle() for x in value.split()):
            raise ValueError("ФИО должно начинаться с заглавной буквы")
        if not all(x.isalpha() or x.isspace() for x in value):
            raise ValueError("ФИО должно содержать только буквы")
        instance.__dict__[self.name] = value


class Student:
    full_name = FullNameDescriptor()

    def __init__(self, full_name, subjects_file):
        self.full_name = full_name
        self.subjects = []
        self.grades = {}
        self.test_scores = {}
        with open(subjects_file, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                self.subjects.append(subject)
                self.grades[subject] = []
                self.test_scores[subject] = []

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не допустим")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.grades[subject].append(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не допустим")
        if not 0 <= score <= 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.test_scores[subject].append(score)

    def average_test_score(self, subject):
        scores = self.test_scores[subject]
        return sum(scores) / len(scores)

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades)

    def save_to_csv(self, filename):
        file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['ФИО', 'Предмет', 'Оценки', 'Результаты тестов'])
            for subject in self.subjects:
                grades = ', '.join(map(str, self.grades[subject]))
                test_scores = ', '.join(map(str, self.test_scores[subject]))
                writer.writerow([self.full_name, subject, grades, test_scores])

    def __str__(self):
        res = [f'Студент: {self.full_name}']
        for subject in self.subjects:
            res.append(f'Предмет: {subject}')
            grades = ', '.join(map(str, self.grades[subject]))
            res.append(f'Оценки: {grades}')
            test_scores = ', '.join(map(str, self.test_scores[subject]))
            res.append(f'Результаты тестов: {test_scores}')
        return '\n'.join(res)


if __name__ == '__main__':
    # Создаем экземпляры класса Студент для двух студентов
    ivan = Student('Иван Иванов', 'subjects.csv')
    anna = Student('Мария Петрова', 'subjects.csv')

    # Добавляем оценки и результаты тестов для Ивана
    ivan.add_grade('Математика', 5)
    ivan.add_grade('Математика', 4)
    ivan.add_test_score('Математика', 85)
    ivan.add_test_score('Математика', 90)

    # Добавляем оценки и результаты тестов для Анны
    anna.add_grade('Математика', 4)
    anna.add_grade('Математика', 3)
    anna.add_test_score('Математика', 75)
    anna.add_test_score('Математика', 80)

    # Сохраняем данные обоих студентов в один файл CSV
    ivan.save_to_csv('students_data.csv')
    anna.save_to_csv('students_data.csv')
    # Выводим на печать
    print(anna)
    print(ivan)
