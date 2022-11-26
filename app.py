
from flask import Flask
app = Flask(__name__)
from flask import request, jsonify, Blueprint
import random

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route("/get_cordinates", methods=["POST"])
def get_cordinates(lat: float, long:float):
    lat=24.876077
    long=67.083399
    res = list()
    for _ in range(12):
        coordinate = dict()
        x = random.randint(-100000, 100000)
        y = random.randint(-100000, 100000)
        coordinate['lat'] = lat + (x/1000000)
        coordinate['long'] = long + (x/1000000)
        res.append(coordinate)
        return jsonify(res), 200

    print(res)
    # json_payload = request.get_json()
    # user_entry = User.get(json_payload['username'])
    # if (user_entry):
    #     user = User(*user_entry)
    #     if (user.password == json_payload['password']):  # not for prod
    #         login_user(user)
    #   return jsonify(isLoggedIn=current_user.is_authenticated), 200

    return jsonify(authorization=False), 403
