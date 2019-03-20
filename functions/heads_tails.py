from random import random


def flip_coin():
    if random() > 0.5:
        return 'Heads'
    else:
        return 'Tails'


print(flip_coin())


# Default parameters 
def print_this(msg = 'yeah'):
    print(msg)

print_this()    # prints 'yeah'

print_this('Ho')    # prints 'Ho'

# Default paramaters with functions

def add(a, b):
    return a + b


def math(a, b, fn=add):
    return fn(a, b)

def subtract(a, b):
    return a - b

math(2, 2)  # default : add : 4
math(2, 2, subtract)    # subtract : 0

