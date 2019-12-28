# By Benjamin Ombeni
# 
# Description:
# ------------
# This is a Tic Tac Toe game. It is made to be played by two players sitting on the same computer
# and using the keys q,w,e,a,s,d,z,x,c as the table.
#
# The table is designed as follow on the keyboard:    q | w | e     ->     o | x | x
#                                                    -----------          -----------
#                                                     a | s | f     ->     x | o | x
#                                                    -----------          -----------
#                                                     z | x | c     ->     o | x | o

from os import system, name
from getpass import getpass

def draw_table(table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    '''
    INPUT: (List of 9 characters)
    TASK: Prints tic tac toa table
    '''
    if len(table) < 9:
        print('Insufficient number of checks in TTT table!')
    else:
        print(f'\n\t{table[0]} | {table[1]} | {table[2]}')
        print('\t---------')
        print(f'\t{table[3]} | {table[4]} | {table[5]}')
        print('\t---------')
        print(f'\t{table[6]} | {table[7]} | {table[8]}\n')

# ==========================================================================================
def get_players_info():
    '''
    INPUT: none
    TASK: gets player's name and sign
    RETURN: A dictionary of names and signs
    '''
    # Getting player's names
    player1_name = input('\nPlayer one username: ' )
    player2_name = input('Player two username: ' )

    # getting player's game signs
    player1_sign = input(f'\n{player1_name.capitalize()}, enter your sign (o or x): ')
    while player1_sign.lower() not in 'ox':
        player1_sign = input('Incorrect sign, try again: ')

    if player1_sign.lower() == 'x':
        player2_sign = 'o'
    else:
        player2_sign = 'x'

    # Printing info
    print(f'\n{player1_name.capitalize()}: {player1_sign}\t {player2_name.capitalize()}: {player2_sign}\n')

    return {'player1':{'name':player1_name, 'sign':player1_sign},
            'player2':{'name':player2_name, 'sign':player2_sign}}

# =================================================================================================
def clear():
    '''
    INPUT: None
    TASK: Clears the OS screen
    RETURN: None
    '''
    # For windows
    if name == 'nt':
        _ = system('cls')
    # For max and linux (name == posix)
    else:
        _ = system('clear')

# ================================================================================================
def update_table(player, letter, table, letters = ('q','w','e','a','s','d','z','x','c')):
    '''
    INPUT: A valid letter, a sign(x or o), A list constituting the game table
    TASK: Updates the list after each play
    OUTPUT: Updated list
    '''
    if letter in letters and table[letters.index(letter) == ' ']:
        table[letters.index(letter)] = player['sign']
    else:
        pass
    return table

# ========================================================================================
def isEven(number):
    '''
    INPUT: Integer
    RETURN: True if integer is even, otherwise False
    '''
    return (number % 2 == 0)

# ===================================================
def game_over(table):
    '''
    INPUT: Table
    RETURN: True if game is over, otherwise False
    '''
    return (' ' not in table or
            (table[0] == table[1] == table[2]) and (' ' not in [table[0], table[1], table[2]]) or
            (table[0] == table[4] == table[8]) and (' ' not in [table[0], table[4], table[8]]) or
            (table[0] == table[3] == table[6]) and (' ' not in [table[0], table[3], table[6]]) or
            (table[1] == table[4] == table[7]) and (' ' not in [table[1], table[4], table[7]]) or
            (table[2] == table[4] == table[6]) and (' ' not in [table[2], table[4], table[6]]) or
            (table[2] == table[5] == table[8]) and (' ' not in [table[2], table[5], table[8]]) or
            (table[3] == table[4] == table[5]) and (' ' not in [table[3], table[4], table[5]]) or
            (table[6] == table[7] == table[8]) and (' ' not in [table[6], table[7], table[8]]))

# ===================================================================
def play():
    # Getting players info and initializing table and turns
    players = get_players_info()
    clear()
    draw_table()
    table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    turn = 0

    # Game loop starts here
    while not game_over(table):
        letter = getpass('')
        clear()

        # Determine players turns (Player1:Even, Player2:Odd)
        if isEven(turn):
            table = update_table(players['player1'], letter, table)
        else:
            table = update_table(players['player2'], letter, table)
        
        # Draws updated table on the screen 
        draw_table(table)
        turn += 1

    print('\nGame Over\n') 

# ===================================================================

play()

    
