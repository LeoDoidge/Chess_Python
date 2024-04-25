import pygame
import sys
from settings import *
from ui import board
from utils import helpers
from game_logic import grid
from game_logic import game


pygame.init()
clock = pygame.time.Clock()
grid = grid.Grid()

pygame.display.set_caption("Chess Project")  

highlighted_pos = None  


# Function to draw the chessboard and piec


running = True
selected_piece = None
game_clock = 0
successful_moves = 0
square_clicked = None

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            square_clicked = helpers.square_pos(click_pos)

            if not selected_piece:  # If no piece was previously selected / highlighted
                if helpers.check_occup(square_clicked) and helpers.color(square_clicked) == (
                    "w" if game_clock % 2 == 0 else "b"
                ):
                    selected_piece = square_clicked
                else:
                    if helpers.type_piece(square_clicked) == "--":
                        pass
                    else:
                        print("It's not your turn!")
            else:  # A piece was previously selected / highlighed
                move_made = False
                if helpers.check_occup(square_clicked):
                    if helpers.color(square_clicked) != helpers.color(selected_piece):
                        move_made = game.eat_piece(selected_piece, square_clicked)
                else:
                    move_made = game.move_piece(
                        selected_piece, square_clicked, game_clock
                    )

                if move_made:
                    game_clock += 1
                    selected_piece = None
                else:
                    selected_piece = None
                    print("Invalid move!")
    screen.fill((0, 0, 0))
    board.draw_board(highlighted_pos, square_clicked)

    if selected_piece:  # highlighting a piece if there should be one
        selected_piece_color = helpers.color(selected_piece)
        board.highlight(selected_piece, selected_piece)

    pygame.display.update()
    clock.tick(10)


pygame.quit()
sys.exit()