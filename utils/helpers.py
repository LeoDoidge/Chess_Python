import pygame
from settings import *


def color(self, square_clicked):
        if square_clicked == None:
            return None
        x, y = square_clicked
        piece = self.grid[y][x]
        return piece[0]

def type_piece(self, square_clicked):
    x, y = square_clicked
    return self.grid[y][x]

def check_occup(self, square_pos):
    for i in range(8):
        for j in range(8):
            if square_pos == (i, j):
                if self.grid[j][i] == "--":
                    return False
                else:
                    return True
                
def square_pos(self, pos):
        x = pos[0]
        y = pos[1]
        square_pos = (int(x / H * 8), int(y / H * 8))
        return square_pos