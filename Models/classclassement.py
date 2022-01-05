import operator


class Classement:

    def __init__(self, players_ranking):
        self.players_ranking = players_ranking

    def ranking(self, players_list):
        """This function sorts the players list according to their score and then according to their rank"""
        self.players_ranking = sorted(players_list, key=operator.itemgetter(6, 5))
        return self.players_ranking



