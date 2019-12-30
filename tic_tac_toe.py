# By Benjamin Ombeni
# 
# I will remember this Tic_Tac_Toe game as the first real Python project I ever built. After print('Hello World') of course :)
#
# Description:
# ------------
# This is a Tic Tac Toe game. It is made to be played by two players sitting on the same computer
# and using the keys q,w,e,a,s,d,z,x,c
#
# Example:
# The table is designed as follow on the keyboard:    q | w | e     ->     o | x | x
#                                                    -----------          -----------
#                                                     a | s | f     ->     x | o | x
#                                                    -----------          -----------
#                                                     z | x | c     ->     o | x | o

from os import system, name
from getpass import getpass
from random import randint

# =============================DRAW_TABLE()========================================
def draw_table(table = [' '] * 9, players = {'player1':{'name':'...', 'sign':'...'},'player2':{'name':'...', 'sign':'...'}}):
    '''
    INPUT: (List of 9 characters), Optional Dictionary of players
    TASK: Prints tic tac toa table
    '''
    # clears the screen befor drawing the table
    clear_screen()

    if len(table) < 9:
        print('Incomplete Table!')
    else:
        # prints date and players info
        print('\n')
        _ = system('date') 
        print(f"\n\t\t\t{players['player1']['name']}: {players['player1']['sign']}")
        print(f"\t\t\t{players['player2']['name']}: {players['player2']['sign']}\n")

        # Draws the table
        print(f'\t{table[0]} | {table[1]} | {table[2]}')
        print('\t---------')
        print(f'\t{table[3]} | {table[4]} | {table[5]}')
        print('\t---------')
        print(f'\t{table[6]} | {table[7]} | {table[8]}\n')

# =================================GET_PLAYERS_INFO()=========================================================
def get_players_info():
    '''
    INPUT: none
    TASK: gets player's name and sign
    RETURN: A dictionary of names and signs
    '''
    # Welcome message
    print('\n\tWELCOME TO TIC TAC TOE')

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

    #### Printing info
    #### print(f'\n{player1_name.capitalize()}: {player1_sign}\t {player2_name.capitalize()}: {player2_sign}\n')

    return {'player1':{'name':player1_name, 'sign':player1_sign},
            'player2':{'name':player2_name, 'sign':player2_sign}}

# =============================CLEAR_SCREEN()=====================================
def clear_screen():
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

# =========================ISEVEN()=================================
def isEven(turn):
    '''
    INPUT: Integer
    RETURN: True if integer is even, otherwise False
    '''
    return (turn % 2 == 0)

# =====================GAME_OVER()==============================
def game_over(table):
    '''
    INPUT: Table
    RETURN: Tuple (True if game over, otherwise False, States of the game 'won', 'tied' or 'ongoing')
    '''
    # Won game
    if((table[0] == table[1] == table[2]) and (' ' not in [table[0], table[1], table[2]]) or
       (table[0] == table[4] == table[8]) and (' ' not in [table[0], table[4], table[8]]) or
       (table[0] == table[3] == table[6]) and (' ' not in [table[0], table[3], table[6]]) or
       (table[1] == table[4] == table[7]) and (' ' not in [table[1], table[4], table[7]]) or
       (table[2] == table[4] == table[6]) and (' ' not in [table[2], table[4], table[6]]) or
       (table[2] == table[5] == table[8]) and (' ' not in [table[2], table[5], table[8]]) or
       (table[3] == table[4] == table[5]) and (' ' not in [table[3], table[4], table[5]]) or
       (table[6] == table[7] == table[8]) and (' ' not in [table[6], table[7], table[8]])):
       return(True, 'won')

    # Tied Game
    elif(' ' not in table):
        return (True, 'tied')

    # Ongoing Game
    else:
        return(False, 'ongoing')

# ====================EXECUTE_PLAYER_MOVE()===============================
def execute_player_move(player, table, letters = ('q','w','e','a','s','d','z','x','c')):
    '''
    INPUT: The current player dictionary, the game table list
    RETURN: The game table list after the player's move has been executed
    '''
    # Collecting input
    letter = getpass(f"\t\t\t{player['name']}'s turn\n")

    # Checking for validity of the input
    while letter.lower() not in letters or table[letters.index(letter)] != ' ':
        letter = getpass('')

    # Updating table
    table[letters.index(letter)] = player['sign']

    return table
    
# ============================GAME_ON()=======================================
def game_on(players):
    '''
    INPUT: Players dictionary
    RETURN: None
    '''
    # Setup Game Area
    table = [' ']*9
    draw_table(table, players)
    turn = randint(0,1) # randomly picks who goes first (coin flip)

    # Game loop starts here (game_over returns a tuple with --> (bool, game state))
    while not game_over(table)[0]:
        # Determines players turn (Player1:Even, Player2:Odd)
        if isEven(turn):
            table = execute_player_move(players['player1'], table)
        else:
            table = execute_player_move(players['player2'], table)

        # Draws updated table on the screen 
        draw_table(table, players)
        turn += 1

    # Evaluates results and print them on the screen
    evaluate_results(players, game_over(table)[1], turn)

#===================EVALUATE_RESULTS()================================
def evaluate_results(players, game_state, turn):
    '''
    INPUT: Players Dictionary , State of the game string (won or tied), Last Play Turn Integer
    RETURN: None
    '''
    # Game was won by one of the players
    if game_state == 'won':
        if isEven(turn):
            print(f"\t\t\t{players['player2']['name']} Won!\n")
        else:
            print(f"\t\t\t{players['player1']['name']} Won!\n")

    # Game was tied
    elif game_state == 'tied':
        print('\t\t\tTie!\n')

    else:
        print(f'Error: Invalid Game State!')
# ===========================PLAY_AGAIN()=============================
def play_again():
    '''
    INPUT: None
    TASK: Determines wether current players want to play another game
    RETURN: Boolean
    '''
    # Gets input from the user
    valid_choices = {'y':True,'n':False}
    choice = input('Would you like to play again (y or n): ')

    # Checks for validity
    while choice.lower() not in valid_choices.keys():
        choice = input('Invalid input, try again (y or n): ')

    return valid_choices[choice]
    
# ===========================TIC_TAC_TOE()========================================
def tic_tac_toe():
    '''
    INPUT: None
    TASK: Main Game Function
    RETUEN: None
    '''
    # Getting players info 
    players = get_players_info()
    game_on(players)
    
    # Checks if the players want to keep playing
    while play_again():
        game_on(players)

    print(f'\n\tGood Bye!\n')

# GAME
tic_tac_toe()
