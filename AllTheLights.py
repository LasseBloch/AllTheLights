from flask import Flask, jsonify, request

app = Flask(__name__)

lights = []

@app.route('/lights/list', methods=['GET'])
def get_lights():
    return jsonify({'lights': lights})

@app.route('/lights/add', methods=['POST'])
def add_light():
    if not request.json or not 'name' in request.json:
        return '', 404

    if len(lights):
        id = lights[-1]['id'] + 1
    else:
        id = 0

    new_light = {
        'id': id,
        'name': request.json['name'],
        'value': 0
    }
    lights.append(new_light)
    request.json
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)