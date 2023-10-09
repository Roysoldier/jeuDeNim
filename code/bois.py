import pygame
import time
class Bois():
    '''
    L'objet " Bois " permet de gerer directement tout ce qui se passe avec les allumettes les "bois" du jeux de nim . 
    '''
    iteration = 1
    def __init__(self,nbr,ecran):
        '''
        Cet Objet ne prend que le nombre de baton et les dimension de l'écran en argument il va initialiser les 
        variables utiles.
        '''
        self.base_nbr = nbr
        self.nbr = nbr
        self.ecran = ecran
        self.surface = pygame.display.set_mode(ecran)
        self.color = (66,34,22)
        self.color_delete = (0,0,0)
        Bois.iteration += 1

    def draw(self):
        '''
        Cette fonction va "dessiner" les baton sur lka page du jeu !
        '''
        distance = 30
        for i in range(self.nbr):
            pygame.draw.rect(self.surface, self.color, pygame.Rect(distance, 210, 30, 300),border_radius=20)
            distance += 52
        #for i in range(self.base_nbr - self.nbr):
            #pygame.draw.rect(self.surface, self.color_delete, pygame.Rect(distance, 210, 30, 300),border_radius=20)
            #distance += 52
    