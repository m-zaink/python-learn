import requests as req
from pyfiglet import figlet_format as fg
from termcolor import colored
from random import choice

url = 'https://icanhazdadjoke.com/search'

key = input('Enter search key : ')

res = req.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': key}
)

data = res.json()

colors = ('green', 'blue', 'white', 'yellow', 'cyan')

if not data['results']:
    print(fg('No jokes found on that!'))
    exit
else:
    print(fg('WEIRD JOKES'))

for result in data['results']:
    print(colored(
        '+ ' + result['joke'],
        color=choice(colors),
        on_color='on_white'
    ))
