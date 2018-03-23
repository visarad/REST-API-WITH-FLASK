import sqlite3
from db import db


class ItemModel(db.Model):
    
    __tabelname__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
    
        query = "select * from items where name=? "
        result = cursor.execute(query, (name,))
    
        row = result.fetchone()
        connection.close()
    
        if row:
              return cls(*row)
              #return cls(row[0], row[1])


    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
    
        query = 'Insert into items values (?,?)'
        cursor.execute(query, (self.name, self.price))
    
        connection.commit()
        connection.close()

    
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
    
        query = 'UPDATE items SET price=? where name=?'
        cursor.execute(query, (self.price, self.name))
    
        connection.commit()
        connection.close()
    
        return {"Message": "Item updated "}