import sqlite3
from db import db
import traceback

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        #NB: name and price initialzed by the code above. id value exists but not passed to self.id here. L84 @ 10:20
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        #keeping this as a class method because it returns an object.
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        results = cursor.execute(query, (name,))
        row = results.fetchone()
        #NB: fetchone returns one row only
        connection.close()
        if row:
            #return {'item':{'name':row[0], 'price':row[1]}} #, 200
            #now returns ItemModel object instead of json
            #return cls(row[0], row[1])
            return cls(*row) #*row is argument unpacking shorthand

    def insert(self):
        #nb: was previously classmethod, converted to object method as not returning anything
        try:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "INSERT INTO items VALUES (?, ?)"
            results = cursor.execute(query, (self.name, self.price))
            connection.commit()
            connection.close()
        except:
            traceback.print_exc()

    def update(self):
        #nb: was previously classmethod, converted to object method as not returning anything
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price = ? WHERE name=?"
        results = cursor.execute(query, (self.price, self.name))
        connection.commit()
        connection.close()
