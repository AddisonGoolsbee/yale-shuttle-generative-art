import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # need to figure out how to draw a red pixel upon click
            #pygame.draw.rect(screen, (255, 0, 0), (x, y, 1, 1))
            print(f"x={x}, y={y}")
