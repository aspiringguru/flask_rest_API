import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
import traceback
import sys

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
        #return {'message':"recourses.item.py, post(post(self, '{}' ) callled. data['price']='{}'".format(name, data['price']),
        #        "message2":"type(item)'{}'".format(type(item)),
        #        "message3":"item.name='{}', item.price={}".format(item.name, item.price)
        #}
        #above shows we are getting type models.item.ItemModel with values for item.name and item.price
        try:
            item.save_to_db()
        except:
            traceback.print_exc()
            return {"message": "An error occurred inserting the item.",
                    "message2": "item.json()={}".format(item.json()),
                    "message3": "type(item)={}".format(type(item)),
                    "message4": "item.name={}, item.price={}.format(item.name, item.price)"}, 500 #internal server errror
        return item.json(), 201


    #@jwt_required() #future implementation of login to delete
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        #error fixed in L85 @ 14:31
        if item:
            item.delete_from_db()
        return {"message": "item deleted."}

    @jwt_required() #future implementation of login to put
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
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
