import pygame

W = 700
H = 500
screen = pygame.display.set_mode([W, H])
SQUARE_SIZE = 62
BOARD_SIZE = 8
running = True


def DrawBoard():
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


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    DrawBoard()
    pygame.display.update()
