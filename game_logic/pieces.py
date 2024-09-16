"""
This module handles all calculation of legal moves
"""

from ui import board
from utils import helpers


class Pieces:
    def __init__(self):
        self.board = board.Grid.grid

    def PawnRank(self, square_pos):
        return square_pos[1]

    def KingLegalMoves(self, start_pos):
        total_moves = []
        legal_moves = []
        possible_moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        x, y = start_pos
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                total_moves.append((new_x, new_y))
        for move in total_moves:
            x, y = move
            if self.board[y][x] == "--":
                legal_moves.append(move)
            else:
                pass
        return legal_moves

    def QueenLegalMoves(self, start_pos):
        legal_moves = []
        legal_moves.append(self.BishopLegalMoves(start_pos))
        legal_moves.append(self.RookLegalMoves(start_pos))
        return helpers.ListMerger(legal_moves)

    def RookLegalMoves(self, start_pos):
        total_moves = [[], [], [], []]
        legal_moves = []
        x, y = start_pos
        possible_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        axis = 0
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    total_moves[axis].append((new_x, new_y))
                else:
                    break
            axis += 1
        for axis_list in total_moves:
            for move in axis_list:
                x, y = move
                if self.board[y][x] == "--":
                    legal_moves.append(move)
                else:
                    break

        return legal_moves

    def BishopLegalMoves(self, start_pos):
        total_moves = [[], [], [], []]
        legal_moves = []
        x, y = start_pos
        possible_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        axis = 0
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    total_moves[axis].append((new_x, new_y))
                else:
                    break
            axis += 1
        for axis_list in total_moves:
            for move in axis_list:
                x, y = move
                if self.board[y][x] == "--":
                    legal_moves.append(move)
                else:
                    break
        return legal_moves

    def PawnLegalMoves(self, start_pos):
        total_moves = []
        legal_moves = []
        color = helpers.Color(start_pos)
        x, y = start_pos
        if color == "b":
            if y == 1:
                total_moves.append((x, y + 1))
                total_moves.append((x, y + 2))
                helpers.ListMerger(total_moves)
            else:
                total_moves.append((x, y + 1))
            for move in total_moves:

                x, y = move
                if self.board[y][x] == "--":
                    legal_moves.append(move)
                else:
                    break
        if color == "w":
            if y == 6:
                total_moves.append((x, y - 1))
                total_moves.append((x, y - 2))
                helpers.ListMerger(total_moves)
            else:
                total_moves.append((x, y - 1))
            for move in total_moves:

                x, y = move
                if self.board[y][x] == "--":
                    legal_moves.append(move)
                else:
                    break
        return legal_moves

    def KnightLegalMoves(self, start_pos):
        total_moves = []
        legal_moves = []
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
        x, y = start_pos
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                total_moves.append((new_x, new_y))
        for move in total_moves:
            x, y = move
            if self.board[y][x] == "--":
                legal_moves.append(move)
            else:
                pass
        return legal_moves

    def KnightEat(self, start_pos):
        legal_eat = []
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
        x, y = start_pos
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[y][x] != "--":
                    legal_eat.append((new_x, new_y))
        return legal_eat

    def BishopEats(self, start_pos):
        legal_eats = []
        x, y = start_pos
        possible_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if self.board[y][x] != "--":
                        legal_eats.append((new_x, new_y))
        return legal_eats

    def RookEats(self, start_pos):
        legal_eats = []
        x, y = start_pos
        possible_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if self.board[y][x] != "--":
                        legal_eats.append((new_x, new_y))
        return legal_eats

    def PawnEats(self, start_pos):
        x, y = start_pos
        valid_eat_list = []
        color = helpers.Color(start_pos)
        x1 = x + 1
        x2 = x - 1
        if color == "w":
            new_y = y - 1
            valid_eat_list.append((x1, new_y))
            valid_eat_list.append((x2, new_y))
        else:
            new_y = y + 1
            valid_eat_list.append((x1, new_y))
            valid_eat_list.append((x2, new_y))
        return valid_eat_list

    def KingEats(self, start_pos):
        legal_eats = []
        possible_moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]
        x, y = start_pos
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if self.board[y][x] != "--":
                    legal_eats.append((new_x, new_y))
        return legal_eats

    def QueenEats(self, start_pos):
        legal_eats = []
        legal_eats.append(self.RookEats(start_pos))
        legal_eats.append(self.BishopEats(start_pos))
        return helpers.ListMerger(legal_eats)
