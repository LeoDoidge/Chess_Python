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


running = True  # Flag to control the game loop
selected_piece = None  # Variable to store selected piece

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop when window is closed

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            square_clicked = grid.square_pos(click_pos)

            if not selected_piece:  # If no piece is selected
                if grid.check_occup(click_pos):
                    selected_piece = square_clicked
            else:  # If a piece is already selected
                if grid.check_occup(click_pos):
                    if grid.color(square_clicked) != grid.color(selected_piece):
                        grid.eat_piece(selected_piece, square_clicked)
                        selected_piece = None
                    else:
                        selected_piece = None
                else:
                    grid.move_piece(selected_piece, square_clicked)
                    selected_piece = None

    screen.fill((0, 0, 0))  # Clearing the screen
    draw_board()  # Drawing the chessboard and pieces

    # Highlight the selected piece if it exists
    if selected_piece:
        selected_piece_color = grid.color(selected_piece)
        grid.highlight(selected_piece, selected_piece)

    pygame.display.update()  # Updating the display
    clock.tick(10)  # Limiting the frame rate

pygame.quit()  # Quitting pygame
sys.exit()  # Exiting the script
