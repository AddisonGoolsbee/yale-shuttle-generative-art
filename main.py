import pygame
import sys

# initialization stuff
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # make black background
            screen.fill((0, 0, 0))
            # draw a green pixel at the click position
            pygame.draw.rect(screen, (0, 255, 0), (x, y, 1, 1))
            # update display
            pygame.display.update()
            # print coords
            print(f"x={x}, y={y}")
