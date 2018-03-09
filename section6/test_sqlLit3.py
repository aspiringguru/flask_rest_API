import sqlite3

#https://docs.python.org/3/library/sqlite3.html


#NB: manually delete data.db before running this
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
user2 = (1, 'fred', 'fffff123')
user3 = (1, 'jane', 'jjjjjfffff')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)
cursor.execute(insert_query, user2)
cursor.execute(insert_query, user3)

users = [
    (4,"peter","paaaa"),
    (5,"john","jkkkkkkkkkkk"),
    (6,"mary","mzzzzzzzzz")
]
cursor.executemany(insert_query, users)
#nb: cursor.execute inserts tuple elements into the SQL string.


select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print (row)

connection.commit()
connection.close()
