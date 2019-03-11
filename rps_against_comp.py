# ---------------------------------------------------------------------------------------------------
# Rock - Paper - Scissor Game Simulation
# ---------------------------------------------------------------------------------------------------

import os
import random

# ---------------------------------------------------------------------------------------------------
# Function to validate the inputs if they aren't properly entered
# ---------------------------------------------------------------------------------------------------

def validate_inputs(p1, p2):
    if (p1[0] == 's' or p1[0] == 'r' or p1[0] == 'p') and  (p2[0] == 's' or p2[0] == 'r' or p2[0] == 'p'):
        return
    else:
        os.system('clear')
        print('!!!! Improper choice of options !!!!')
        exit(0)

# ---------------------------------------------------------------------------------------------------
# Function to return appropriate names
# ---------------------------------------------------------------------------------------------------

def get_approp_choice (p):
    if p == 's':
        return 'scissor'
    if p == 'r':
        return 'rock'
    if p == 'p':
        return 'paper'

# ---------------------------------------------------------------------------------------------------
# Logic of the game begins
# ---------------------------------------------------------------------------------------------------

print('# -------------------------------------------------------------------------------------- #')
print('Rock - Paper - Scissors | Best - Of - Three - Series')
print('# -------------------------------------------------------------------------------------- #')

num_of_rounds = 0
score_p1 = 0
score_p2 = 0

player1 = input('Human Player - Enter your name : ')
player2 = 'Napoleon'

comp_choices = ['rock', 'paper', 'scissor']

while (num_of_rounds != 3):
    os.system('clear')

    winner = 'Draw'

    print('# -------------------------------------------------------------------------------------- #')
    print(f' ROUND #{num_of_rounds + 1}')
    print('# -------------------------------------------------------------------------------------- #')

    p1 = input(player1 + ' - Enter your choice : ')
    p2 = comp_choices[random.randint(0, 2)]

    os.system('clear')

    p1 = p1.lower()
    p2 = p2.lower()

    validate_inputs(p1, p2)

    if p1[0] == p2[0]:
        pass
    elif (p1[0] == 's' and p2[0] == 'p') or (p1[0] == 'p' and p2[0] == 'r') or (p1[0] == 'r' and p2[0] == 's'):
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
    print(player1 + ' wins the series.')
else:
    print(player2 + ' wins the series.')
