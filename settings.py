"""
This module handles all global variables
"""

import pygame
import datetime

pygame.font.init()

H = 500
W = 700
BOARD_SIZE = 8
SQUARE_SIZE = 62
backround_color = 255, 255, 255
screen = pygame.display.set_mode([W, H])
RUNNING = True
HIGHLIGHTED_POS = None
SELECTED_PIECE = None
SQUARE_CLICKED = None
GAME_CLOCK = 0
SUCCESSFUL_MOVES = 0
font = pygame.font.Font(None, 36)  
time_left = [datetime.timedelta(minutes=15), datetime.timedelta(minutes=15)]
player = 0
