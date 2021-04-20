from flask import Flask, request, jsonify
from flask_cors import CORS

from controller.product import Product

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


# This route adds a new product
@app.route('/SurvivalApp/insert/product', methods=['POST'])
def handle_add_new_product():
    if request.method == 'POST':
        return Product().add_new_product(request.json)
    else:
        return jsonify("Method Not Allowed"), 405


# This route gets all the products
@app.route('/SurvivalApp/get/product', methods=['GET'])
def handle_get_product():
    if request.method == 'GET':
        return Product().get_product()
    else:
        return jsonify("Method Not Allowed"), 405


# This route gets a product by id
@app.route('/SurvivalApp/get/product/<int:product_id>', methods=['GET'])
def handle_get_product_by_id(product_id):
    if request.method == 'GET':
        return Product().get_product_by_id(product_id)
    else:
        return jsonify("Method Not Allowed"), 405


# This route delete a product
@app.route('/SurvivalApp/remove/product/<int:product_id>', methods=['DELETE'])
def handle_delete_product(product_id):
    if request.method == 'DELETE':
        return Product().delete_product(product_id)
    else:
        return jsonify("Method Not Allowed"), 405


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=True)
