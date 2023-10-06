import pygame
import time
class Bois():
    iteration = 1
    def __init__(self,nbr,ecran):
        self.base_nbr = nbr
        self.nbr = nbr
        self.ecran = ecran
        self.surface = pygame.display.set_mode(ecran)
        self.color = (66,34,22)
        self.color_delete = (0,0,0)
        Bois.iteration += 1

    def draw(self):
        distance = 30
        for i in range(self.nbr):
            pygame.draw.rect(self.surface, self.color, pygame.Rect(distance, 210, 30, 300),border_radius=20)
            distance += 52
        #for i in range(self.base_nbr - self.nbr):
            #pygame.draw.rect(self.surface, self.color_delete, pygame.Rect(distance, 210, 30, 300),border_radius=20)
            #distance += 52
    