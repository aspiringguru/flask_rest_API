import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
#NB INTEGER PRIMARY KEY make the column auto incrimenting
#when inserting data to create new users, only have to nominate username & password

cursor.execute(create_table)


connection.commit()

connection.close()
