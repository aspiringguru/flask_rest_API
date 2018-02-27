from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name':'my item',
                'price': 15.99
            }
        ]
    }
]


@app.route("/")
def home():
    return "Hello World!"


# POST receives data
# GET  send data back

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    pass

# GET  /store<string:name>
#@app.route("/store/<string:name>", methods=["GET"])  #NB: don't need to specify methods=GET since GET is default
@app.route("/store/<string:name>")
def get_store(name):
    pass

# GET  /store
@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})

# POST /store/<string:name>/item  {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store():
    pass


# GET  /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store():
    pass



app.run(port=5000, host = "0.0.0.0")

