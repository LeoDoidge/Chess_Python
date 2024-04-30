import pygame
from ui import board
from utils import helpers


class Pieces:
    def __init__(self):
        self.board = board.Grid.grid

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
