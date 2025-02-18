#!/usr/bin/python3
"""Simple RESTful API using Flask"""
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    """Home endpoint"""
    return "Welome to the Flask API!"


@app.route('/data')
def data():
    """Data endpoint"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Status endpoint"""
    return "OK"


@app.route('/users/<username>')
def user(username):
    """User endpoint"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add user endpoint"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400

    if not all(key in data for key in ["username", "name", "age", "city"]):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_data = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
