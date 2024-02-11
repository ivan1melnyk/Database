SELECT Subjects.subject_id, Subjects.subject_name 
        FROM Subjects JOIN Teachers ON Subjects.teacher_id = Teachers.teacher_id 
        WHERE Teachers.name = 'Justin Waters';