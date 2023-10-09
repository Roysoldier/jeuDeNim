import pygame
import bois
import joueur
import random

#class Game va gèrer toute les instance et évenement en jeu
class Game():
    '''
    Cet Objet Permet de gerer toutes instances de la game  
    afin de gerer son bon déroulement dans les règles 
    imposer
    '''
    Game_itteration = 0
    def __init__(self):
        '''
        L'objet ne prend aucun argument spécial on va initialiser ici 
        le statut de la game augmenter le nombre d'iteration afin de n'avoir qu'une seule game
        crée une liste qui contiendras les objet joueur puis un historique qui a pour but de réguler la partie
        '''
        print(joueur.Joueur.nombre)
        self.on_game = False
        Game.Game_itteration += 1
        self.joueurs = []
        self.historique = [None]
    
    def start_game(self,nbr_joueur,nbr_bois=20,ecran=(500,500)):
        '''
        Fonction start_game qui prend en argument le nombre de joueurs de bois et les dimension de la fenêtre, cette fonction
        permet de lancer les initialization de la partie !
        '''
        self.bois = bois.Bois(nbr_bois,ecran)
        self.nbr_player = nbr_joueur
        self.on_game = True
        Game.create_player(self,nbr_joueur)

    def create_player(self,nbr_player):
        '''
        Fonction create_player qui prend uniquement le nombre de joueur en argument il va simplement crée les objets des 
        joureurs et les ajouter a self.joueurs
        '''
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
        '''
        Fonction nbr_player qui ne prend rien de spécial en argument ,
        cette fonction renvoie simplement le nombre de joueurs
        '''
        print(f'Il y as {joueur.Joueur.nombre} ')

    def check_delete_nbr(self,nbr_to_delete):
        '''
        Fonction check_delete_nbr qui prend le nombre de baton a enlever et va vérifier la validité de la valeur et retourner 
        de façon booléene si la condition est vérifier ou non
        '''
        if nbr_to_delete < 1 or nbr_to_delete > 3 or nbr_to_delete >= self.bois.nbr:
            return 0 
        else:
            return 1
    def check_status_game(self):
        '''
        Fonction check_status_game qui ne prend aucun argument spécial et qui ba simplement vérifier si 
        la partie doit continuer ou non et renvoyer un booléen
        '''
        if self.bois.nbr == 1:
            return 1
        else:
            return 0
    def jeux_ia(self):
        ''' 
        Fonction jeux_ia ne prend rien en argument et fais simplement jouer l'ia
        '''
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
        '''
        Fonction reset_game qui ne prend rien en argument et qui a pour but de simplement renitialiser les différenrts paramètre 
        de la partie.
        '''
        self.joueurs = []
        joueur.Joueur.nombre = 0
        self.historique = [None]