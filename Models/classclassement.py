import operator


class Classement:

    def __init__(self, players_ranking):
        self.players_ranking = players_ranking

    def initialranking(self, players_list):
        self.players_ranking = sorted(players_list, key=operator.itemgetter(5))
        return self.players_ranking



