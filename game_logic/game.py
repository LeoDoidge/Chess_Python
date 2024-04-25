import pygame 
from utils import helpers
import grid
import pieces


class piece_movement:
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
