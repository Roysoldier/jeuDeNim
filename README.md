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
## sqlitewrap : 
```python sqlitewrap
import sqlite3
class SqliteWrap:
    
    def __init__(self,nameDb=""):
        self.conn = sqlite3.connect(nameDb,check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self, tableName="", listFields = []):
        try:
            myCmd = f"CREATE TABLE {tableName}("
            for i in listFields:
                myCmd += f"{i[0]} {i[1]},"

            myCmd = myCmd[:-1] + ")"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e

    def add_row(self,tableName="",listValue=[]):
        try:
            myCmd = f"INSERT INTO {tableName}("
            myValues = " VALUES ("
            for i in listValue:
                myCmd += f"'{i[0]}',"
                if type(i[1]) == str:
                    myValues += f"'{i[1]}',"
                else:
                    myValues += f"{i[1]},"

            myCmd = myCmd[:-1] + ")" + myValues[:-1] + ")"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e
    
    def read_rows(self,tableName="", listFields=[]):
        try:
            myCmd = f"SELECT "
            for i in listFields:
                myCmd += i + ","

            myCmd = myCmd[:-1] + f" FROM {tableName}" 
            return self.cursor.execute(myCmd).fetchall(),None
        except Exception as e:
            return [],e
    
    def max_index(self,tableName="",field=""):
        try:
            myCmd = f"SELECT MAX({field}) FROM {tableName}"
            result =  self.cursor.execute(myCmd).fetchall()
            if result[0][0] == None:
                return [(0,)], None
            return result,None
        except Exception as e:
            return [],e
    
    def read_row(self,tableName="", condition=""):
        try:
            myCmd = f"SELECT * FROM {tableName} WHERE {condition}"
            result = self.cursor.execute(myCmd).fetchall()
            if len(result) == 0:
                return [], None
            if result[0][0] == None:
                return [], None
            return result,None
        except Exception as e:
            return [],e
    
    def update_row(self,tableName="",condition="",change=""):
        try:
            myCmd = f"UPDATE {tableName} SET {change} WHERE {condition}"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e

    def reset_table(self,tableName=""):
        try:
            self.cursor.execute(f"DELETE FROM {tableName}")
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e

    def delete_row(self,tableName="",condition=()):
        try:
            if type(condition[1]) == str:
                myCmd = f"DELETE FROM {tableName} WHERE {condition[0]} = '{condition[1]}'"
            else:
                myCmd = f"DELETE FROM {tableName} WHERE {condition[0]} = {condition[1]}"
            self.cursor.execute(myCmd)
            self.conn.commit()
            return 1,None
        except Exception as e:
            return 0,e
            
    def close_db(self):
        try:
            self.conn.commit()
            self.conn.close()
            return 1,None
        except Exception as e:
            return 0,e
       
```