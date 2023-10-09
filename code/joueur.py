import pygame

class Joueur:
    '''
    Cet Objet joueur a pour but de repertorier les joueur afin de pouvoir les identifier en tant qu'entité dans le jeu.
    '''
    nombre = 0
    def __init__(self,status='joueur'):
        '''
        L'objet prend en argument le statut du joueur pour pouvoir localiser si il s'agit d'une ia ou non ensuite on
        l'applique.
        '''
        if status == "joueur":
            Joueur.nombre += 1 
            self.name = f'Joueur {Joueur.nombre}'
        elif status == "ia":
            self.name = 'Robot 1'

    def check_nbr_joueur(self):
        '''
        Fonction qui vérifie juste le nombre de joueur
        '''
        print(f"La partie comporte {Joueur.nombre} de joueur" )
    def check_player(self):
        '''
        Fonction qui vérifie juste le joueur
        '''
        print(self.name)