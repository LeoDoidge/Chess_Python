'''
This module handles all global variables
'''

import pygame

H = 500
W = 500
BOARD_SIZE = 8
SQUARE_SIZE = W // BOARD_SIZE
backround_color = 255, 255, 255
screen = pygame.display.set_mode([W, H])
RUNNING = True
HIGHLIGHTED_POS = None
SELECTED_PIECE = None
SQUARE_CLICKED = None
GAME_CLOCK = 0
SUCCESSFUL_MOVES = 0
