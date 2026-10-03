import mysql.connector
import random

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ammaappa@24",
    database="timetable_v2"
)

cursor = connection.cursor()

select = "SELECT * FROM teacher_assignments"
cursor.execute(select)

values = cursor.fetchall()

for i in values:
    select_specific = """
    SELECT * FROM teacher_assignments
    WHERE class_level = {}
    AND section = "{}"
    AND subject = "{}"
    """.format(i[0], i[1], i[2])

    cursor.execute(select_specific)

    teachers = cursor.fetchall()

    chosen_teacher = random.choice(teachers)

    for j in teachers:
        if chosen_teacher == j:
            continue
        else:
            remove = """
            DELETE FROM teacher_assignments
            WHERE class_level = {}
            AND section = "{}"
            AND subject = "{}"
            AND teacher_id = {}
            """.format(j[0], j[1], j[2], j[4])

            cursor.execute(remove)
            connection.commit()

connection.close()