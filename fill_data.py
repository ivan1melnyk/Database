from faker import Faker
import sqlite3
from random import randint, choice

fake = Faker()


def generate_fake_data(number_students, number_groups, number_subjects, number_teachers):
    students = []
    groups = []
    subjects = []
    teachers = []

    # Генеруємо групи
    for i in range(1, number_groups+1):
        groups.append((i, f'Group {i}'))

    # Генеруємо студентів
    for i in range(1, number_students+1):
        students.append((i, fake.name(), randint(1, number_groups)))

    # Генеруємо предмети та викладачів
    for i in range(1, number_subjects+1):
        teachers.append((i, fake.name()))
        subjects.append((i, f'Subject {i}', i))

    return students, groups, subjects, teachers


def generate_grades(students, subjects):
    grades = []

    for student in students:
        student_id = student[0]
        for subject in subjects:
            subject_id = subject[0]
            for _ in range(randint(1, 20)):
                grades.append((student_id, subject_id, randint(
                    1, 100), fake.date_between(start_date='-1y', end_date='today')))

    return grades


def insert_data_to_db(students, groups, subjects, teachers, grades):
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

        # Додаємо дані у таблицю груп
        cur.executemany("INSERT INTO Groups VALUES (?, ?)", groups)

        # Додаємо дані у таблицю студентів
        cur.executemany("INSERT INTO Students VALUES (?, ?, ?)", students)

        # Додаємо дані у таблицю викладачів
        cur.executemany("INSERT INTO Teachers VALUES (?, ?)", teachers)

        # Додаємо дані у таблицю предметів
        cur.executemany("INSERT INTO Subjects VALUES (?, ?, ?)", subjects)

        # Додаємо дані у таблицю оцінок
        cur.executemany(
            "INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)", grades)

        con.commit()


if __name__ == "__main__":
    number_students = 50
    number_groups = 3
    number_subjects = 8
    number_teachers = 5

    students, groups, subjects, teachers = generate_fake_data(
        number_students, number_groups, number_subjects, number_teachers)
    grades = generate_grades(students, subjects)
    insert_data_to_db(students, groups, subjects, teachers, grades)
