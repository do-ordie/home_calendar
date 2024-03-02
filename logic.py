from typing import List

import model
import db
import tim


HEADER_LIMIT = 30
TEXT_LIMIT = 200
LIST_DATE = []


class LogicException(Exception):
    pass


class NoteLogic:
    def __init__(self):
        self._note_db = db.NoteDB()

    @staticmethod
    def _validate_note(event: model.Event):
        if event is None:
            raise LogicException("event is None")
        if event.header is None or len(event.header) > HEADER_LIMIT:
            raise LogicException(f"header lenght > MAX: {HEADER_LIMIT}")
        if event.text is None or len(event.text) > TEXT_LIMIT:
            raise LogicException(f"text lenght > MAX: {TEXT_LIMIT}")
        if event.date is None:
            raise LogicException("event is None")
    
        

    def create(self, event: model.Event) -> str:
        self._validate_note(event)
        try:
            if event.date not in LIST_DATE:
                LIST_DATE.append(event.date)
                return self._note_db.create(event)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[model.Event]:
        try:
            return self._note_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Event:
        try:
            return self._note_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, event: model.Event):
        self._validate_note(event)
        try:
            return self._note_db.update(_id,event)
        except Exception as ex:
            raise LogicException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._note_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")