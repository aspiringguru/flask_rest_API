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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        results = cursor.execute(query, (name,))
        row = results.fetchone()
        #NB: fetchone returns one row only
        connection.close()
        if row:
            return {'item':{'name':row[0], 'price':row[1]}} #, 200
        return {'message':'item not found'}, 404

    #@jwt_required() #future implementation of login to post
    def post(self, name):
        #now impose unique name on adding/creating new item.
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message':"An item with name '{}' already exists".format(name)}, 400
        #by using an error first approach, the code below is not executed if error condition found.

        data = Item.parser.parse_args()
        #data = request.get_json() #ssd
        #NB: this requires the content-type to be set to application/json and body to be json in the post request, o/wise error.
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    @jwt_required() #future implementation of login to delete
    def delete(self, name):
        #todo: upgrade to return err msg if item does not exist to delete. curr version does not check
        global items
        #tells this method the items generated is the global var items
        items = list(filter(lambda x: x['name'] != name, items))
        #overwrite list items with list where name has been removed.
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
