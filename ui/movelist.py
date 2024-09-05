import pygame

W = 200
H = 500
Gray = 150, 150, 150


def Window():
    RUNNING = True
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Move List")
    screen.fill(Gray)
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        screen.fill(Gray)
        pygame.display.update()
    pygame.display.quit()
