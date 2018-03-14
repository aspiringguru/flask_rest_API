import sqlite3
from db import db

#methods here are not called directly by api, called internally by resource

class ItemModel(db.Model):
    #http://flask-sqlalchemy.pocoo.org/2.3/models/
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    #NB: id column added in L84 @ 7:20
    name = db.Column(db.String(80))#assigns max number of characters
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        #not using SQLAlchemy here yet. direct calls on sqlite3
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            #return {'item': {'name': row[0], 'price': row[1]}} old return json object
            #return cls(row[0], row[1])#returning object of type ItemModel
            return cls(*row)

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()
