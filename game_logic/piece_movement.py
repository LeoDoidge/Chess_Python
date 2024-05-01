import pygame
from utils import helpers
from ui import board
from pprint import pprint
from game_logic import pieces


PiecesClass = pieces.Pieces()

Legal_Moves_Dict = {
    "bp": PiecesClass.Pawn_remove_blocked_moves,
    "wp": PiecesClass.Pawn_remove_blocked_moves,
    "bR": PiecesClass.Rook_remove_blocked_moves,
    "wR": PiecesClass.Rook_remove_blocked_moves,
    "bN": PiecesClass.Knight_remove_blocked_moves,
    "wN": PiecesClass.Knight_remove_blocked_moves,
    "bB": PiecesClass.Bishop_remove_blocked_moves,
    "wB": PiecesClass.Bishop_remove_blocked_moves,
    "bQ": PiecesClass.Queen_remove_blocked_moves,
    "wQ": PiecesClass.Queen_remove_blocked_moves,
    "bK": PiecesClass.King_remove_blocked_moves,
    "wK": PiecesClass.King_remove_blocked_moves,
}
Legal_Eats_Dict = {
    "bp": PiecesClass.PawnEat,
    "wp": PiecesClass.PawnEat,
    "bR": PiecesClass.Rook_remove_blocked_moves,
    "wR": PiecesClass.Rook_remove_blocked_moves,
    "bN": PiecesClass.Knight_remove_blocked_moves,
    "wN": PiecesClass.Knight_remove_blocked_moves,
    "bB": PiecesClass.Bishop_remove_blocked_moves,
    "wB": PiecesClass.Bishop_remove_blocked_moves,
    "bQ": PiecesClass.Queen_remove_blocked_moves,
    "wQ": PiecesClass.Queen_remove_blocked_moves,
    "bK": PiecesClass.King_remove_blocked_moves,
    "wK": PiecesClass.King_remove_blocked_moves,
}


def move_piece(start_pos, end_pos, game_clock):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    name = helpers.type_piece(start_pos)
    color = helpers.color(start_pos)
    current_turn = "w" if game_clock % 2 == 0 else "b"

    if end_pos not in Legal_Moves_Dict[name](start_pos):
        return False

    if helpers.color(start_pos) != current_turn:
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


def eat_piece(start_pos, end_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    name = helpers.type_piece(start_pos)
    color = helpers.color(start_pos)

    if not (0 <= start_x < 8 and 0 <= start_y < 8):
        return False
    
    if end_pos not in Legal_Eats_Dict[name](start_pos):
       return False

    if not (0 <= end_x < 8 and 0 <= end_y < 8):
        return False

    piece = board.Grid.grid[start_y][start_x]

    if board.Grid.grid[end_y][end_x] != "--" and helpers.color(
        start_pos
    ) != helpers.color(end_pos):

        board.Grid.grid[end_y][end_x] = piece
        board.Grid.grid[start_y][start_x] = "--"
        return True

    return False
