import sqlite3
import traceback

class ItemModel:
    def __init__(self, name, price):
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
        #print("\n\nmodels.item: insert : self.name='{}', self.price='{}'\n\n".format(self.name, self.price), file=sys.stderr)
        #print("\n\nmodels.item: insert : self.name='{}', self.price='{}'\n\n".format(self.name, self.price), file=sys.stdout)
        #return {"message":"item.name='{}', item.price={}".format(item.name, item.price) }
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
