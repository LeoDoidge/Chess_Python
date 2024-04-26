import pygame
import sys
from settings import *
from ui import board
from utils import helpers
from game_logic import grid as grid_module, piece_movement

pygame.display.set_caption("Chess Project")
pygame.init()

clock = pygame.time.Clock()
grid = grid_module.Grid()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            square_clicked = helpers.square_pos(click_pos)

            if not selected_piece:
                if helpers.check_occup(square_clicked) and helpers.color(
                    square_clicked
                ) == ("w" if game_clock % 2 == 0 else "b"):
                    selected_piece = square_clicked
                elif helpers.type_piece(square_clicked) == "--":
                    pass
                else:
                    print("It's not your turn!")
            else:
                move_made = False
                if helpers.check_occup(square_clicked):
                    if helpers.color(square_clicked) != helpers.color(selected_piece):
                        move_made = piece_movement.eat_piece(
                            selected_piece, square_clicked
                        )
                else:
                    move_made = piece_movement.move_piece(
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

    if selected_piece:
        selected_piece_color = helpers.color(selected_piece)
        board.highlight(selected_piece, selected_piece)

    pygame.display.update()
    clock.tick(10)


pygame.quit()
sys.exit()
