#getting started with the file
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Ammaappa@24",
    database="timetable"
)
cursor = connection.cursor()
connection.close()
