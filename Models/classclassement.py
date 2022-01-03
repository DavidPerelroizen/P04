from Models.classjoueur import Joueur

class Classement:

    def __init__(self, players_ranking):
        self.players_ranking = players_ranking

    def initialranking(self, players_list):
        for Joueur in players_list:

