import pygame
from os import path
from settings import *
from utils import helpers
from pprint import pprint

class Grid:
    grid = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

    def __init__(self):
        pass


def drawPiece(x, y, screen):
    if 0 <= x < 8 and 0 <= y < 8:  # Check if x and y are within the valid range
        name = Grid.grid[y][x]
        if name == "--":
            pass
        else:
            image = pygame.image.load(path.join("assets", "images", name + ".png"))
            imagerect = image.get_rect()
            imagerect.left = (W - H) / 2 + x * H / 8
            imagerect.top = y * H / 8
            screen.blit(image, imagerect)

def highlight(start_pos, end_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    if (
        Grid.grid[start_y][start_x] != "--"
        and Grid.grid[start_y][start_x][0] == Grid.grid[end_y][end_x][0]
    ):
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (
                (start_x * square_size),
                (start_y * square_size),
                square_size,
                square_size,
            ),
            3,
        )
    elif Grid.grid[start_y][start_x][0] != Grid.grid[end_y][end_x][0]:
        return None
    

def draw_board(highlighted_pos, square_clicked):
    for row in range(8):
        for col in range(8):
            x = col * square_size
            y = row * square_size
            if (row + col) % 2 == 0:
                pygame.draw.rect(
                    screen, (255, 255, 255), (x, y, square_size, square_size)
                )
            else:
                pygame.draw.rect(
                    screen, (150, 150, 150), (x, y, square_size, square_size)
                )

    for i in range(8):
        for j in range(8):
            drawPiece(i, j, screen)

    if highlighted_pos is not None:
        highlight(highlighted_pos, square_clicked)