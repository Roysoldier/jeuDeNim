import pygame

class Joueur:
    nombre = 0
    def __init__(self,status='joueur'):
        if status == "joueur":
            Joueur.nombre += 1 
            self.name = f'Joueur {Joueur.nombre}'
        elif status == "ia":
            self.name = 'Robot 1'

    def check_nbr_joueur(self):
        print(f"La partie comporte {Joueur.nombre} de joueur" )
    def check_player(self):
        print(self.name)