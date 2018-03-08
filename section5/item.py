import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be left blank!"
    )

    @jwt_required() #when this route is in front of a method definition, the method requires authorisation to execute
    def get(self, name):
        #todo: surround next line in try except block
        item = self.find_by_name(name)
        if item:
            return item
        return {'message':'item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        results = cursor.execute(query, (name,))
        row = results.fetchone()
        #NB: fetchone returns one row only
        connection.close()
        if row:
            return {'item':{'name':row[0], 'price':row[1]}} #, 200


    #@jwt_required() #future implementation of login to post
    def post(self, name):
        if Item.find_by_name(name):
            return {'message':"An item with name '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
            self.insert(item)
        except:
            return {"message", "An error occurred inserting the item."}, 500 #internal server errror
        return item, 201

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        results = cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()


    #@jwt_required() #future implementation of login to delete
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name = ?"
        results = cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'item deleted'}

    @jwt_required() #future implementation of login to put
    def put(self, name):
        #todo: replicate this in other methods.
        data = Item.parser.parse_args()
        #print (data['another']) #results in keyerror when tested in postman

        #data = request.get_json()
        #item = next(filter(lambda x: x['name'] == name, items), None)
        item = self.find_by_name(name)
        updated_item = {'name':name, 'price': data['price']}
        if item is None:
            #item does not exist, create new item
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            #item does exist, do an update.
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occurred updating the item."}, 500
            #nb: data might contain a new name, bad, need to protect against this later
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price = ? WHERE name=?"
        results = cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()



class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        results = cursor.execute(query)
        items = []
        for result in results:
            items.append({'name': result[0], 'price':result[1]})
        connection.close()
        return {"items": items}
