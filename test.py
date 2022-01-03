from Models.classtournoi import Tournoi
from Models.constants import time_controllers

liste_joueurs = ['J1', "J2", "J3"]

tournoi1 = Tournoi('Tournoi du siècle', 'Dijon', '01/01/2022', ["des", "tours"], time_controllers[2], [])

for i in liste_joueurs:
    tournoi1.addplayer(i)
    tournoi1.displayplayerslist()

