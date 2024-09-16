"""
Module for functions used across the code 
"""

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


class Converter:
    def __init__(self):
        pass

    def ImageName(self, name):
        if name[1] == "p":
            return "Pawn"
        if name[1] == "N":
            return "Knight"
        if name[1] == "B":
            return "Bishop"
        if name[1] == "Q":
            return "Queen"
        if name[1] == "K":
            return "King"
        if name[1] == "R":
            return "Rook"

    def PyToChess(self, coordinates):
        if not (
            isinstance(coordinates, tuple)
            and len(coordinates) == 2
            and all(0 <= i <= 7 for i in coordinates)
        ):
            raise ValueError(
                "Input must be a tuple with two integers in the range 0-7."
            )

        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        row = 8 - coordinates[1]
        column = columns[coordinates[0]]
        return f"{column}{row}"

    def EatNotation(self):
        pass

    def CheckNotation(self):
        pass

    def CheckMateNotation(self):
        pass

    def PawnNotation(self):
        return f"{self.PyToChess(self.destination)}"

    def RookNotation(self):
        return f"R{self.PyToChess(self.destination)}"

    def KnightNotation(self):
        return f"N{self.PyToChess(self.destination)}"

    def BishopNotation(self):
        return f"B{self.PyToChess(self.destination)}"

    def QueenNotation(self):
        return f"Q{self.PyToChess(self.destination)}"

    def KingNotation(self):
        return f"K{self.PyToChess(self.destination)}"
