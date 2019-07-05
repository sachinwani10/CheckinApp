import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS time_sheet (id INTEGER PRIMARY KEY, date text, day text, username text, timee text)"
cursor.execute(create_table)


connection.commit()
connection.close()
