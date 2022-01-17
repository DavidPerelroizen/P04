
class Classement:
    """This object will help refreshing the players ranking"""

    def ranking(self, players_list):
        """This function sorts the players list according to their score and then according to their rank"""
        players_ranking = sorted(players_list, key=lambda x:  (-x[6], x[5]))
        return players_ranking
