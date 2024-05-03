import sys
import pygame
from settings import *
from ui import board
from utils import helpers
from game_logic import piece_movement
from countdown import countdown


pygame.display.set_caption("Chess Project")
last_click = datetime.datetime.now()


clock = pygame.time.Clock()
start_time = datetime.datetime.now()

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                time_left[player] -= datetime.datetime.now() - last_click
                if player == 0:
                    player += 1
                elif player == 1:
                    player -= 1
                
                last_click = datetime.datetime.now()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            SQUARE_CLICKED = helpers.SquarePos(click_pos)
            if SQUARE_CLICKED is not None:
                if not SELECTED_PIECE:
                    if helpers.CheckOccup(SQUARE_CLICKED) and helpers.Color(
                        SQUARE_CLICKED
                    ) == ("w" if GAME_CLOCK % 2 == 0 else "b"):
                        SELECTED_PIECE = SQUARE_CLICKED
                    elif helpers.TypePiece(SQUARE_CLICKED) == "--":
                        pass
                    else:
                        print("It's not your turn!")
                else:
                    MOVE_MADE = False
                    if helpers.CheckOccup(SQUARE_CLICKED):
                        if helpers.Color(SQUARE_CLICKED) != helpers.Color(SELECTED_PIECE):
                            MOVE_MADE = piece_movement.EatPiece(
                                SELECTED_PIECE, SQUARE_CLICKED
                            )
                    else:
                        MOVE_MADE = piece_movement.MovePiece(
                            SELECTED_PIECE, SQUARE_CLICKED, GAME_CLOCK
                        )

                    if MOVE_MADE:
                        GAME_CLOCK += 1
                        SELECTED_PIECE = None
                    else:
                        SELECTED_PIECE = None
                        print("Invalid move!")
            else:
                print("Out of bounds!")
    screen.fill((backround_color))
    board.DrawBoard(None, SQUARE_CLICKED)
    board.display_timer(start_time, player, last_click)
    if SELECTED_PIECE:
        selected_piece_color = helpers.Color(SELECTED_PIECE)
        board.Highlight(SELECTED_PIECE, SELECTED_PIECE)

    pygame.display.update()
    clock.tick(60)


sys.exit()
