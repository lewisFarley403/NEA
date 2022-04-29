import pygame
import os
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
# bus = pygame.image.load(os.getcwd()+r'\bus.jpg')

bus = pygame.image.load(
    os.getcwd()+r'\bus2.png')
while True:
    # main game loops
    screen.blit(bus, (0, 0))
    pygame.display.update()
pygame.quit()
quit()
