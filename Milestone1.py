from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''

    # KEEP ASKING PLAYER 1 TO CHOOSE X OR O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    # ASSIGN PLAYER TWO OPPOSITE MARKER
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)

def place_marker(board, marker, position):