from Models.classtournoi import Tournoi
from Models.constants import time_controllers
from Models.classjoueur import Joueur
from Models.classmatch import Match
from Models.classtour import Tour
from Models.classclassement import Classement

players_list = [
    ['Joueur1', 'self.last_name1', 'self.first_name1', '01/01/2000', 'M', 4],
    ['Joueur2', 'self.last_name2', 'self.first_name2', '01/01/2001', 'M', 2],
    ['Joueur3', 'self.last_name3', 'self.first_name3', '01/01/2002', 'M', 1],
    ['Joueur4', 'self.last_name4', 'self.first_name4', '01/01/2003', 'M', 3]
]

classement1 = Classement([])
print(classement1.initialranking(players_list))










