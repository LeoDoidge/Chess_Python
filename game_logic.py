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

    def move_piece(self, start_pos, end_pos, game_clock):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        current_turn = "w" if game_clock % 2 == 0 else "b"

        if self.color(start_pos) != current_turn:
            return False

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
        type_piece = self.grid[start_y][start_x]

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


class Pieces:
    def __init__(self) -> None:
        None


class Pawn(Pieces):
    def __init__(self) -> None:
        pass

    def PawnRank(self, square_pos):
        return square_pos[1]

    def ValidMoves(self, start_pos, color):
        ValidMoveList = []
        x, y = start_pos
        if color == "b":
            y += 1
            ValidMoveList.append((x, y))
            if self.PawnRank(start_pos) == 1:
                y += 1
                ValidMoveList.append((x, y))
        if color == "w":
            y -= 1
            ValidMoveList.append((x, y))
            if self.PawnRank(start_pos) == 6:
                y -= 1
                ValidMoveList.append((x, y))
        return ValidMoveList


class Knight(Pieces):
    def ValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]

            if 0 <= new_x < 8 and 0 <= new_y < 8:
                ValidMovesList.append((new_x, new_y))
        return ValidMovesList


class Bishop(Pieces):
    def ValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList.append((new_x, new_y))
        return ValidMovesList


class Rook(Pieces):
    def ValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [(0, 1), (0, -1), (-1, 0), (-1, -0)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList.append((new_x, new_y))
        return ValidMovesList


class Queen(Pieces):
    def ValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [(0, 1), (0, -1), (-1, 0), (-1, -0),(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList.append((new_x, new_y))
        return ValidMovesList


class King(Pieces):
    def ValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [(0, 1), (0, -1), (-1, 0), (-1, -0),(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in possible_moves:
            new_x = x + move[0] 
            new_y = y + move[1] 
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                ValidMovesList.append((new_x, new_y))
        return ValidMovesList
