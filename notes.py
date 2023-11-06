import datetime
from typing import List
import model


class Note:
    note_id = 0
    title = ""
    text = ""
    note_dt = datetime.datetime.now()

    def __init__(self, title_, text_):
        self.note_id = model.generate_id()
        self.title = title_
        self.text = text_
        self.note_dt = datetime.datetime.now()

    def edit(self, title_="", text_=""):
        if not (title_ == "" and text_ == ""):
            if not title_ == "":
                self.title = title_
            if not text_ == "":
                self.text = text_
            self.note_dt = datetime.datetime.now()


class ListOfNotes:
    notes: List[Note] = []

    def add_note(self, note_: Note):
        self.notes.append(note_)

    def is_id_in_list(self, note_id: int):
        for note in self.notes:
            if note.note_id == note_id:
                return True
        return False

    def get_by_date(self, date_begin: datetime.datetime, date_end: datetime.datetime):
        export = []
        for note in self.notes:
            if date_begin <= note.note_dt <= date_end:
                export.append(note)
        return export

    def size(self):
        return len(self.notes)

    def get_by_index(self, index) -> Note:
        return self.notes[index]

    def edit_by_id(self, note_id, title_, text_):
        self.notes[note_id].edit(title_, text_)

    def to_string(self) -> str:  # Debug func
        result = ""
        result += "\n\tList of notes:\n\n"

        for note in self.notes:
            result += (f"\t\tNote ID: {note.note_id}\n\t\tNote Title: {note.title}\n\t\tNote text: {note.text}\n\t\t"
                       f"Note date: {note.note_dt}\n\n")

        return result
