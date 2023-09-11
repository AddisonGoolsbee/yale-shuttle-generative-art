import pygame
import sys

# initialization stuff
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
font = pygame.font.SysFont(None, 25)

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
            text = font.render(f"x={x}, y={y}", True, (255,0,255))
            screen.blit(text, (x + 5, y))
            # update display
            pygame.display.update()
            # print coords to chat
            print(f"x={x}, y={y}")
            
