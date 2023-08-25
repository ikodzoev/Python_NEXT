"""Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых."""

import csv
import os


class FullNameDescriptor:
    """
    Дескриптор для проверки и установки полного имени студента.
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        Проверяет, что все слова в полном имени начинаются с заглавной буквы и содержат только буквы.
        """
        if not all(x.istitle() for x in value.split()):
            raise ValueError("ФИО должны начинаться с заглавной буквы")
        if not all(x.isalpha() or x.isspace() for x in value):
            raise ValueError("ФИО должны содержать только буквы")
        instance.__dict__[self.name] = value


class Student:
    """
    Класс для представления студента.
    """
    full_name = FullNameDescriptor()

    def __init__(self, full_name, subjects_file):
        """
        Инициализирует экземпляр класса Student с заданным полным именем и списком предметов из файла.
        """
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
        """
        Добавляет оценку по заданному предмету.
        """
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} недопустим")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.grades[subject].append(grade)

    def add_test_score(self, subject, score):
        """
        Добавляет результат теста по заданному предмету.
        """
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не допустим")
        if not 0 <= score <= 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.test_scores[subject].append(score)

    def average_test_score(self, subject):
        """
        Возвращает средний результат теста по заданному предмету.
        """
        scores = self.test_scores[subject]
        return sum(scores) / len(scores)

    def average_grade(self):
        """
        Возвращает среднюю оценку по всем предметам.
        """
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)
        return sum(all_grades) / len(all_grades)

    def save_to_csv(self, filename):
        """
        Сохраняет информацию о студенте в файл CSV.

         Если файл существует и не пустой, то информация добавляется в конец файла.
         В противном случае создается новый файл с заголовками столбцов.
         """
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
        """
        Возвращает строковое представление информации о студенте.
        """
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
    ivan = Student('Иванов Иван Петрович', 'subjects.csv')
    anna = Student('Петрова Анна Владимировна', 'subjects.csv')

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
