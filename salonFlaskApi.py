from flask import Flask, jsonify, request
from salon import Salon

app = Flask(__name__)

salon = Salon()


@app.route('/')
def get_all_cars():
    return jsonify(cars=[b.serialize for b in salon.get_all_cars()])


@app.route('/<string:name>')
def get_car_by_name(name):
    car = salon.get_car_by_name(name)
    if car is not None:
        return jsonify(car=car.serialize)
    else:
        return jsonify(error="There is no car with name: " + name)


@app.route('/addcar', methods=['POST'])
def add_car():
    name = request.get_json().get("name")
    speed = request.get_json().get("speed")
    return jsonify(car=salon.add_car(name, speed).serialize)


@app.route('/updatecar', methods=['PUT'])
def update_car():
    id = request.get_json().get("id")
    name = request.get_json().get("name")
    speed = request.get_json().get("speed")
    car = salon.update_car(id, name, speed)
    if car is not None:
        return jsonify(car=car.serialize)
    else:
        return jsonify(error="There is no car with id: " + str(id))


@app.route('/deletecar/<int:id>', methods=['DELETE'])
def delete_car(id):
    is_deleted = salon.delete_car_by_id(id)
    if is_deleted:
        return jsonify(message="car with id = " + str(id) + " was successfully deleted")
    else:
        return jsonify(error="There is no car with id: " + str(id))


if __name__ == '__main__':
    app.run()
