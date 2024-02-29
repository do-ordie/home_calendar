from flask import Flask, request 

app = Flask(__name__)

import model
import logic

_note_logic = logic.NoteLogic()

class ApiException(Exception):
    pass

def _from_raw(raw_note: str) -> model.Event:
    parts = raw_note.split('|')
    if len(parts) == 4:
        event = model.Event()
        event.id = parts[0]
        event.date = parts[1]
        event.header = parts[2]
        event.text = parts[3]
        return event
    else:
        raise ApiException(f"invalid RAW note data {raw_note}")
    
    
def _to_raw(event: model.Event) -> str:
    if event.id is None:
        return f"{event.date}|{event.header}|{event.text}"
    else:
        return f"{event.id}|{event.date}|{event.header}|{event.text}"


    

API_ROOT = "/api/v1"
NOTE_API_ROOT = API_ROOT + "/note"

@app.route(NOTE_API_ROOT + "/", methods=["POST"])
def create():
    try:
        body = request.get_data().decode('utf-8')
        event = _from_raw(body)
        _id = _note_logic.create(event)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404
    

@app.route(NOTE_API_ROOT + "/", methods=["GET"])
def list():
    try:
        events = _note_logic.list()
        raw_notes = ""
        for event in events:
            raw_notes += _to_raw(event) + '\n'
        return raw_notes, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404

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