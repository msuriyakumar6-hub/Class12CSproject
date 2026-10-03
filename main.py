#getting started with the file
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ammaappa@24",
    database="timetable"
)
cursor = connection.cursor()
teacher_level =  """
SELECT subject_periods.class_level, classes.section,subject_periods.subject,subject_periods.stream, teacher_classes.teacher_id, teachers.name
FROM subject_periods, teacher_classes, teachers,classes
WHERE subject_periods.subject = teacher_classes.subject
AND subject_periods.class_level between teacher_classes.class_from and teacher_classes.class_to
AND teacher_classes.teacher_id = teachers.teacher_id
AND classes.class_level = subject_periods.class_level
ORDER BY subject,class_level,section;"""
cursor.execute(teacher_level)
print(cursor.fetchall())



connection.close()
