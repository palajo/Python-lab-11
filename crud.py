from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from flask_marshmallow import Marshmallow
import json
import copy

with open("secret.json") as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Tank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    engine_volume = db.Column(db.Integer, unique=False)
    fuel_consumption = db.Column(db.Float, unique=False)
    max_speed = db.Column(db.Float, unique=False)
    passengers_capacity = db.Column(db.Integer, unique=False)
    fire_range = db.Column(db.Integer, unique=False)
    overview_in_degrees = db.Column(db.Integer, unique=False)

    def __init__(self, engine_volume: int, fuel_consumption: float, max_speed: float, passengers_capacity: int,
                 fire_range: int, overview_in_degrees: int):
        self.engine_volume = engine_volume
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed
        self.passengers_capacity = passengers_capacity
        self.fire_range = fire_range
        self.overview_in_degrees = overview_in_degrees

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


db.create_all()


class TankSchema(ma.Schema):
    class Meta:
        model = Tank
        sql_session = db.session

    id = fields.Integer(dump_only=True)
    engine_volume = fields.Integer(required=True)
    fuel_consumption = fields.Float(required=True)
    max_speed = fields.Float(required=True)
    passengers_capacity = fields.Integer(required=True)
    fire_range = fields.Integer(required=True)
    overview_in_degrees = fields.Integer(required=True)


tank_schema = TankSchema()
many_tank_schemas = TankSchema(many=True)


@app.route("/tanks", methods=["GET"])
def get_all_tanks():
    tanks = Tank.query.all()
    if not tanks:
        abort(404)
    tanks = many_tank_schemas.dump(tanks)
    return make_response(jsonify({"tanks": tanks}), 200)


@app.route("/tanks/<id>", methods=["GET"])
def get_tank_by_id(id):
    get_tank = Tank.query.get(id)
    if not get_tank:
        abort(404)
    tank = tank_schema.dump(get_tank)
    return make_response(jsonify({"tank": tank}), 200)


@app.route("/tanks", methods=["POST"])
def add_tank():
    engine_volume = request.json['engine_volume']
    fuel_consumption = request.json['fuel_consumption']
    max_speed = request.json['max_speed']
    passengers_capacity = request.json['max_speed']
    fire_range = request.json['fire_range']
    overview_in_degrees = request.json['overview_in_degrees']

    tank = Tank(engine_volume=engine_volume, fuel_consumption=fuel_consumption, max_speed=max_speed,
                passengers_capacity=passengers_capacity, fire_range=fire_range, overview_in_degrees=overview_in_degrees)

    db.session.add(tank)
    db.session.commit()
    return tank_schema.jsonify(tank)

@app.route("/tanks/<id>", methods=["PUT"])
def update_flower_by_id(id):
    data = request.get_json()
    get_tank = Tank.query.get(id)

    old_tank = copy.deepcopy(get_tank)
    if data.get("engine_volume"):
        get_tank.engine_volume = data["engine_volume"]
    if data.get("fuel_consumption"):
        get_tank.fuel_consumption = data["fuel_consumption"]
    if data.get("max_speed"):
        get_tank.max_speed = data["max_speed"]
    if data.get("passengers_capacity"):
        get_tank.passengers_capacity = data["passengers_capacity"]
    if data.get("fire_range"):
        get_tank.fire_range = data["fire_range"]
    if data.get("overview_in_degrees"):
        get_tank.overview_in_degrees = data["overview_in_degrees"]

    db.session.add(get_tank)
    db.session.commit()
    return tank_schema.jsonify(old_tank)


@app.route("/tanks/<id>", methods=["DELETE"])
def delete_weapon_by_id(id):
    get_tank = Tank.query.get(id)
    if not get_tank:
        abort(404)
    db.session.delete(get_tank)
    db.session.commit()
    return make_response("", 200)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="127.0.0.1", port="8080")