import pygame
from ui import board
from utils import helpers


class Pieces:
    def __init__(self):
        self.board = board.Grid.grid

    def PawnRank(self, square_pos):
        return square_pos[1]

    def BlackPawnValidMoves(self, start_pos):
        ValidMoveList = []
        x, y = start_pos
        if y == 1:
            new_y1 = y + 1
            new_y2 = y + 2
            ValidMoveList.append((x, new_y1))
            ValidMoveList.append((x, new_y2))
        else:
            new_y1 = y + 1
            ValidMoveList.append((x, new_y1))
        return ValidMoveList

    def WhitePawnValidMoves(self, start_pos):
        ValidMoveList = []
        x, y = start_pos
        if y == 6:
            new_y1 = y - 1
            new_y2 = y - 2
            ValidMoveList.append((x, new_y1))
            ValidMoveList.append((x, new_y2))
        else:
            new_y1 = y - 1
            ValidMoveList.append((x, new_y1))

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
                ValidMovesList.append((new_x, new_y))
        return ValidMovesList

    def BishopValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = [[], [], [], []]
        possible_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        axis = 0
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList[axis].append((new_x, new_y))
                else:
                    break
            axis += 1
        return ValidMovesList

    def RookValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = [[], [], [], []]
        possible_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        axis = 0
        for move in possible_moves:
            for i in range(1, 8):
                new_x = x + move[0] * i
                new_y = y + move[1] * i
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    ValidMovesList[axis].append((new_x, new_y))
                else:
                    break
            axis += 1

        return ValidMovesList

    def KingValidMoves(self, start_pos):
        x, y = start_pos
        ValidMovesList = []
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
        for move in possible_moves:
            new_x = x + move[0]
            new_y = y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                ValidMovesList.append((new_x, new_y))
        return ValidMovesList

    def Pawn_remove_blocked_moves(self, start_pos):
        color = helpers.color(start_pos)
        if color == "w":
            valid_move_list = self.WhitePawnValidMoves(start_pos)
        else:
            valid_move_list = self.BlackPawnValidMoves(start_pos)
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
                pass

        return updated_move_list

    def Bishop_remove_blocked_moves(self, start_pos):
        valid_move_list = self.BishopValidMoves(start_pos)
        updated_move_list = []
        for axis_list in valid_move_list:
            for move in axis_list:
                x, y = move
                if self.board[y][x] == "--":
                    updated_move_list.append(move)
                else:
                    break

        return updated_move_list

    def Rook_remove_blocked_moves(self, start_pos):
        valid_move_list = self.RookValidMoves(start_pos)
        updated_move_list = []
        for axis_list in valid_move_list:
            for move in axis_list:
                x, y = move
                if self.board[y][x] == "--":
                    updated_move_list.append(move)
                else:
                    break
        return updated_move_list

    def Queen_remove_blocked_moves(self, start_pos):
        updated_move_list = []
        updated_move_list.append(self.Rook_remove_blocked_moves(start_pos))
        updated_move_list.append(self.Bishop_remove_blocked_moves(start_pos))
        return helpers.merger(updated_move_list)

    def King_remove_blocked_moves(self, start_pos):
        valid_move_list = self.KingValidMoves(start_pos)
        updated_move_list = []
        for move in valid_move_list:
            x, y = move
            if self.board[y][x] == "--":
                updated_move_list.append(move)
            else:
                pass

        return updated_move_list

    def PawnEat(self, start_pos):
        x, y = start_pos
        valid_eat_list = []
        color = helpers.color(start_pos)
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
