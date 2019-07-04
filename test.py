"""
This file is only for testinf sqlite3
does not contain code relavant to this project
this file might be used in future to create schema for seqlite3
"""
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'sachin', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit()
connection.close()
