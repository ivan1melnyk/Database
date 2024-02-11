SELECT Groups.group_id, Groups.group_name, AVG(Grades.grade) AS average_grade 
        FROM Groups JOIN Students ON Groups.group_id = Students.group_id 
        JOIN Grades ON Students.student_id = Grades.student_id 
        WHERE Grades.subject_id = 1 
        GROUP BY Groups.group_id, Groups.group_name;