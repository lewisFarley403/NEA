import pygame
from compiler import RPN
import sys
import cv2
from simulation import CPU
from simulation import Simulation


class Sim:
    def __init__(self):
        pygame.init()
        self.size = (700, 500)
        self.screen = pygame.display.set_mode(self.size)
        #self.sim = Simulation()

    def show(self):
        pass

    def drawCPU(self):
        # draw main cpu body
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(0, self.size[-1]/2, self.size[0], self.size[-1]), 10)
        # draw the cpu's special registers registers

        # MAR
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(3*self.size[0]/4, self.size[-1]/2, self.size[0]/4, self.size[-1]/4), 10)
        # MDR
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
            0, self.size[-1]/2, 1*self.size[0]/4, self.size[-1]/4), 10)

        # PC between MAR,MDR
        pygame.draw.rect(self.screen, (250, 0, 0), pygame.Rect(
            1*self.size[0]/4, self.size[-1]/2, 1*self.size[0]/4, self.size[-1]/4), 10)
        # write text "pc" in the middle of the pc rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('pc', True, (0, 0, 0))
        self.screen.blit(
            text, (1*self.size[0]/4+self.size[0]/8, self.size[-1]/2+self.size[-1]/8))

        # write text "MAR" in the middle of the mar rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('MAR', True, (0, 0, 0))
        self.screen.blit(
            text, (3*self.size[0]/4+self.size[0]/8, self.size[-1]/2+self.size[-1]/8))

        # write text "MDR" in the middle of the mdr rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('MDR', True, (0, 0, 0))
        self.screen.blit(
            text, (0+self.size[0]/8, self.size[-1]/2+self.size[-1]/8))

        # draw ACC

        # draw line between center of PC and the center of MAR
        pygame.draw.line(self.screen, (0, 250, 0),
                         (2*self.size[0]/4, self.size[-1]/2+self.size[-1]/8), (3*self.size[0]/4, self.size[-1]/2+self.size[-1]/8), 10)        # refresh screen

        pygame.display.flip()


s = Sim()
while True:
    # set background to white
    s.screen.fill((255, 255, 255))

    frame = s.drawCPU()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
