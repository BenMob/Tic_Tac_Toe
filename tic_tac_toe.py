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
# =============================DRAW_TABLE()========================================
def draw_table(table = [' ',' ',' ',' ',' ',' ',' ',' ',' '], players = {'player1':{'name':'...', 'sign':'...'},'player2':{'name':'...', 'sign':'...'}}):
    '''
    INPUT: (List of 9 characters), Optional Dictionary of players
    TASK: Prints tic tac toa table
    '''
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
    RETURN: Game winner
    '''
    # Setup Game Area
    clear_screen()
    table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    draw_table(table, players)
    turn = 0

    # Game loop starts here
    while not game_over(table):
        # Determines players turn (Player1:Even, Player2:Odd)
        if isEven(turn):
            table = execute_player_move(players['player1'], table)
        else:
            table = execute_player_move(players['player2'], table)

        # clears the screen
        clear_screen()

        # Draws updated table on the screen 
        draw_table(table, players)
        turn += 1

    # Evaluates results and print them on the screen
    evaluate_results(players,table,turn)

#===================EVALUATE_RESULTS()================================
def evaluate_results(players,table, turn):
    '''
    INPUT: Players Dictionary , Game Table List, Last Play Turn Integer
    RETURN: None
    '''
    if ' ' in table:
        if isEven(turn):
            print(f"\t\t\t{players['player2']['name']} Won!\n")
        else:
            print(f"\t\t\t{players['player1']['name']} Won!\n")
    else:
        print('\t\t\tTie!\n')
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

    print(f'\tGood Bye!\n')

# GAME
tic_tac_toe()




    
