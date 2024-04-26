import pygame
from os import path
from settings import *
from utils import helpers
from game_logic import grid

grid = grid.Grid()


def draw_board(highlighted_pos, square_clicked):
    for row in range(board_size):
        for col in range(board_size):
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


def drawPiece(x, y, screen):
    name = grid.grid[y][x]
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
        grid.grid[start_y][start_x] != "--"
        and grid.grid[start_y][start_x][0] == grid.grid[end_y][end_x][0]
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
    elif grid.grid[start_y][start_x][0] != grid.grid[end_y][end_x][0]:
        return None
