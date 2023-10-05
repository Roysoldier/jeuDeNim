import math
import pygame
from pygame.locals import *
import time
import game

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

button1 = pygame.image.load('./data/bouton1.png')
button1 = pygame.transform.scale(button1, (100,100))
button1_rect = button1.get_rect()
button1_rect.x = screen.get_width() -200
button1_rect.y = math.ceil(screen.get_height()/1.3)

button2 = pygame.image.load('./data/bouton2.png')
button2 = pygame.transform.scale(button2, (100,100))
button2_rect = button2.get_rect()
button2_rect.x = screen.get_width()/2 -50
button2_rect.y = math.ceil(screen.get_height()/1.3)

button3 = pygame.image.load('./data/bouton3.png')
button3 = pygame.transform.scale(button3, (100,100))
button3_rect = button3.get_rect()
button3_rect.x = 100
button3_rect.y = math.ceil(screen.get_height()/1.3)

rejouer_bouton = pygame.image.load('./data/replay.png')
rejouer_bouton = pygame.transform.scale(rejouer_bouton, (300,120))
rejouer_bouton_rect = rejouer_bouton.get_rect()
rejouer_bouton_rect.x = 50
rejouer_bouton_rect.y = math.ceil(screen.get_height() - 150)

quit_bouton = pygame.image.load('./data/quit.png')
quit_bouton = pygame.transform.scale(quit_bouton, (300,120))
quit_bouton_rect = quit_bouton.get_rect()
quit_bouton_rect.x = 730
quit_bouton_rect.y = math.ceil(screen.get_height() - 150)

lancement_bouton_1 = pygame.image.load('./data/one_player.png')
lancement_bouton_1 = pygame.transform.scale(lancement_bouton_1, (300,120))
lancement_bouton_1_rect = lancement_bouton_1.get_rect()
lancement_bouton_1_rect.x = 50
lancement_bouton_1_rect.y = math.ceil(screen.get_height() - 150)

lancement_bouton_2 = pygame.image.load('./data/two_player.png')
lancement_bouton_2 = pygame.transform.scale(lancement_bouton_2, (300,120))
lancement_bouton_2_rect = lancement_bouton_2.get_rect()
lancement_bouton_2_rect.x = 730
lancement_bouton_2_rect.y = math.ceil(screen.get_height() - 150)


pygame.init()
font = pygame.font.Font(None,100)

game = game.Game()


#boucle de statut du jeu
gagnant = None
while running:
    
    if not game.on_game and gagnant == None:
        backround = pygame.image.load('./data/start.png')
        screen.blit(backround,(0,0))
        screen.blit(img,(284,154))
        screen.blit(lancement_bouton_1, lancement_bouton_1_rect)
        screen.blit(lancement_bouton_2, lancement_bouton_2_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            #Vérification de l'évenement de fermeture de la fenètre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                Debug.log("Arrêt du jeu !", "INFO")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if lancement_bouton_1_rect.collidepoint(event.pos):
                    game.start_game(1,20,displaySize)
                elif lancement_bouton_2_rect.collidepoint(event.pos):
                    game.start_game(2,20,displaySize)

    elif not game.on_game and gagnant != None:
        backround = pygame.image.load('./data/fin.png')
        text = font.render(f"{gagnant} a gagner !",30, (255,255,255))
        screen.blit(backround,(0,0))
        screen.blit(text, (210, 75))
        screen.blit(rejouer_bouton, rejouer_bouton_rect)
        screen.blit(quit_bouton, quit_bouton_rect)
        pygame.display.flip()
        pygame.init()
        for event in pygame.event.get():
            #Vérification de l'évenement de fermeture de la fenètre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                Debug.log("Arrêt du jeu !", "INFO")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rejouer_bouton_rect.collidepoint(event.pos):
                    game.reset_game()
                    gagnant = None
                elif quit_bouton_rect.collidepoint(event.pos):
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
                    screen.blit(button1, button1_rect)
                if game.bois.nbr > 2:
                    screen.blit(button2, button2_rect)
                if game.bois.nbr > 3:
                    screen.blit(button3, button3_rect)
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
                            if button1_rect.collidepoint(event.pos) and game.historique[-1] != joueur.name:
                                if game.bois.nbr > 1:
                                    game.bois.nbr -= 1
                                    status = True
                                    game.historique.append(joueur.name)
                            elif button2_rect.collidepoint(event.pos) and  game.historique[-1] != joueur.name:
                                if game.bois.nbr > 2:
                                    game.bois.nbr -= 2
                                    status = True
                                    game.historique.append(joueur.name)
                            elif button3_rect.collidepoint(event.pos) and  game.historique[-1] != joueur.name:
                                if game.bois.nbr > 3:
                                    game.bois.nbr -= 3
                                    status = True
                                    game.historique.append(joueur.name)
                
            elif joueur.name == "Robot 1":
                print(joueur.name)
                screen.blit(backround,(0,0))
                game.bois.draw()
                text = font.render(f"{joueur.name}",30, (255,255,255))
                screen.blit(text, (410, 75))
                pygame.display.flip()
                time.sleep(1)
                game.bois.nbr -= game.jeux_ia()
                game.historique.append(joueur.name)
                print(game.historique)
                    
            if game.check_status_game():
                gagnant = joueur.name
                game.on_game = False
                break
