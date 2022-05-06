import pygame
from compiler import RPN
import sys
import cv2
from simulation import CPU
from simulation import Simulation
import numpy as np


class Sim:
    def __init__(self):
        pygame.init()
        self.size = (700, 500)
        self.screen = pygame.display.set_mode(self.size)
        # self.sim = Simulation()

    def show(self):
        string_image = pygame.image.tostring(self.screen, 'RGB', True)

        temp_surf = pygame.image.fromstring(
            string_image, (self.size[0], self.size[1]), 'RGB')
        tmp_arr = pygame.surfarray.array3d(temp_surf)
        return tmp_arr

    def drawCPU(self):
        # draw main cpu body
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(0, self.size[-1]/2, self.size[0], self.size[-1]), 10)
        # draw the cpu's special registers registers

        # MAR
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(3*self.size[0]/4, self.size[-1]/2, self.size[0]/4, self.size[-1]/8), 10)
        # MDR
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
            0, self.size[-1]/2, 1*self.size[0]/4, self.size[-1]/8), 10)
        # ACC
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(0, 7*self.size[-1]/8, self.size[0]/4, 3*self.size[-1]/8), 10)
        # draw small register rect above acc, taking up and 8th of the width
        pygame.draw.rect(self.screen, (0, 0, 250),
                         pygame.Rect(0, 6*self.size[-1]/8, self.size[0]/8, 1*self.size[-1]/8), 10)
        # draw the ALU in the lower bottom right corner, taking up 1/4 of the screens width and 1/8 of its hight
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(3*self.size[0]/4, 7*self.size[-1]/8, self.size[0]/4, 3*self.size[-1]/8), 10)
        # draw the control unit from the acc and spans half the width of the screen until the alu and 1/8 of the screen hight
        pygame.draw.rect(self.screen, (0, 0, 0),
                         pygame.Rect(self.size[0]/4, 7*self.size[-1]/8, self.size[0]/2, self.size[-1]/8), 10)

        # PC between MAR,MDR
        pygame.draw.rect(self.screen, (250, 0, 0), pygame.Rect(
            1*self.size[0]/4, self.size[-1]/2, 1*self.size[0]/4, self.size[-1]/8), 10)
        # write text "pc" in the middle of the pc rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('pc', True, (0, 0, 0))
        self.screen.blit(
            text, (1*self.size[0]/4+self.size[0]/8, self.size[-1]/2+self.size[-1]/16))

        # write text "MAR" in the middle of the mar rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('MAR\ntest', True, (0, 0, 0))
        self.screen.blit(
            text, (3*self.size[0]/4+self.size[0]/8, self.size[-1]/2+self.size[-1]/16))

        # write text "MDR" in the middle of the mdr rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('MDR', True, (0, 0, 0))
        self.screen.blit(
            text, (0+self.size[0]/8, self.size[-1]/2+self.size[-1]/16))
        # write text "ACC" in the middle of the acc rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('ACC', True, (0, 0, 0))
        self.screen.blit(
            text, (0+self.size[0]/8, 7*self.size[-1]/8+self.size[-1]/16))
        # write text "ALU" in the middle of the alu rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('ALU', True, (0, 0, 0))
        self.screen.blit(
            text, (3*self.size[0]/4+self.size[0]/8, 7*self.size[-1]/8+self.size[-1]/16))
        # write cu in the middle of the control unit rect
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('CU', True, (0, 0, 0))
        self.screen.blit(
            text, (self.size[0]/4+self.size[0]/4, 7*self.size[-1]/8+self.size[-1]/16))  # write text "CU" in the middle of the control unit rect

        # write register in registers rect
        font = pygame.font.SysFont('Arial', 10)
        text = font.render('Registers', True, (0, 0, 0))
        self.screen.blit(
            text, (0+self.size[0]/16, 6*self.size[-1]/8+self.size[-1]/32))
        text = font.render('R1', True, (0, 0, 0))
        # draw line between center of PC and the center of MAR
        pygame.draw.line(self.screen, (0, 250, 0),
                         (2*self.size[0]/4, self.size[-1]/2+self.size[-1]/16), (3*self.size[0]/4, self.size[-1]/2+self.size[-1]/16), 10)
        # refresh screen

        pygame.display.flip()


s = Sim()
s.drawCPU()
frame = np.asarray(s.show())
# show frame in cv2
cv2.imshow('frame', frame)
# wait for keypress
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
while True:
    # set background to white
    s.screen.fill((255, 255, 255))
    s.drawCPU()
    # refresh screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
