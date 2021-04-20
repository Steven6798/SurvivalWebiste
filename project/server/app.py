import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from controller.equipment import Equipment
from controller.firearm import Firearm
from controller.pistol import Pistol

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


# This route adds a new pistol
@app.route('/ArmoryApp/insert/pistol', methods=['POST'])
def handle_add_new_pistol():
    if request.method == 'POST':
        output = json.loads((Equipment().add_new_equipment(request.json)[0]).get_data())
        output = json.loads((Firearm().add_new_firearm(request.json, output['equipment_id'])[0]).get_data())
        return Pistol().add_new_pistol(request.json, output['firearm_id'])
    else:
        return jsonify("Method Not Allowed"), 405


# This route gets all the pistols
@app.route('/ArmoryApp/get/pistols', methods=['GET'])
def handle_get_pistols():
    if request.method == 'GET':
        return Pistol().get_pistols()
    else:
        return jsonify("Method Not Allowed"), 405


# This route gets a pistols by id
@app.route('/ArmoryApp/get/pistol/<int:pistol_id>', methods=['GET'])
def handle_get_pistol_by_id(pistol_id):
    if request.method == 'GET':
        return Pistol().get_pistol_by_id(pistol_id)
    else:
        return jsonify("Method Not Allowed"), 405


# This route delete a pistol
@app.route('/ArmoryApp/remove/pistol/<int:pistol_id>', methods=['DELETE'])
def handle_delete_like(pistol_id):
    if request.method == 'DELETE':
        output = json.loads((Pistol().delete_pistol(pistol_id)[0]).get_data())
        output = json.loads((Firearm().delete_firearm(request.json, output['firearm_id'])[0]).get_data())
        return Equipment().delete_equipment(request.json, output['equipment_id'])
    else:
        return jsonify("Method Not Allowed"), 405


if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=True)
