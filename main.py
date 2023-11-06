import view
from colorama import Fore


def main():
    try:
        view.start_program()
    except KeyboardInterrupt:
        print(Fore.RED + "Работа прервана. ")


if __name__ == '__main__':
    main()
