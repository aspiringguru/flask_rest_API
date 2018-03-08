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
        #now impose unique name on adding/creating new item.
        #if self.find_by_name(name): #can still call by self, or by class as below
        if Item.find_by_name(name):
            #checks if an item already exists.
            return {'message':"An item with name '{}' already exists".format(name)}, 400
        #by using an error first approach, the code below is not executed if error condition found.

        data = Item.parser.parse_args()
        #data = request.get_json() #ssd
        #NB: this requires the content-type to be set to application/json and body to be json in the post request, o/wise error.
        item = {'name': name, 'price': data['price']}
        #items.append(item)  #obselete since storing in database not ItemList
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        results = cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()
        #NB: all return have to be json.
        return item, 201

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
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
            #nb: data might contain a new name, bad, need to protect against this later
        return item



class ItemList(Resource):
    def get(self):
        return {"items": items}
