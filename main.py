# Importing necessary libraries and modules
import pygame
import sys
import game_logic
from globals import *

# Initializing pygame
pygame.init()
clock = pygame.time.Clock()

# Creating the game grid
grid = game_logic.Grid()
pygame.display.set_caption("Chess Project")  # Setting window title

highlighted_pos = None  # Initializing highlighted position variable


# Function to draw the chessboard and pieces
def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            x = col * square_size
            y = row * square_size
            if (row + col) % 2 == 0:
                pygame.draw.rect(
                    screen, (255, 255, 255), (x, y, square_size, square_size)
                )
            else:
                pygame.draw.rect(
                    screen, (150, 150, 150), (x, y, square_size, square_size)
                )

    for i in range(8):
        for j in range(8):
            grid.drawPiece(i, j, screen)

    if highlighted_pos is not None:
        grid.highlight(highlighted_pos, square_clicked)


running = True
selected_piece = None
game_clock = 0
successful_moves = 0

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            square_clicked = grid.square_pos(click_pos)

            if not selected_piece:  # If no piece was previously selected / highlighted
                if grid.check_occup(click_pos) and grid.color(square_clicked) == (
                    "w" if game_clock % 2 == 0 else "b"
                ):
                    selected_piece = square_clicked
                else:
                    print("It's not your turn!")
            else:  # A piece was previously selected / highlighed
                move_made = False
                if grid.check_occup(click_pos):
                    if grid.color(square_clicked) != grid.color(selected_piece):
                        move_made = grid.eat_piece(selected_piece, square_clicked)
                else:
                    move_made = grid.move_piece(
                        selected_piece, square_clicked, game_clock
                    )

                if move_made:
                    game_clock += 1
                    selected_piece = None
                else:
                    selected_piece = None
                    print("Invalid move!")

    screen.fill((0, 0, 0))
    draw_board()

    if selected_piece:  # highlighting a piece if there should be one
        selected_piece_color = grid.color(selected_piece)
        grid.highlight(selected_piece, selected_piece)

    pygame.display.update()
    clock.tick(10)


pygame.quit()
sys.exit()
