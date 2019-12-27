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


tb = ['x','x','o','x','o','o','x','o','o']
#tb = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
help(draw_table)