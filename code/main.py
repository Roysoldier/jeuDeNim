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
Debug.log("Tout est prêt pour le lancement !", "INFO")
while running:
    #Verification du statut actuel de la game ici nous cherchons a lancer une partie
    if not game.on_game and gagnant == None:
        #initialisation de tout les élement graphique
        backround = pygame.image.load('./data/start.png')
        screen.blit(backround,(0,0))
        screen.blit(img,(284,154))
        bouton.active_bouton('Start_1')
        bouton.active_bouton('Start_2')
        pygame.display.flip()
        #Boucle d'évenement qui va permettre de réciuperer les différents élements de type évenement qui s'applique a pygame
        for event in pygame.event.get():
            #Vérification de l'évenement de fermeture de la fenètre
            if event.type == pygame.QUIT:
                Debug.log("La fermerture du jeu est demander ...", "INFO")
                running = False
                pygame.quit()
                Debug.log("Arrêt du jeu !", "INFO")
            #évenement cliquer sur la souris
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton.lancement_bouton_1_rect.collidepoint(event.pos):
                    Debug.log("Lancement du jeu pour 1 joueur ...", "INFO")
                    game.start_game(1,20,displaySize)
                elif bouton.lancement_bouton_2_rect.collidepoint(event.pos):
                    Debug.log("Lancement du jeu pour 2 joueurs ...", "INFO")
                    game.start_game(2,20,displaySize)
    # Page de fin de partie qui va annoncer le gagnant et demander si l'on veux rejouer ou quitter  !
    elif not game.on_game and gagnant != None:
        #initialisation des élemement graphiques
        backround = pygame.image.load('./data/fin.png')
        text = font.render(f"{gagnant} a gagner !",30, (255,255,255))
        screen.blit(backround,(0,0))
        screen.blit(text, (210, 75))
        bouton.active_bouton('Replay')
        bouton.active_bouton('Quit')
        pygame.display.flip()
        pygame.init()
        #Boucle d'évenement qui va permettre de réciuperer les différents élements de type évenement qui s'applique a pygame
        for event in pygame.event.get():
            #Vérification de l'évenement de fermeture de la fenètre
            if event.type == pygame.QUIT:
                Debug.log("La fermerture du jeu est demander ...", "INFO")
                running = False
                pygame.quit()
                Debug.log("Arrêt du jeu !", "INFO")
            #évenement cliquer sur la souris
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bouton.rejouer_bouton_rect.collidepoint(event.pos):
                    Debug.log("Le bouton rejouer à été presser !", "INFO")
                    game.reset_game()
                    gagnant = None
                elif bouton.quit_bouton_rect.collidepoint(event.pos):
                    Debug.log("Le bouton quitter à été presser !", "INFO")
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
                    Debug.log("Le bouton 1 est actif !", "INFO")
                    bouton.active_bouton('B1')
                if game.bois.nbr > 2:
                    Debug.log("Le bouton 2 est actif !", "INFO")
                    bouton.active_bouton('B2')
                if game.bois.nbr > 3:
                    Debug.log("Le bouton 3 est actif !", "INFO")
                    bouton.active_bouton('B3')
                pygame.display.flip()
                time.sleep(0.1)
                #Gérer les évenement   
                status = False
                while not status and game.on_game:
                    pygame.init()
                    #Boucle d'évenement qui va permettre de réciuperer les différents élements de type évenement qui s'applique a pygame
                    for event in pygame.event.get():
                        #Vérification de l'évenement de fermeture de la fenètre
                        if event.type == pygame.QUIT:
                            Debug.log("La fermerture du jeu est demander ...", "INFO")
                            running = False
                            pygame.quit()
                            Debug.log("Arrêt du jeu !", "INFO")
                        #évenement cliquer sur la souris
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if bouton.button1_rect.collidepoint(event.pos) and game.historique[-1] != joueur.name:
                                Debug.log("Le bouton 1 à été presser !", "INFO")
                                if game.bois.nbr > 1:
                                    Debug.log(f"{joueur.name} à jouer 1", "INFO")
                                    game.bois.nbr -= 1
                                    status = True
                                    game.historique.append(joueur.name)
                            elif bouton.button2_rect.collidepoint(event.pos) and  game.historique[-1] != joueur.name:
                                Debug.log("Le bouton 2 à été presser !", "INFO")
                                if game.bois.nbr > 2:
                                    Debug.log(f"{joueur.name} à jouer 2", "INFO")
                                    game.bois.nbr -= 2
                                    status = True
                                    game.historique.append(joueur.name)
                            elif bouton.button3_rect.collidepoint(event.pos) and  game.historique[-1] != joueur.name:
                                Debug.log("Le bouton 3 à été presser !", "INFO")
                                if game.bois.nbr > 3:
                                    Debug.log(f"{joueur.name} à jouer 3", "INFO")
                                    game.bois.nbr -= 3
                                    status = True
                                    game.historique.append(joueur.name)
            # On fais jouer l'ia si c'est à son tour !
            elif joueur.name == "Robot 1":
                screen.blit(backround,(0,0))
                game.bois.draw()
                text = font.render(f"{joueur.name}",30, (255,255,255))
                screen.blit(text, (410, 75))
                pygame.display.flip()
                time.sleep(1)
                Debug.log(f"{joueur.name} à jouer ", "INFO")
                game.bois.nbr -= game.jeux_ia()
                game.historique.append(joueur.name)
            # On vérifie que la game est encore en cour et on rétablie son statut      
            if game.check_status_game():
                Debug.log(f"{joueur.name} à gagner !", "INFO")
                gagnant = joueur.name
                game.on_game = False
                break
