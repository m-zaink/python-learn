# ---------------------------------------------------------------------------------------------------
# Rock - Paper - Scissor Game Simulation
# ---------------------------------------------------------------------------------------------------

import os

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
# Logic of the game begins
# ---------------------------------------------------------------------------------------------------


print('# -------------------------------------------------------------------------------------- #')
print('Rock - Paper - Scissors')
print('# -------------------------------------------------------------------------------------- #')

player1 = input('Player 1 - Enter your name : ')
player2 = input('Player 2 - Enter your name : ')


os.system('clear')

winner = 'Draw'

p1 = input(player1 + ' - Enter your choice : ')
os.system('clear')
p2 = input(player2 + ' - Enter your choice : ')

p1 = p1.lower()
p2 = p2.lower()

validate_inputs(p1, p2)

if p1 == p2:
    winner = 'Draw'
elif (p1[0] == 's' and p2[0] == 'p') or (p1[0] == 'p' and p2[0] == 'r') or (p1[0] == 'r' and p2[0] == 's'):
    winner = player1
else:
    winner = player2

os.system('clear')

if (winner != 'Draw'):
    print(winner + ' wins the game')
else:
    print('!!!! Draw !!!!')
