# Jeu de Nim projet 1
### Noan et jeremy

- Source du cahier de bord : https://docs.google.com/document/d/1j6VZEGTlrcGJBkthKDbn2dna8XKGhRP_9V6aO6ADo_4/edit?usp=sharing
# Algorithme jeu de Nim :
- Choisir le nombre d'allumette (de base 20) ainsi que le nombre de joueur (de base 2)
- Tant que la partie n'est pas terminer on va faire jouer les 2 joueur 1 à 1 
- Le joueur donner une valeur entre 1 et 3 il recommence tant qua la valeur qu'il a donner n'est pas bonne
- Une fois que la valeur donner est valide on va retirer cette valeur au nombre d'allumettes total restant
- Si il ne reste plus qu'une seule allumette alors la partie est finie et le joueur qui vient de jouer à gagner 
- Sinon on passe simplement au joueur suivant 


# Particularité du jeu de Nim
- Le jeu admet Obligatoirement un vainceur 
- Le joueur doit Absolument prendre à la fois comprise entre 1 et 3 et > au nombre d'allumettes
- La partie doit s'arrêter dès que l'un des joueurs fais tomber le nombre d'allumettes à 1

# Code simple du jeu de Nim 
```python jeu de nim
baton=20
joueurs=['j1','j2']
running=False
while running==False:
    for i in joueurs:
        status=False
        while status==False:
            print('|'*baton)
            try:
                delete=int(input(f' au tour de {i} de donner un nombre entre 1 et 3 '))
            
                if delete>3 or delete<1 or delete>baton:
                    print('la valeur donnée n est pas valide')
                else:
                    status=True
                    baton-=delete
            except Exception as e:
                print(f"Une erreur c'est produite: {e}")
        
        if baton==1:
            print(f'{i} a gagné la partie!')
            running=True
            break
```

# Information complémentaire sur le code 
## Librairie utilisé : 
- Pygame
- Time
- Math
- Random
## Libraire personelle importée dans le répertoire : './lib' (code en fin de page)
- myLogger (loggeur personnel)
- sqlitewrap (librairie pour sqlitewrap version lite de mySql)

## Ressource utilisé :
- PowerPoint
- Google 
- Wikipédia
- Visual studio code 
- GitHub/Git
## Source des images du diaporama : 
- https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.fredtechnocollege.org%2Falgorithme-du-jeu-de-nim%2F&psig=AOvVaw3pUIjciuEBxzYFllu3DTQh&ust=1695806967226000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNi4vLH7x4EDFQAAAAAdAAAAABAD

- https://www.google.com/url?sa=i&url=https%3A%2F%2Fo.fortboyard.tv%2Fdefis%2Fbatonnets.php&psig=AOvVaw0Xjy2M7bhVm73YXeMQF6IL&ust=1695804212637000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPjVwKL7x4EDFQAAAAAdAAAAABAD

- https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/800px-Java_programming_language_logo.svg.png

- https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/640px-JavaScript-logo.png

- https://seeklogo.com/images/C/c-sharp-c-logo-02F17714BA-seeklogo.com.png

- https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/ISO_C%2B%2B_Logo.svg/1822px-ISO_C%2B%2B_Logo.svg.png

- https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png

## Sources et ressoures graphique du jeu :

# Détails des Objets :
## Bois : 

    L'objet " Bois " permet de gerer directement tout ce qui se passe avec les allumettes les "bois" du jeux de nim . 
- Cet Objet rend en entrée le nbr de bois a utiliser ici nous n'en prendrons que 20 ainsi que les dimension de l'écran
- Fonction draw qui ne prend que self en argument va simplement " dessiner " les bois restant sur la fenêtre de jeu

### Code :
``` python Object bois
import pygame
import time
class Bois():
    iteration = 1
    def __init__(self,nbr,ecran):
        self.base_nbr = nbr
        self.nbr = nbr
        self.ecran = ecran
        self.surface = pygame.display.set_mode(ecran)
        self.color = (66,34,22)
        self.color_delete = (0,0,0)
        Bois.iteration += 1

    def draw(self):
        distance = 30
        for i in range(self.nbr):
            pygame.draw.rect(self.surface, self.color, pygame.Rect(distance, 210, 30, 300),border_radius=20)
            distance += 52

```

## Bouton :
    L'objet Bouton permet de crée les bouton et de récupèrer toutes leur coordonée afin de les localiser et d'en faire des entité pur capable d'interaction dans le code il permet aussi de les afficher simplement.
- Cet objet prend en entrée l'écran e ces paramètre afin de pouvoir le modifier directement
- Fonction active_bouton qui prend en entrée le nom du bouton afin de savoir quel bouton activer 'afficher' sur l'écran
### Code :
``` python bouton object
import pygame
import math
class Bouton():
    def __init__(self,screen):
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


```
## Joueur :
    Cet Objet joueur a pour but de repertorier les joueur afin de pouvoir les identifier en tant qu'entité dans le jeu.
- Cet Objet prend simplement le statut du joueur (de base un joueur sinon une ia)
- Fonction check_nbr_joueur prend simplement self en argument et sert juste a afficher le nombre de joueur présent.
- Fonction check_player prend simplement self en argument et set simplement a récuperer le nom du joueur.
### Code : 
``` python joueur Object
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
```
## Game : 
    Cet Objet Permet de gerer toutes instances de la game  

### Code :
``` python game code 
import pygame
import bois
import joueur
import random

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
```
# Code des librairie personnelle :
## myLogger :
```python mylogger
import logging
from logging.handlers import RotatingFileHandler
import sys

class MyLogger:
    def __init__(self,path="./logs/messages.log",console=False):
        self.logger = None

        if console:
            self.logger = logging.getLogger('mylogger')
            self.logger.setLevel(logging.DEBUG)
            sh = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
            sh.setFormatter(formatter)
            self.logger.addHandler(sh)
        else:
            self.logger = logging.getLogger('mylogger')
            self.logger.setLevel(logging.DEBUG)
            fh = RotatingFileHandler(path, maxBytes=10000000, backupCount=10, encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s > %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            
    def log(self,message="",severity="DEBUG"):
        match severity:
            case "DEBUG":
                self.logger.debug(message)
            case "INFO":
                self.logger.info(message)
            case "WARN":
                self.logger.warn(message)
            case "ERROR":
                self.logger.error(message)
            case "CRITICAL":
                self.logger.critical(message)
            case _:
                self.logger.debug(message)

```
