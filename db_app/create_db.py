import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

# Cursor
cursor = conn.cursor()

# Create Database
cursor.execute('CREATE DATABASE coding2023')