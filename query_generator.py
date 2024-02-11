from sqlite3 import Error

from connect import create_connection, database

# comand_list = ['Знайти 5 студентів із найбільшим середнім балом з усіх предметів.',
#                'Знайти студента із найвищим середнім балом з певного предмета.',
#                'Знайти середній бал у групах з певного предмета.',
#                'Знайти середній бал на потоці (по всій таблиці оцінок).',
#                'Знайти які курси читає певний викладач.',
#                'Знайти список студентів у певній групі.',
#                'Знайти оцінки студентів у окремій групі з певного предмета.',
#                'Знайти середній бал, який ставить певний викладач зі своїх предметів.',
#                'Знайти список курсів, які відвідує студент.',
#                'Список курсів, які певному студенту читає певний викладач.'
#                ]

select_list = [
    """SELECT Students.student_id, Students.name, AVG(Grades.grade) AS average_grade 
        FROM Students JOIN Grades ON Students.student_id = Grades.student_id 
        GROUP BY Students.student_id, Students.name 
        ORDER BY average_grade DESC 
        LIMIT 5;""",
    """SELECT Students.student_id, Students.name, AVG(Grades.grade) AS average_grade 
        FROM Students JOIN Grades ON Students.student_id = Grades.student_id 
        WHERE Grades.subject_id = 1 
        GROUP BY Students.student_id, Students.name 
        ORDER BY average_grade DESC 
        LIMIT 1;""",
    """SELECT Groups.group_id, Groups.group_name, AVG(Grades.grade) AS average_grade 
        FROM Groups JOIN Students ON Groups.group_id = Students.group_id 
        JOIN Grades ON Students.student_id = Grades.student_id 
        WHERE Grades.subject_id = 1 
        GROUP BY Groups.group_id, Groups.group_name;""",
    """SELECT AVG(grade) AS average_grade 
        FROM Grades;""",
    """SELECT Subjects.subject_id, Subjects.subject_name 
        FROM Subjects JOIN Teachers ON Subjects.teacher_id = Teachers.teacher_id 
        WHERE Teachers.name = 'Justin Waters';""",
    """SELECT Students.student_id, Students.name 
        FROM Students WHERE Students.group_id = 3;""",
    """SELECT Students.student_id, Students.name, Grades.grade 
        FROM Students JOIN Grades ON Students.student_id = Grades.student_id 
        WHERE Students.group_id = 3 AND Grades.subject_id = 3;""",
    """SELECT Teachers.teacher_id, Teachers.name, AVG(Grades.grade) AS average_grade 
        FROM Teachers JOIN Subjects ON Teachers.teacher_id = Subjects.teacher_id JOIN Grades ON Subjects.subject_id = Grades.subject_id 
        WHERE Teachers.name = 'Steven Armstrong' 
        GROUP BY Teachers.teacher_id, Teachers.name;""",
    """SELECT Subjects.subject_id, Subjects.subject_name 
        FROM Subjects JOIN Grades ON Subjects.subject_id = Grades.subject_id 
        JOIN Students ON Grades.student_id = Students.student_id
        WHERE Students.student_id = 5;""",
    """SELECT Subjects.subject_id, Subjects.subject_name 
        FROM Subjects JOIN Grades ON Subjects.subject_id = Grades.subject_id 
        JOIN Students ON Grades.student_id = Students.student_id 
        JOIN Teachers ON Subjects.teacher_id = Teachers.teacher_id 
        WHERE Students.student_id = 5 AND Teachers.name = 'Justin Waters';"""
]


if __name__ == '__main__':
    for index, comand in enumerate(select_list, 1):
        with open(f'query_{index}.sql', 'w') as file:
            file.write(comand)
