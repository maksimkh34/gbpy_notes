import random

import json_lib
import notes

from colorama import Fore
from datetime import datetime

main_list = notes.ListOfNotes()  # Список, который будет обновляться


def import_notes():
    global main_list
    main_list = json_lib.import_f()


def generate_id():
    rnd = random.Random()
    new_id = rnd.randint(1, 9223372036854775807)
    if not main_list.is_id_in_list(new_id):
        return new_id
    else:
        return generate_id()


def create_note():
    title = input(Fore.BLUE + "\tВведите название заметки: " + Fore.LIGHTCYAN_EX)
    text = input(Fore.BLUE + "\tВведите тело заметки: " + Fore.LIGHTCYAN_EX)

    new_note = notes.Note(title, text)
    global main_list
    main_list.add_note(new_note)
    print(Fore.GREEN + "\n\t\tЗаметка добавлена! ")


def find_note():
    inp = input(Fore.BLUE + "Введите название заметки или её id: " + Fore.LIGHTCYAN_EX)
    if inp.isdigit():
        inp = int(inp)
        for i in range(0, main_list.size()):
            if main_list.get_by_index(i).note_id == inp:
                print(Fore.GREEN + "Заметка найдена! ")
                return i

        print(Fore.RED + "Заметка с таким id не найдена. ")
        return "#$nothing#$"
    else:
        for i in range(0, main_list.size()):
            if main_list.get_by_index(i).title == inp:
                print(Fore.GREEN + "Заметка найдена! ")
                return i
        print(Fore.RED + "Заметка с таким названием не найдена. ")
        return "#$nothing#$"


def edit_note():
    note = find_note()
    if note != "#$nothing#$":
        title = input(Fore.LIGHTYELLOW_EX + "Введите новое название: " + Fore.LIGHTCYAN_EX)
        text = input(Fore.LIGHTYELLOW_EX + "Введите новый текст заметки: " + Fore.LIGHTCYAN_EX)
        main_list.edit_by_id(note, title, text)


def remove_note():
    main_list.remove_by_index(find_note())
    print(Fore.GREEN + "\tЗаметка удалена!\n")


def list_notes():
    print(notes.ListOfNotes.to_string(main_list.notes))


def filter_by_data():
    try:
        date = input(Fore.LIGHTCYAN_EX + "Введите дату начала фильтра в формате гг-мм-дд чч:мм:сс: ")
        dt_begin = datetime.strptime(date, '%y-%m-%d %H:%M:%S')

        date = input(Fore.LIGHTCYAN_EX + "Введите дату конца фильтра в формате гг-мм-дд чч:мм:сс: ")
        dt_end = datetime.strptime(date, '%y-%m-%d %H:%M:%S')
    except ValueError:
        print(Fore.RED + "Дата введена неверно. ")
        return

    print(notes.ListOfNotes.to_string(main_list.get_by_date(dt_begin, dt_end)))


def close():
    json_lib.export_f()
    exit(0)
