import pygame
from os import path
from globals import *


class Grid:
    grid = []

    def __init__(self):
        self.grid = (
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        )

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

    def color(self, square_clicked):
        if square_clicked == None:
            return None
        x, y = square_clicked
        piece = self.grid[y][x]
        return piece[0]

    def check_occup(self, pos):
        if pos == []:
            pass
        else:
            x = pos[0]
            y = pos[1]
            square_pos = (int(x / H * 8), int(y / H * 8))
            for i in range(8):
                for j in range(8):
                    if square_pos == (i, j):
                        if self.grid[j][i] == "--":
                            return False
                        else:
                            return True

    def highlight(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        if (
            self.grid[start_y][start_x] != "--"
            and self.grid[start_y][start_x][0] == self.grid[end_y][end_x][0]
        ):
            # Highlight the selected piece with a green border
            pygame.draw.rect(
                screen,
                (0, 255, 0),  # Green color
                (
                    (start_x * square_size),
                    (start_y * square_size),
                    square_size,
                    square_size,
                ),
                3,  # Border width
            )
        elif self.grid[start_y][start_x][0] != self.grid[end_y][end_x][0]:
            print(self.grid[end_y][end_x][0])
            return None

    def square_pos(self, pos):
        x = pos[0]
        y = pos[1]
        square_pos = (int(x / H * 8), int(y / H * 8))
        return square_pos

    def move_piece(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        # Ensure the start position is valid
        if not (0 <= start_x < 8 and 0 <= start_y < 8):
            return False

        # Ensure the end position is valid
        if not (0 <= end_x < 8 and 0 <= end_y < 8):
            return False

        # Get the piece from the start position
        piece = self.grid[start_y][start_x]

        # Check if the end position is empty
        if self.grid[end_y][end_x] == "--":
            # Move the piece to the end position and clear the start position
            self.grid[end_y][end_x] = piece
            self.grid[start_y][start_x] = "--"
            return True

        return False  # Return False if the move is not valid

    def eat_piece(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos

        # Ensure the start position is valid
        if not (0 <= start_x < 8 and 0 <= start_y < 8):
            return False

        # Ensure the end position is valid
        if not (0 <= end_x < 8 and 0 <= end_y < 8):
            return False

        # Get the piece from the start position
        piece = self.grid[start_y][start_x]

        # Check if the end position is not empty and has an opponent's piece
        if self.grid[end_y][end_x] != "--" and self.color(start_pos) != self.color(
            end_pos
        ):
            # Capture the opponent's piece: move the piece to the end position and clear the start position
            self.grid[end_y][end_x] = piece
            self.grid[start_y][start_x] = "--"
            return True

        return False  # Return False if the eat is not valid


# Pieces logic


def load_image(imagename):
    return pygame.image.load(imagename)


class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        if color == 0:
            color = "w"
        else:
            color = "b"
        self.color = color

    def get_name(self):
        return [self.name]

    def position(self, x, y):
        self.x = x
        self.y = y

    def get_legal_moves(self):
        return []


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = self.color + "K"


class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = self.color + "Q"


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = self.color + "p"


class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = self.color + "N"


class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = self.color + "B"


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.name = self.color + "R"
