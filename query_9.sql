SELECT Subjects.subject_id, Subjects.subject_name 
        FROM Subjects JOIN Grades ON Subjects.subject_id = Grades.subject_id 
        JOIN Students ON Grades.student_id = Students.student_id
        WHERE Students.student_id = 5;