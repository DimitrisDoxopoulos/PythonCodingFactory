import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'coding2023',
    port = '3306'
)

# Cursor
cursor = conn.cursor()

cursor.execute(
    'INSERT INTO teachers (id, firstname, lastname, age) VALUES (%s, %s, %s, %s)',
    (1, 'Panagiotis', 'Moschos', 36)
)

conn.commit()
conn.close()