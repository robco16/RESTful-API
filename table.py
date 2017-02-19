import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(table)

table = "CREATE TABLE IF NOT EXISTS tasks (name text PRIMARY KEY, description text)" #might need to change that real to text maybe.
cursor.execute(table)

connection.commit()

connection.close()
