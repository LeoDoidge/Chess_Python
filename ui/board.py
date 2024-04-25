import pygame 
from os import path
from settings import *
from utils import helpers
from game_logic import grid, pieces

def drawPiece(self, x, y, screen):
        name = self.grid[y][x]
        if name == "--":
            pass
        else:
            image = pygame.image.load(path.join("Images", name + ".png"))
            imagerect = image.get_rect()
            imagerect.left = (W - H) / 2 + x * H / 8
            imagerect.top = y * H / 8
            screen.blit(image, imagerect)

def highlight(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        if (
            self.grid[start_y][start_x] != "--"
            and self.grid[start_y][start_x][0] == self.grid[end_y][end_x][0]
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
        elif self.grid[start_y][start_x][0] != self.grid[end_y][end_x][0]:
            return None