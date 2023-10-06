import math
import pygame
from pygame.locals import *
import time
import game
import bouton

from lib import myLogger,sqlitewrap


#Définition des différente variable utile au bon fonctionnement des paramètre de la partie
clock = pygame.time.Clock
FPS = 60
displaySize = (1080,720)
Debug = myLogger.MyLogger()

#Géneration de la fenêtre pygame
pygame.display.set_caption("Jeu De nim")
screen = pygame.display.set_mode(displaySize)


img = pygame.image.load('./data/conf.png')

#Etat de la partie 
running = True
Debug.log("Lancement du jeu !", "INFO")


pygame.init()
font = pygame.font.Font(None,100)

game = game.Game()
bouton = bouton.Bouton(screen)

#boucle de statut du jeu
gagnant = None
while running:
    
    if not game.on_game and gagnant == None:
        backround = pygame.image.load('./data/start.png')
        screen.blit(backround,(0,0))
        screen.blit(img,(284,154))
        bouton.active_bouton('Start_1')
        bouton.active_bouton('Start_2')
        pygame.display.flip()
        for event in pygame.event.get():
            #Vérification de l'évenement de fermeture de la fenètre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                Debug.log("Arrêt du jeu !", "INFO")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton.lancement_bouton_1_rect.collidepoint(event.pos):
                    game.start_game(1,20,displaySize)
                elif bouton.lancement_bouton_2_rect.collidepoint(event.pos):
                    game.start_game(2,20,displaySize)

    elif not game.on_game and gagnant != None:
        backround = pygame.image.load('./data/fin.png')
        text = font.render(f"{gagnant} a gagner !",30, (255,255,255))
        screen.blit(backround,(0,0))
        screen.blit(text, (210, 75))
        bouton.active_bouton('Replay')
        bouton.active_bouton('Quit')
        pygame.display.flip()
        pygame.init()
        for event in pygame.event.get():
            #Vérification de l'évenement de fermeture de la fenètre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                Debug.log("Arrêt du jeu !", "INFO")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton.rejouer_bouton_rect.collidepoint(event.pos):
                    game.reset_game()
                    gagnant = None
                elif bouton.quit_bouton_rect.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    Debug.log("Arrêt du jeu !", "INFO")

    elif game.on_game:
        backround = pygame.image.load('./data/fond.png')
        for joueur in game.joueurs:
            
            if joueur.name != 'Robot 1':
                screen.blit(backround,(0,0))
                game.bois.draw()
                text = font.render(f"{joueur.name}",30, (255,255,255))
                screen.blit(text, (410, 75))
                #Appliquer le fond d'écran du jeu  
                if game.bois.nbr > 1:
                    bouton.active_bouton('B1')
                if game.bois.nbr > 2:
                    bouton.active_bouton('B2')
                if game.bois.nbr > 3:
                    bouton.active_bouton('B3')
                pygame.display.flip()
                time.sleep(0.1)
                #Gérer les évenement   
                status = False
                while not status and game.on_game:
                    pygame.init()
                    for event in pygame.event.get():
                        #Vérification de l'évenement de fermeture de la fenètre
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            Debug.log("Arrêt du jeu !", "INFO")
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if bouton.button1_rect.collidepoint(event.pos) and game.historique[-1] != joueur.name:
                                if game.bois.nbr > 1:
                                    game.bois.nbr -= 1
                                    status = True
                                    game.historique.append(joueur.name)
                            elif bouton.button2_rect.collidepoint(event.pos) and  game.historique[-1] != joueur.name:
                                if game.bois.nbr > 2:
                                    game.bois.nbr -= 2
                                    status = True
                                    game.historique.append(joueur.name)
                            elif bouton.button3_rect.collidepoint(event.pos) and  game.historique[-1] != joueur.name:
                                if game.bois.nbr > 3:
                                    game.bois.nbr -= 3
                                    status = True
                                    game.historique.append(joueur.name)
                
            elif joueur.name == "Robot 1":
                screen.blit(backround,(0,0))
                game.bois.draw()
                text = font.render(f"{joueur.name}",30, (255,255,255))
                screen.blit(text, (410, 75))
                pygame.display.flip()
                time.sleep(1)
                game.bois.nbr -= game.jeux_ia()
                game.historique.append(joueur.name)
                    
            if game.check_status_game():
                gagnant = joueur.name
                game.on_game = False
                break
