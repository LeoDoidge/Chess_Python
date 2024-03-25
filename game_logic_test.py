import unittest
import game_logic
from pprint import pprint

class TestMoves(unittest.TestCase):

    def test_valid_move(self):
        my_grid = game_logic.Grid()
        my_grid.move_piece((6,3), (4,3))
        pprint(my_grid.grid)
        self.assertEqual(my_grid.grid, [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "wp", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
                          ])

    def test_valid_move_result(self):
        my_grid = game_logic.Grid()
        my_grid.move_piece((6,3), (4,3))
        pprint(my_grid.grid)
        self.assertEqual(my_grid.grid, [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "wp", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "--", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
                          ])

if __name__ == '__main__':
    unittest.main()