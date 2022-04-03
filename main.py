from Game import *

if __name__ == '__main__':
    board_game = initial_board()
    print_board(board_game)
    turn = False
    while not game_over(board_game):
        next_move = input("Introduce the coord of square ").upper()
        board_game, siguiente = movement(board_game, next_move, turn)
        if not siguiente:
            print("That is not a legal move")
        else:
            if next_can_move(board_game, not turn):
                turn = not turn
            else:
                print("you can't move")
        print_board(board_game)
    points(board_game)
