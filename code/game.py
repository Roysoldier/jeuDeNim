import pygame
import bois
import joueur
import random

#class Game va gèrer toute les instance et évenement en jeu
class Game():
    Game_itteration = 0
    def __init__(self):
        print(joueur.Joueur.nombre)
        self.on_game = False
        Game.Game_itteration += 1
        self.joueurs = []
        self.historique = [None]
    
    def start_game(self,nbr_joueur,nbr_bois=20,ecran=(500,500)):
        self.bois = bois.Bois(nbr_bois,ecran)
        self.nbr_player = nbr_joueur
        self.on_game = True
        Game.create_player(self,nbr_joueur)

    def create_player(self,nbr_player):
        if nbr_player > 2:
            return 0
        elif nbr_player == 1:
            self.joueurs.append(joueur.Joueur())
            self.joueurs.append(joueur.Joueur('ia'))
        else :
            for i in range(1,nbr_player+1):
                self.joueurs.append(joueur.Joueur())
            print(self.joueurs)
    
    def nbr_players(self):
        print(f'Il y as {joueur.Joueur.nombre} ')

    def check_delete_nbr(self,nbr_to_delete):
        if nbr_to_delete < 1 or nbr_to_delete > 3 or nbr_to_delete >= self.bois.nbr:
            return 0 
        else:
            return 1
    def check_status_game(self):
        if self.bois.nbr == 1:
            return 1
        else:
            return 0
    def jeux_ia(self):
        nbr_a_jouer = 0
        if self.bois.nbr == 3: 
            nbr_a_jouer = 2
        elif self.bois.nbr == 2: 
            nbr_a_jouer = 1
        elif self.bois.nbr == 4: 
            nbr_a_jouer = random.randint(1,2)
        else :
            nbr_a_jouer = random.randint(1,3)
        return nbr_a_jouer
    def reset_game(self):
        self.joueurs = []
        joueur.Joueur.nombre = 0
        self.historique = [None]