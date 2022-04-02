def print_board(board):
    abc = 'A'
    print(' ', end=' ')
    print(abc, end=' ')
    for _ in range(7):
        x = chr(ord(abc) + 1)
        abc = chr(ord(abc) + 1)
        print(x, end=' ')
    print('')
    index = 0
    for row in board:
        print(index+1, end='|')
        index = index + 1
        for i in row:
            print(i, end='|')
        print('')
    abc = 'A'

    print(' ', end=' ')
    print(abc, end=' ')
    for _ in range(7):
        x = chr(ord(abc) + 1)
        abc = chr(ord(abc) + 1)
        print(x, end=' ')
    print('')


def initial_board():
    board = []
    for _ in range(8):
        board.append([' ']*8)
    board[3][3] = '☗'
    board[4][4] = '☗'
    board[3][4] = '☖'
    board[4][3] = '☖'
    return board


def movement(board, move, white):
    token = '☗' if white else '☖'
    move = translate_cord(move)
    board[move[0]][move[1]] = token
    
    return board


def translate_cord(move):
    part_t = ord(move[1])-ord('A')
    return move[0]-1, part_t


def check_up(move,board, white):
    next_cas = move[0]-1 ,move[1]
    while next_cas[0] > 0:
        if white and board[move[0]][move[1]]!= :
        next_cas = next_cas[0] - 1, next_cas[1]
    return

if __name__ == '__main__':
    board_game = initial_board()
    print_board(board_game)
    movement(board_game, (3, 'D'), False)
    print_board(board_game)

