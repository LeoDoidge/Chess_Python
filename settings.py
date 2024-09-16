"""
This module handles all global variables
"""

import datetime
import pygame


pygame.font.init()

H = 500
W = 700
BOARD_SIZE = 8
SQUARE_SIZE = 62
backround_color = 150, 150, 150
screen = pygame.display.set_mode([W, H])
RUNNING = True
HIGHLIGHTED_POS = None
SELECTED_PIECE = None
SQUARE_CLICKED = None
GAME_CLOCK = 0
SUCCESSFUL_MOVES = 0
font = pygame.font.Font(None, 36)
time_left = [datetime.timedelta(minutes=15), datetime.timedelta(minutes=15)]
NMB_MOVES_TOTAL = 0
MOVE_ORIGIN = []
MOVE_DESTINATION = []
MOVE_ORIGIN_TYPE = []
EAT_ORIGIN = []
EAT_DESTINATION = []
EAT_ORIGIN_TYPE = []
EAT_DESTINATION_TYPE = []
