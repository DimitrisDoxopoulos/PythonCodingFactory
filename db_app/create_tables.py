import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'coding2023'
)

# Cursor
cursor = conn.cursor()

# Create table
cursor.execute('''
               CREATE TABLE students
               (ID integer PRIMARY KEY,
               firstname VARCHAR(50),
               lastname VARCHAR(50))
               ''')

cursor.execute('''
               CREATE TABLE teachers
               (ID integer PRIMARY KEY,
               firstname VARCHAR(50),
               lastname VARCHAR(50))
               ''')

conn.commit()
conn.close()
