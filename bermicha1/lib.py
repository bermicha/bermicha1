from termcolor import cprint
from pyfiglet import figlet_format


def try_me():
    cprint(figlet_format('Yes! It Works!', font='starwars'),
           'yellow',
           'on_green',
           attrs=['bold'])



if __name__ == "__main__":
    try_me()
