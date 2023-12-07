"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    print(user)

    if user is None:
        return jsonify({"msg": "The user doesnt exist"}), 401

    if password != user.password:
        return jsonify({"msg": "Wrong password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)

@api.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    print(body)
    user = User.query.filter_by(email=body["email"]).first()
    print(user)
    if user == None:
        new_user = User(email=body["email"],password=body["password"], is_active=True)
        db.session.add(new_user)
        db.session.commit()
        response_body = {
            "msg": "New user created"
        }
        return jsonify(response_body), 200
    else:
        return jsonify({"msg": "There is already a user created with this email"}), 401

@api.route("/private", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200