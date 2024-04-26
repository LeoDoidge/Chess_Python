import pygame 

H = 500
W = 500
board_size = 8
square_size = W // board_size
backround_color = 255, 255, 255
screen = pygame.display.set_mode([W, H])
running = True
highlighted_pos = None
selected_piece = None
square_clicked = None
game_clock = 0
successful_moves = 0
