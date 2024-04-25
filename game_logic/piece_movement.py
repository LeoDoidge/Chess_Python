import pygame 
from utils import helpers
from game_logic import grid
grid = grid.Grid()


def move_piece(start_pos, end_pos, game_clock):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        current_turn = "w" if game_clock % 2 == 0 else "b"

        if helpers.color(start_pos) != current_turn:
            return False

        if not (0 <= start_x < 8 and 0 <= start_y < 8):
            return False

        if not (0 <= end_x < 8 and 0 <= end_y < 8):
            return False
        
        piece = grid.grid[start_y][start_x]

        if grid.grid[end_y][end_x] == "--":

            grid.grid[end_y][end_x] = piece
            grid.grid[start_y][start_x] = "--"
            return True

        return False

def eat_piece(start_pos, end_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    type_piece = grid.grid[start_y][start_x]

    if not (0 <= start_x < 8 and 0 <= start_y < 8):
        return False

    if not (0 <= end_x < 8 and 0 <= end_y < 8):
        return False

    piece = grid.grid[start_y][start_x]

    if grid.grid[end_y][end_x] != "--" and grid.color(start_pos) != grid.color(
        end_pos
    ):

        grid.grid[end_y][end_x] = piece
        grid.grid[start_y][start_x] = "--"
        return True

    return False
