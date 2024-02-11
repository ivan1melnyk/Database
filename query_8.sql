SELECT Teachers.teacher_id, Teachers.name, AVG(Grades.grade) AS average_grade 
        FROM Teachers JOIN Subjects ON Teachers.teacher_id = Subjects.teacher_id JOIN Grades ON Subjects.subject_id = Grades.subject_id 
        WHERE Teachers.name = 'Steven Armstrong' 
        GROUP BY Teachers.teacher_id, Teachers.name;