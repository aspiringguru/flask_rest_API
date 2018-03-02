from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return {"name": name, "price": item['price']}
        return {"error": "item " + name + " not found."}, 404
        # ,404 after the json is interpreted by browser as http response code

    def post(self, name):
        data = request.get_json()
        #NB: this requires the content-type to be set to application/json and body to be json in the post request, o/wise error.
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

api.add_resource(Item, "/item/<string:name>")


class ItemList(Resource):
    def get(self):
        return {"items": items}
api.add_resource(ItemList, "/items")


class Store(Resource):
    def get(self, name):
        return {"store": name}

api.add_resource(Store, "/store/<string:name>")


class Home(Resource):
    def get(self):
        return{"message": "Connected"}

api.add_resource(Home, "/")
#test

app.run(debug=True, port=5000, host='0.0.0.0')

