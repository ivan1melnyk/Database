SELECT Students.student_id, Students.name, AVG(Grades.grade) AS average_grade 
        FROM Students JOIN Grades ON Students.student_id = Grades.student_id 
        GROUP BY Students.student_id, Students.name 
        ORDER BY average_grade DESC 
        LIMIT 5;