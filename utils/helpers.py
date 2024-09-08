from settings import *

from ui import board


def ListMerger(item):
    return item[0] + item[1]


def Color(clicked_pos):
    if clicked_pos is None:
        return None
    x, y = clicked_pos
    piece = board.Grid.grid[y][x]
    return piece[0]


def TypePiece(clicked_pos):
    x, y = clicked_pos
    return board.Grid.grid[y][x]

def TypeMove(clicked_pos): 
    Move = ""
    Piece = TypePiece(clicked_pos)
    
    return Move

def CheckOccup(square_pos):
    for i in range(8):
        for j in range(8):
            if square_pos == (i, j):
                if board.Grid.grid[j][i] == "--":
                    return False
    return True


def SquarePos(pos):
    x = pos[0]
    y = pos[1]
    if x > 500:
        return None
    square_pos = (int(x / H * 8), int(y / H * 8))
    return square_pos

def ClockSwitch(GAME_CLOCK):
    if GAME_CLOCK == 0:
        GAME_CLOCK = 1
    elif GAME_CLOCK == 1:
        GAME_CLOCK = 0
        return GAME_CLOCK