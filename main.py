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
            # make white background
            screen.fill((255, 255, 255))
            # draw a red pixel at the click position
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 1, 1))
            # update display
            pygame.display.update()
            # print coords
            print(f"x={x}, y={y}")
