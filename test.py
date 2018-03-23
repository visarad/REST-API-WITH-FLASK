import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = 'CREATE TABLE users (id integer, username text,password text)'

cursor.execute(create_table)
user = (1,'visarad','pararthi')

insert_query = 'INSERT INTO users VALUES(?,?,?)'
cursor.execute(insert_query,user)

users = [(2,'kumar','pararthi'),
         (3,'pararthi','visarad'),
         (4,'siva','sai')]

cursor.executemany(insert_query,users)

select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()

