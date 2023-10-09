import pygame
import math
class Bouton():
    '''
    L'objet Bouton permet de crée les bouton et de récupèrer toutes leur coordonée afin de les localiser
    et d'en faire des entité pur capable d'interaction dans le code il permet aussi de les afficher simplement.
    '''
    def __init__(self,screen,):
        '''
        L'objet ne prend que l'objet screen en argument on va initialiser tout les bouton dans le init
        '''
        self.screen = screen
        self.button1 = pygame.image.load('./data/bouton1.png')
        self.button1 = pygame.transform.scale(self.button1, (100,100))
        self.button1_rect = self.button1.get_rect()
        self.button1_rect.x = screen.get_width() -200
        self.button1_rect.y = math.ceil(screen.get_height()/1.3)

        self.button2 = pygame.image.load('./data/bouton2.png')
        self.button2 = pygame.transform.scale(self.button2, (100,100))
        self.button2_rect = self.button2.get_rect()
        self.button2_rect.x = screen.get_width()/2 -50
        self.button2_rect.y = math.ceil(screen.get_height()/1.3)

        self.button3 = pygame.image.load('./data/bouton3.png')
        self.button3 = pygame.transform.scale(self.button3, (100,100))
        self.button3_rect = self.button3.get_rect()
        self.button3_rect.x = 100
        self.button3_rect.y = math.ceil(screen.get_height()/1.3)

        self.rejouer_bouton = pygame.image.load('./data/replay.png')
        self.rejouer_bouton = pygame.transform.scale(self.rejouer_bouton, (300,120))
        self.rejouer_bouton_rect = self.rejouer_bouton.get_rect()
        self.rejouer_bouton_rect.x = 50
        self.rejouer_bouton_rect.y = math.ceil(screen.get_height() - 150)

        self.quit_bouton = pygame.image.load('./data/quit.png')
        self.quit_bouton = pygame.transform.scale(self.quit_bouton, (300,120))
        self.quit_bouton_rect = self.quit_bouton.get_rect()
        self.quit_bouton_rect.x = 730
        self.quit_bouton_rect.y = math.ceil(screen.get_height() - 150)

        self.lancement_bouton_1 = pygame.image.load('./data/one_player.png')
        self.lancement_bouton_1 = pygame.transform.scale(self.lancement_bouton_1, (300,120))
        self.lancement_bouton_1_rect = self.lancement_bouton_1.get_rect()
        self.lancement_bouton_1_rect.x = 50
        self.lancement_bouton_1_rect.y = math.ceil(screen.get_height() - 150)

        self.lancement_bouton_2 = pygame.image.load('./data/two_player.png')
        self.lancement_bouton_2 = pygame.transform.scale(self.lancement_bouton_2, (300,120))
        self.lancement_bouton_2_rect = self.lancement_bouton_2.get_rect()
        self.lancement_bouton_2_rect.x = 730
        self.lancement_bouton_2_rect.y = math.ceil(screen.get_height() - 150)

    def active_bouton(self,bouton):
        '''
        Cette Fonction qui prend en paramètre le nom du bouton va permetre d'activer les boutons dans le jeu
        '''
        if bouton == 'Start_1':
            self.screen.blit(self.lancement_bouton_1,self.lancement_bouton_1_rect)
        elif bouton == 'Start_2':
            self.screen.blit(self.lancement_bouton_2, self.lancement_bouton_2_rect)
        elif bouton == 'Replay':
            self.screen.blit(self.rejouer_bouton, self.rejouer_bouton_rect)
        elif bouton == 'Quit':
            self.screen.blit(self.quit_bouton, self.quit_bouton_rect)
        elif bouton == 'B1':
            self.screen.blit(self.button1, self.button1_rect)
        elif bouton == 'B2':
            self.screen.blit(self.button2, self.button2_rect)
        elif bouton == 'B3':
            self.screen.blit(self.button3, self.button3_rect)

