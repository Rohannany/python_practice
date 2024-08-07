from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/")
def home():
    return "Homepage"

stores = [
    {
        'name' : 'Pharmacy',
        'items': [
            {
                'name' : 'Dolo 650',
                'Price' : 30
            }
        ]
    },
    {
        'name' : 'Bakery',
        'items' : [
            {
                'name' : 'Pastry',
                'Price' : 80
            }
        ]
    }
]
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message' : 'Store not found'})

@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message' : 'Store not found'})

@app.route('/store', methods = ['POST'])
def create_store():
    req_data = request.get_json()
    new_store = {
        'name' : req_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item(name):
    for store in stores:
        if store['name'] == name:
            req_data = request.get_json()
            new_item = {
                'name' : req_data['name'],
                'item' : req_data['Price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message' : 'Store not found'})

app.run(port=8000)