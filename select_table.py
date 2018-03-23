import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


select_table = "SELECT * FROM users"
rows = cursor.execute(select_table)

for row in rows:
    print(row)

connection.commit()
connection.close()