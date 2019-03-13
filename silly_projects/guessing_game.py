from random import randint
from os import system
number = randint(1, 10)
guess = -1
choice = 'n'
print(number)

while True:
    guess = int(input('Enter your guess : '))
    if guess > number :
        print('Too high')
    elif guess < number :
        print('Too low')
    else:
        print('Awesome. Right on.')
        choice = input('Want to continue?')
        if(choice.lower()[0] == 'y'):
            system('clear')
            number = randint(1, 10)
        else:
            break