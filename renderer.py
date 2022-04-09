import pygame


class Renderer:
    def __init__(self, x, y, width, height, src):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(src)

    def show(self, screen):
        s
