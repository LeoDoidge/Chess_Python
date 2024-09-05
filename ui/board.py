from os import path
import pygame
import tkinter as tk
from settings import *


class Grid:
    grid = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
    ]

    def __init__(self):
        pass


def DrawPiece(x, y, game):
    if 0 <= x < 8 and 0 <= y < 8:  # Check if x and y are within the valid range
        name = Grid.grid[y][x]
        if name == "--":
            pass
        else:
            image = pygame.image.load(path.join("assets", "images", name + ".png"))
            imagerect = image.get_rect()
            imagerect.left = x * H / 8
            imagerect.top = y * H / 8
            game.blit(image, imagerect)


def Highlight(start_pos, end_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    if (
        Grid.grid[start_y][start_x] != "--"
        and Grid.grid[start_y][start_x][0] == Grid.grid[end_y][end_x][0]
    ):
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (
                (start_x * SQUARE_SIZE),
                (start_y * SQUARE_SIZE),
                SQUARE_SIZE,
                SQUARE_SIZE,
            ),
            3,
        )
    elif Grid.grid[start_y][start_x][0] != Grid.grid[end_y][end_x][0]:
        return None


def DisplayTimer(pointer, last_click):
    seconds_left = [time_left[0].seconds, time_left[1].seconds]
    seconds_left[pointer] -= (datetime.datetime.now() - last_click).seconds
    time_text_p1 = font.render(
        str(seconds_left[1] // 60) + ":" + str(seconds_left[1] % 60).zfill(2),
        True,
        (0, 0, 0),
    )
    time_text_p2 = font.render(
        str(seconds_left[0] // 60) + ":" + str(seconds_left[0] % 60).zfill(2),
        True,
        (255, 255, 255),
    )
    screen.blit(time_text_p1, ((W - 500) // 2 + 470, H // 2 - 20))
    screen.blit(time_text_p2, ((W - 500) // 2 + 470, H // 2 + 20))


def TotalMovesDisplay(tt_moves):
    tt_moves = font.render(str(tt_moves), True, (0, 0, 0))
    screen.blit(tt_moves, ((W - 500) // 2 + 500, 50))


def MoveButton():
    text = font.render(str("Move list"), True, (0, 0, 0))
    screen.blit(text, ((W - 500) // 2 - 50 + 500, 100))


def DrawBoard(highlighted_pos, square_clicked):
    for row in range(8):
        for col in range(8):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            if (row + col) % 2 == 0:
                pygame.draw.rect(
                    screen, (255, 255, 255), (x, y, SQUARE_SIZE, SQUARE_SIZE)
                )
            else:
                pygame.draw.rect(
                    screen, (150, 150, 150), (x, y, SQUARE_SIZE, SQUARE_SIZE)
                )
    # Deviding line in between info bar and board
    pygame.draw.rect(screen, (0, 0, 0), (496, 0, 3, H))

    for i in range(8):
        for j in range(8):
            DrawPiece(i, j, screen)

    if highlighted_pos is not None:
        Highlight(highlighted_pos, square_clicked)


def SecondaryWindow():
    window = tk.Tk()
    window.title("Move list")

    for x in range(20):
        for y in range(2):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            frame.grid(row=x, column=y)  # line 13
            label = tk.Label(master=frame, text="hello world")
            label.pack()

    window.mainloop()
