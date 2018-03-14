from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel
import sys, traceback

class Item(Resource):
    __tablename__ = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        print('resources.item.Item.post({}) called.'.format(name), file=sys.stderr)
        #if ItemModel.find_by_name(name):
        #    return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            traceback.print_exc(file=sys.stderr)
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        #NB: added functionality to advise user of error deleting non existing item.
        #added HTTP status codes.
        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}, 200
        else:
            return {'message': 'Item not found'}, 400

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
            print('item added to database & price set.', file=sys.stderr)
        else:
            item.price = data['price']
            print('price of existing item updated.', file=sys.stderr)
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()

        return {'items': items}
