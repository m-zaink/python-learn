# ---------------------------------------------------------------------------------------------------
# Rock - Paper - Scissor Game Simulation
# ---------------------------------------------------------------------------------------------------

import os
import random

# ---------------------------------------------------------------------------------------------------
# Function to validate the inputs if they aren't properly entered
# ---------------------------------------------------------------------------------------------------

def validate_inputs(p1, p2):
    if (['s', 'r', 'p'].__contains__(p1[0]) and ['s', 'r', 'p'].__contains__(p2[0])):
        return
    else:
        os.system('clear')
        print('!!!! Improper choice of options !!!!')
        exit(0)

# ---------------------------------------------------------------------------------------------------
# Function to return appropriate names
# ---------------------------------------------------------------------------------------------------

def get_approp_choice (p):
    appro_words = {'s':'scissor', 'r':'rock', 'p':'paper'};
    return appro_words[p]

# ---------------------------------------------------------------------------------------------------
# Logic of the game begins
# ---------------------------------------------------------------------------------------------------

print('# -------------------------------------------------------------------------------------- #')
print('Rock - Paper - Scissors | Best - Of - Three - Series')
print('# -------------------------------------------------------------------------------------- #')

num_of_rounds = 0
score_p1 = 0
score_p2 = 0

player1 = input('Player 1 - Enter your name : ')
player2 = input('Player 2 - Enter your name : ')

winning_cases = {'s':'p', 'p':'r', 'r':'s'}

while (num_of_rounds != 3):
    os.system('clear')

    winner = 'Draw'

    print('# -------------------------------------------------------------------------------------- #')
    print(f' ROUND #{num_of_rounds + 1}')
    print('# -------------------------------------------------------------------------------------- #')

    p1 = input(player1 + ' - Enter your choice : ')
    os.system('clear')
    print('# -------------------------------------------------------------------------------------- #')
    print(f' ROUND #{num_of_rounds + 1}')
    print('# -------------------------------------------------------------------------------------- #')

    p2 = input(player2 + ' - Enter your choice : ')

    os.system('clear')

    p1 = p1.lower()
    p2 = p2.lower()

    validate_inputs(p1, p2)

    if p1[0] == p2[0]:
        pass
    elif (winning_cases[p1[0]] == p2[0]):
        winner = player1
        score_p1 += 1
    else:
        score_p2 += 1
        winner = player2

    os.system('clear')

    #  Prints a single round's result
    if (winner != 'Draw'):
        print(player1 + ' had chosen : ' + get_approp_choice(p1[0]))
        print(player2 + ' had chosen : ' + get_approp_choice(p2[0]))
        print(winner + ' wins the round.')
    else:
        print('!!!! Draw !!!!')
    
    input('Continue ? ')
    num_of_rounds += 1

# Prints the complete series result
os.system('clear')
if score_p1 == score_p2 : 
    print('!!!! Draw Series !!!!')
elif score_p1 > score_p2 :
    print('!!! ' + player1 + ' wins the series !!!')
else:
    print('!!! ' + player2 + ' wins the series !!!')
