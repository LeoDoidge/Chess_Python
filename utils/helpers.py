import pygame
from settings import *
from game_logic import grid

grid= grid.Grid()


def color(square_clicked):
    if square_clicked == None:
        return None
    x, y = square_clicked
    piece = grid.grid[y][x]
    return piece[0]


def type_piece(square_clicked):
    x, y = square_clicked
    return grid.grid[y][x]


def check_occup(square_pos):
    for i in range(8):
        for j in range(8):
            if square_pos == (i, j):
                if grid.grid[j][i] == "--":
                    return False
                else:
                    return True


def square_pos(pos):
    x = pos[0]
    y = pos[1]
    square_pos = (int(x / H * 8), int(y / H * 8))
    return square_pos
