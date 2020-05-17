from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from config import config
import pyotp
import json

username = config.get("user")
pwd = config.get("password")
otp_key = config.get("otp_key")
data = config.get("data")

app = Flask(__name__)
CORS(app)
api = Api(app)

class Login(Resource):
    def post(self):
        user = request.json['user']
        password = request.json['password']
        auth = request.json['auth']
        otp = pyotp.TOTP(otp_key)
        if user == username and password == pwd and otp.verify(str(auth)):
            response = {
                "statusCode": 200,
                "body": json.dumps({"auth": True, "mensaje": "Usuario autenticado", "data": data}),
            }
            return response
        response = {
            "statusCode": 401,
            "body": json.dumps({"auth": False, "mensaje": "Las credenciales no son correctas"})
        }
        return response

api.add_resource(Login, '/login')

if __name__ == '__main__':
     app.run(port='5000')