'''
This module handles all piece movement
'''

from utils import helpers
from ui import board
from game_logic import pieces


PiecesClass = pieces.Pieces()

legal_moves_dict = {
    "bp": PiecesClass.PawnLegalMoves,
    "wp": PiecesClass.PawnLegalMoves,
    "bR": PiecesClass.RookLegalMoves,
    "wR": PiecesClass.RookLegalMoves,
    "bN": PiecesClass.KnightLegalMoves,
    "wN": PiecesClass.KnightLegalMoves,
    "bB": PiecesClass.BishopLegalMoves,
    "wB": PiecesClass.BishopLegalMoves,
    "bQ": PiecesClass.QueenLegalMoves,
    "wQ": PiecesClass.QueenLegalMoves,
    "bK": PiecesClass.KingLegalMoves,
    "wK": PiecesClass.KingLegalMoves,
}
legal_eats_dict = {
    "bp": PiecesClass.PawnEats,
    "wp": PiecesClass.PawnEats,
    "bR": PiecesClass.RookEats,
    "wR": PiecesClass.RookEats,
    "bN": PiecesClass.KnightEat,
    "wN": PiecesClass.KnightEat,
    "bB": PiecesClass.BishopEats,
    "wB": PiecesClass.BishopEats,
    "bQ": PiecesClass.QueenEats,
    "wQ": PiecesClass.QueenEats,
    "bK": PiecesClass.KingEats,
    "wK": PiecesClass.KingEats,
}


def MovePiece(start_pos, end_pos, game_clock):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    name = helpers.TypePiece(start_pos)
    current_turn = "w" if game_clock % 2 == 0 else "b"

    if end_pos not in legal_moves_dict[name](start_pos):
        return False

    if helpers.Color(start_pos) != current_turn:
        return False

    if not (0 <= start_x < 8 and 0 <= start_y < 8):
        return False

    if not (0 <= end_x < 8 and 0 <= end_y < 8):
        return False

    piece = board.Grid.grid[start_y][start_x]

    if board.Grid.grid[end_y][end_x] == "--":

        board.Grid.grid[end_y][end_x] = piece
        board.Grid.grid[start_y][start_x] = "--"
        return True

    return False


def EatPiece(start_pos, end_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    name = helpers.TypePiece(start_pos)

    if not (0 <= start_x < 8 and 0 <= start_y < 8):
        return False

    if end_pos not in legal_eats_dict[name](start_pos):
        return False

    if not (0 <= end_x < 8 and 0 <= end_y < 8):
        return False

    piece = board.Grid.grid[start_y][start_x]

    if board.Grid.grid[end_y][end_x] != "--" and helpers.Color(
        start_pos
    ) != helpers.Color(end_pos):

        board.Grid.grid[end_y][end_x] = piece
        board.Grid.grid[start_y][start_x] = "--"
        return True

    return False
