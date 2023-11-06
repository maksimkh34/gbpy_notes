import datetime
from typing import List
import model
from colorama import Fore


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

    def import_note(self, note_id_, title_, text_, dt_):
        self.note_id = note_id_
        self.text = text_
        self.title = title_
        self.note_dt = dt_

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

    @staticmethod
    def to_string(notes, date_filter_text="") -> str:
        if len(notes) == 0:
            print(Fore.YELLOW + "\n\tСписок пуст! ", end="")
            return ""

        result = ""
        result += Fore.GREEN + "\n\tСписок заметок" + Fore.CYAN + date_filter_text + Fore.GREEN + ":\n\n"

        for note in notes:
            result += (f"{Fore.LIGHTCYAN_EX}\t\tID заметки: {Fore.LIGHTBLUE_EX}{note.note_id}{Fore.LIGHTCYAN_EX}"
                       f"\n\t\tНазвание: {Fore.LIGHTBLUE_EX}{note.title}{Fore.LIGHTCYAN_EX}\n\t\t"
                       f"Текст: {Fore.LIGHTBLUE_EX}{note.text}\n\t\t"
                       f"{Fore.LIGHTCYAN_EX}Дата создания(изменения): {Fore.LIGHTBLUE_EX}{str(note.note_dt).split(".")[0]}\n\n")

        return result

    def remove_by_index(self, index):
        self.notes.pop(index)

    def to_dict(self) -> {}:
        output = {"notes": []}

        for note in self.notes:
            output["notes"].append({
                "id": note.note_id,
                "title": note.title,
                "text": note.text,
                "dt": str(note.note_dt).split(".")[0]
            })

        return output
