import time

from flask import Flask, jsonify, request

app = Flask(__name__)

lights = []


def name_already_excists(name):
    for light in lights:
        if light['name'] == name:
            return True
    return False

@app.route('/lights/list', methods=['GET'])
def get_lights():
    return jsonify({'lights': lights})

@app.route('/lights/add', methods=['POST'])
# Add also works as keep alive if we already have the light in the dictionary
def add_light():
    if not request.json or not 'name' in request.json:
        return '', 404
    #    if lights
    if len(lights):
        if not name_already_excists(request.json['name']):
            id = lights[-1]['id'] + 1
        else:
            print "{} already in list of lights".format(request.json['name'])
            # 409 Conflict if the name is already taken
            return '', 409
    else:
        id = 0

    new_light = {
        'id': id,
        'name': request.json['name'],
        'value': 0,
        'last_hart_beat': time.time()
    }
    lights.append(new_light)
    request.json
    return '', 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)