import datetime

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

    def edit(self, title_="#%NOCHANGES#%", text_="#%NOCHANGES#%"):
        if not title_ == "#%NOCHANGES#%" and text_ == "#%NOCHANGES#%":
            if not title_ == "#%NOCHANGES#%":
                self.title = title_
            if not text_ == "#%NOCHANGES#%":
                self.text = text_
            self.note_dt = datetime.datetime.now()


class ListOfNotes:
    notes = []

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

    