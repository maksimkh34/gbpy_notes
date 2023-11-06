import model
import notes
import json
import datetime


def import_f() -> notes.ListOfNotes:
    output = notes.ListOfNotes()
    with open('output.json') as f:
        notes_json = json.load(f)['notes']

    for note_json in notes_json:
        new_note = notes.Note("", "")
        new_note.import_note(
            note_json['id'],
            note_json['title'],
            note_json['text'],
            datetime.datetime.strptime(str(note_json['dt'])[2:], '%y-%m-%d %H:%M:%S')
        )
        output.add_note(new_note)

    return output


def export_f():
    with open('output.json', 'w') as f:
        f.write(json.dumps(model.main_list.to_dict()))
