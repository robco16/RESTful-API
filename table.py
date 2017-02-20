import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# Creates the table that will store the users' id, name, password.
table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(table)

# Creates the table that will store the name of the tasks and their respective descriptions.
table = "CREATE TABLE IF NOT EXISTS tasks (name text PRIMARY KEY, description text)"
cursor.execute(table)

connection.commit()

connection.close()
