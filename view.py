import model
from colorama import Fore


def start_program():
    model.import_notes()
    print(Fore.GREEN + "\n\tПрограмма запущена!" + Fore.RESET)
    while True:
        menu()


def menu():
    print(Fore.CYAN + "\n\tВыберите пункт меню: ")

    print(Fore.YELLOW + "\t\t1. " + Fore.BLUE + "Создать заметку" + Fore.YELLOW)
    print("\t\t2. " + Fore.BLUE + "Редактировать заметку" + Fore.YELLOW)
    print("\t\t3. " + Fore.BLUE + "Удалить заметку" + Fore.YELLOW)
    print("\t\t4. " + Fore.BLUE + "Просмотреть список" + Fore.YELLOW)
    print("\t\t5. " + Fore.BLUE + "Просмотреть по дате" + Fore.YELLOW)
    print("\t\t6. " + Fore.BLUE + "Выйти" + Fore.YELLOW)

    try:
        choice = int(input(Fore.GREEN + "\tВыбор: "))
        if not 1 <= choice <= 6:
            raise ValueError  # ValueError - ошибка значения, а в нашем случае значение,
            # не принадлежащее диапазону [1, 6] является ошибочным, так что исключение оправдано
    except ValueError:
        print(Fore.RED + "\n\t\tОшибка ввода! Введите одну цифру от 1 до 6 в соответствии с пунктами меню.")
        return
    except KeyboardInterrupt:
        print(Fore.RED + "\n\t\tВвод отменен.")
        exit(0)

    match choice:
        case 1:
            model.create_note()
        case 2:
            model.edit_note()
        case 3:
            model.remove_note()
        case 4:
            model.list_notes()
        case 5:
            model.filter_by_data()
        case 6:
            print(Fore.LIGHTMAGENTA_EX + "\n\t\tВыход...")
            exit(0)

    # TEMP!!!
    print(model.main_list.to_string())
