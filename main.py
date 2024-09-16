"""
Main module to run the app
"""

import sys
import pygame
from settings import *
from ui import board
from utils import helpers
from game_logic import piece_movement


pygame.display.set_caption("Chess Project")
last_click = datetime.datetime.now()


clock = pygame.time.Clock()
start_time = datetime.datetime.now()
converter = helpers.Converter()

while RUNNING:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = False

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

                        if helpers.Color(SQUARE_CLICKED) != helpers.Color(
                            SELECTED_PIECE
                        ):
                            MOVE_MADE = piece_movement.EatPiece(
                                SELECTED_PIECE, SQUARE_CLICKED
                            )
                            if MOVE_MADE:
                                EAT_ORIGIN.append(converter.PyToChess(SELECTED_PIECE))
                                EAT_DESTINATION.append(
                                    converter.PyToChess(SQUARE_CLICKED)
                                )

                    else:
                        MOVE_MADE = piece_movement.MovePiece(
                            SELECTED_PIECE, SQUARE_CLICKED, GAME_CLOCK
                        )
                        if MOVE_MADE:
                            MOVE_ORIGIN.append(converter.PyToChess(SELECTED_PIECE))
                            MOVE_DESTINATION.append(converter.PyToChess(SQUARE_CLICKED))

                    if MOVE_MADE:
                        if helpers.Color(SQUARE_CLICKED) == "b":
                            NMB_MOVES_TOTAL += 1

                        time_left[GAME_CLOCK] -= datetime.datetime.now() - last_click

                        if GAME_CLOCK == 0:
                            GAME_CLOCK = 1

                        elif GAME_CLOCK == 1:
                            GAME_CLOCK = 0

                        SELECTED_PIECE = None
                        last_click = datetime.datetime.now()

                    else:
                        SELECTED_PIECE = None
                        print("Invalid move!")

            elif 550 < click_pos[0] < 650 and 95 < click_pos[1] < 125:
                board.SecondaryWindow(NMB_MOVES_TOTAL)
            else:
                print("Out of bounds!")

    screen.fill((backround_color))

    board.DrawBoard(None, SQUARE_CLICKED)
    board.DisplayTimer(GAME_CLOCK, last_click)
    board.TotalMovesDisplay(NMB_MOVES_TOTAL)
    board.MoveButton()

    if SELECTED_PIECE:
        board.Highlight(SELECTED_PIECE, SELECTED_PIECE)

    pygame.display.update()
    clock.tick(60)


sys.exit()
