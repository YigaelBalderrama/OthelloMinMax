from Game import *


def nro_of_sons(board, white):
    res = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == ' ':
                if checker((i, j), board, white):
                    res = res + 1
    return res


def heuristic1(board, white):
    pass


def heuristic2(board, white):
    pass


def heuristic3(board, white):
    pass


class State:

    def __init__(self, board, white, father):
        self.board = board
        self.alpha = 0
        self.beta = 0
        self.nro_sons = nro_of_sons(board, white)
        self.white = white
        self.child = []
        self.father = father

    def put_son(self, son):
        self.child.append(son)
        if self.nro_sons == len(self.child):
            self.father.actualize()

    def actualize(self):
        if self.father is not None:
            self.father.putson(heuristic1(self.board, self.white))


