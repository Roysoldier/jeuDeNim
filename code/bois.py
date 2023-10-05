import pygame

class Bois():
    iteration = 1
    def __init__(self,nbr,ecran):
        self.nbr = nbr
        self.ecran = ecran
        self.surface = pygame.display.set_mode(ecran)
        self.color = (66,34,22)
        Bois.iteration += 1

    def draw(self):
        distance = 30
        for i in range(self.nbr):
            pygame.draw.rect(self.surface, self.color, pygame.Rect(distance, 210, 30, 300),border_radius=20)
            distance += 52
    
    def game(self):
        self.nbr -= 1