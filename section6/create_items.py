import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
item1 = (4, 'chair', 11.11)
item2 = (5, 'table', 22.22)
item3 = (3, 'bench', 33.33)
insert_query = "INSERT INTO items VALUES (?, ?, ?)"
cursor.execute(insert_query, item1)
cursor.execute(insert_query, item2)
cursor.execute(insert_query, item3)
connection.commit()
connection.close()
