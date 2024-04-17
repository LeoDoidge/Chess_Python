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

    def square_pos(self, pos):
        x = pos[0]
        y = pos[1]
        square_pos = (int(x / H * 8), int(y / H * 8))
        return square_pos

    def move_piece(self, start_pos, end_pos, game_clock):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        current_turn = "w" if game_clock % 2 == 0 else "b"
        color = self.color(start_pos)

        if self.color(start_pos) != current_turn:
            return False

        if not (0 <= start_x < 8 and 0 <= start_y < 8):
            return False

        if not (0 <= end_x < 8 and 0 <= end_y < 8):
            return False
        
        piece = self.grid[start_y][start_x]

        if self.grid[end_y][end_x] == "--":

            self.grid[end_y][end_x] = piece
            self.grid[start_y][start_x] = "--"
            return True

        return False

    def eat_piece(self, start_pos, end_pos):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        type_piece = self.grid[start_y][start_x]

        if not (0 <= start_x < 8 and 0 <= start_y < 8):
            return False

        if not (0 <= end_x < 8 and 0 <= end_y < 8):
            return False

        piece = self.grid[start_y][start_x]

        if self.grid[end_y][end_x] != "--" and self.color(start_pos) != self.color(
            end_pos
        ):

            self.grid[end_y][end_x] = piece
            self.grid[start_y][start_x] = "--"
            return True

        return False


grid = Grid()


class Pieces:
    def __init__(self):
        self.board = grid.grid

    def PawnRank(self, square_pos):
        return square_pos[1]

    def PawnValidMoves(self, start_pos, color):
        ValidMoveList = []
        x, y = start_pos
        if color == "b":
            y += 1
            ValidMoveList.append((y, x))
            if self.PawnRank(start_pos) == 1:
                y += 1
                ValidMoveList.append((y, x))
        if color == "w":
            y -= 1
            ValidMoveList.append((y, x))
            if self.PawnRank(start_pos) == 6:
                y -= 1
                ValidMoveList.append((y, x))
        return ValidMoveList

    def KnightValidMoves(self, start_pos):
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
                ValidMovesList.append((new_y, new_x))
        return ValidMovesList

    def BishopValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList.append((new_y, new_x))
        return ValidMovesList

    def RookValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [(0, 1), (0, -1), (-1, 0), (-1, -0)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList.append((new_y, new_x))
        return ValidMovesList

    def QueenValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (-1, -0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList.append((new_y, new_x))
        return ValidMovesList

    def KingValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
        possible_moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (-1, -0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                ValidMovesList.append((new_y, new_x))
        return ValidMovesList

    def Pawn_remove_blocked_moves(self, start_pos, color):
        valid_move_list = self.PawnValidMoves(start_pos, color)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                break

        return updated_move_list

    def Knight_remove_blocked_moves(self, start_pos):
        valid_move_list = self.KnightValidMoves(start_pos)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                break

        return updated_move_list

    def Bishop_remove_blocked_moves(self, start_pos):
        valid_move_list = self.BishopValidMoves(start_pos)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                break

        return updated_move_list

    def Rook_remove_blocked_moves(self, start_pos):
        valid_move_list = self.RookValidMoves(start_pos)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                break

        return updated_move_list

    def Queen_remove_blocked_moves(self, start_pos):
        valid_move_list = self.QueenValidMoves(start_pos)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                break

        return updated_move_list

    def King_remove_blocked_moves(self, start_pos):
        valid_move_list = self.KingValidMoves(start_pos)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                break

        return updated_move_list

