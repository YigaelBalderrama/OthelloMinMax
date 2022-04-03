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
    old_doit = False
    token = '☗' if white else '☖'
    move = translate_cord(move)
    board[move[0]][move[1]] = token
    ## direccionales ##
    if look_up(move, board, white):
        doit, board = check_up(move, board, white)
        old_doit = doit or old_doit
    if look_down(move, board, white):
        doit, board = check_down(move, board, white)
        old_doit = doit or old_doit
    if look_right(move, board, white):
        doit, board = check_right(move, board, white)
        old_doit = doit or old_doit
    if look_left(move, board, white):
        doit, board = check_left(move, board, white)
        old_doit = doit or old_doit
    ## diagonales ##
    if look_ds(move, board, white):
        doit, board = check_ds(move, board, white)
        old_doit = doit or old_doit
    if look_ii(move, board, white):
        doit, board = check_ii(move, board, white)
        old_doit = doit or old_doit
    if look_di(move, board, white):
        doit, board = check_di(move, board, white)
        old_doit = doit or old_doit
    if look_id(move, board, white):
        doit, board = check_id(move, board, white)
        old_doit = doit or old_doit
    if not old_doit:
        board[move[0]][move[1]] = ' '
    return board, old_doit


def is_on_board(place):
    if place[0] < 0:
        return False
    if place[0] >= 8:
        return False
    if place[1] < 0:
        return False
    if place[1] >= 8:
        return False
    return True


def translate_cord(move):
    move = list(move.strip(" "))
    part_t = ord(move[0])-ord('A')
    return int(move[1])-1, part_t


def look_up(move, board, white):
    next_cas = move[0] + 1, move[1]
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[0] < 8 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0] + 1, next_cas[1]
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[0] < 8 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0] + 1, next_cas[1]
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_down(move, board, white):
    next_cas = move[0] - 1, move[1]
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[0] >= 0 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0] - 1, next_cas[1]
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[0] >= 0 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0] - 1, next_cas[1]
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_right(move, board, white):
    next_cas = move[0], move[1] + 1
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[1] < 8 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0], next_cas[1] + 1
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[1] < 8 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0], next_cas[1] + 1
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_left(move, board, white):
    next_cas = move[0], move[1] - 1
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[1] >= 0 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0], next_cas[1] - 1
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[1] >= 0 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0], next_cas[1] - 1
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_ds(move, board, white):
    next_cas = move[0] + 1, move[1] + 1
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[1] < 8 and next_cas[0] < 8 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0] + 1, next_cas[1] + 1
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[1] < 8 and next_cas[0] < 8 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0] + 1, next_cas[1] + 1
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_ii(move, board, white):
    next_cas = move[0] - 1, move[1] - 1
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[1] >= 0 and next_cas[0] > 0 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0] - 1, next_cas[1] - 1
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[1] >= 0 and next_cas[0] > 0 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0] - 1, next_cas[1] - 1
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_di(move, board, white):
    next_cas = move[0] - 1, move[1] + 1
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[1] >= 0 and next_cas[0] < 8 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0] - 1, next_cas[1] + 1
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[1] >= 0 and next_cas[0] < 8 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0] - 1, next_cas[1] + 1
        return board[next_cas[0]][next_cas[1]] == '☖'


def look_id(move, board, white):
    next_cas = move[0] + 1, move[1] - 1
    if not is_on_board(next_cas):
        return False
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False
    if white:
        while next_cas[1] < 8 and next_cas[0] >= 0 and board[next_cas[0]][next_cas[1]] == '☖':
            next_cas = next_cas[0] + 1, next_cas[1] - 1
        return board[next_cas[0]][next_cas[1]] == '☗'
    else:
        while next_cas[1] < 8 and next_cas[0] >= 0 and board[next_cas[0]][next_cas[1]] == '☗':
            next_cas = next_cas[0] + 1, next_cas[1] - 1
        return board[next_cas[0]][next_cas[1]] == '☖'


def check_di(move, board, white):
    old_board = board
    next_cas = move[0] - 1, move[1] + 1
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0] - 1, next_cas[1] + 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0] - 1, next_cas[1] + 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_id(move, board, white):
    old_board = board
    next_cas = move[0] + 1, move[1] - 1
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0] + 1, next_cas[1] - 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0] + 1, next_cas[1] - 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_ii(move, board, white):
    old_board = board
    next_cas = move[0] - 1, move[1] - 1
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0] - 1, next_cas[1] - 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0] - 1, next_cas[1] - 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_ds(move, board, white):
    old_board = board
    next_cas = move[0] + 1, move[1] + 1
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0] + 1, next_cas[1] + 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0] + 1, next_cas[1] + 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_up(move, board, white):
    old_board = board
    next_cas = move[0]+1, move[1]
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0]+1, next_cas[1]
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0] + 1, next_cas[1]
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_down(move, board, white):
    old_board = board
    next_cas = move[0]-1, move[1]
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0]-1, next_cas[1]
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0] - 1, next_cas[1]
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_right(move, board, white):
    old_board = board
    next_cas = move[0], move[1] + 1
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while next_cas[1] < 8 and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0], next_cas[1] + 1
        if next_cas[1] < 8 and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while next_cas[1] < 8 and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0], next_cas[1] + 1
        if next_cas[1] < 8 and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def check_left(move, board, white):
    old_board = board
    next_cas = move[0], move[1] - 1
    if board[next_cas[0]][next_cas[1]] != '☖' and white:
        return False, board
    if board[next_cas[0]][next_cas[1]] != '☗' and not white:
        return False, board
    if white:
        board[next_cas[0]][next_cas[1]] = '☖'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            board[next_cas[0]][next_cas[1]] = '☗'
            next_cas = next_cas[0], next_cas[1] - 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            return True, board
        else:
            return False, old_board
    else:
        board[next_cas[0]][next_cas[1]] = '☗'
        while is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☗':
            board[next_cas[0]][next_cas[1]] = '☖'
            next_cas = next_cas[0], next_cas[1] - 1
        if is_on_board(next_cas) and board[next_cas[0]][next_cas[1]] == '☖':
            return True, board
        else:
            return False, old_board


def game_over(board):
    for row in board:
        for i in row:
            if i == ' ':
                return False
    return True


def points(board):
    white, black = 0, 0
    for row in board:
        for i in row:
            if i == '☗':
                white = white + 1
            else:
                black = black + 1
    print("Points of black player: ", black)
    print("Points of white player: ", white)


def checker(move, board, white):
    ## direccionales ##
    if look_up(move, board, white):
        return True
    if look_down(move, board, white):
        return True
    if look_right(move, board, white):
        return True
    if look_left(move, board, white):
        return True
    ## diagonales ##
    if look_ds(move, board, white):
        return True
    if look_ii(move, board, white):
        return True
    if look_di(move, board, white):
        return True
    if look_id(move, board, white):
        return True
    return False


def next_can_move(board, white):
    for i in range(8):
        for j in range(8):
            if board[i][j] == ' ':
                if checker((i, j), board, white):
                    return True
    return False
