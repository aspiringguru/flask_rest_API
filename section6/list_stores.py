import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

select_query = "SELECT * FROM stores"
for row in cursor.execute(select_query):
    print (row)


connection.commit()

connection.close()
