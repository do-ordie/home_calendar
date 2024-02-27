from flask import Flask

app = Flask(__name__)

import model

class ApiException(Exception):
    pass

API_ROOT = "/api/v1"
NOTE_API_ROOT = API_ROOT + "/note"

@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    return "create", 201

@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    return "list", 201

@app.route(NOTE_API_ROOT + "/<_id>/", methods=["GET"])
def reade(_id: str):
    return "reade", 201

@app.route(NOTE_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    return "update", 201

@app.route(NOTE_API_ROOT + "/<_id>/", methods=["DELET"])
def delete(_id: str):
    return "delete", 201

if __name__ == '__main__':
    app.run(debug=True)