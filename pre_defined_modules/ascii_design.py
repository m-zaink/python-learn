from pyfiglet import figlet_format
from termcolor import colored

cool_string = input('Enter a cool string : ')
color = input('Enter the color : ')

try:
    print(colored(figlet_format(cool_string), color))
except BaseException:
    print(colored(figlet_format(cool_string), 'magenta'))
