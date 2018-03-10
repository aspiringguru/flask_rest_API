import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

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
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'}, 404


    #@jwt_required() #future implementation of login to post
    def post(self, name):
        #return {'message':"recourses.item.py, post(post(self, '{}' ) callled.".format(name)}
        if ItemModel.find_by_name(name):
            return {'message':"An item with name '{}' already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        #return {'message':"recourses.item.py, post(post(self, '{}' ) callled. data['price']='{}'".format(name, data['price'])}
        try:
            item.insert(item)
        except:
            return {"message": "An error occurred inserting the item."}, 500 #internal server errror
        return item.json(), 201


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
        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])
        if item is None:
            #item does not exist, create new item
            try:
                #ItemModel.insert(updated_item)
                updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item."}, 500
        else:
            #item does exist, do an update.
            try:
                #ItemModel.update(updated_item)
                updated_item.update()
            except:
                return {"message": "An error occurred updating the item."}, 500
            #nb: data might contain a new name, bad, need to protect against this later
        return updated_item.json()


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
