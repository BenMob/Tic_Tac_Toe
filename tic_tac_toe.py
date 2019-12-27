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

# ===============================================================

def get_player_info():
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


print(get_player_info()['player2']['sign'])