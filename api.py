from flask import Flask

app = Flask(__name__)

import model

API_ROOT = "/api/v1"
NOTE_API_ROOT = API_ROOT + "/note"

@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    pass

@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    pass

@app.route(NOTE_API_ROOT + "<_id>", methods=["GET"])
def reade():
    pass

@app.route(NOTE_API_ROOT + "<_id>", methods=["PUT"])
def update():
    pass

@app.route(NOTE_API_ROOT + "<_id>", methods=["DELET"])
def delete():
    pass

if __name__ == '__main__':
    app.run(debug=True)