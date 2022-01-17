from Controllers.dbplayers import updateplayersrank


class Joueur:
    """This class aims at modeling a Player as an object"""

    def __init__(self, player_index, last_name, first_name, birth_date, gender, rank, score=0):
        self.player_index = player_index
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score

    def updaterank(self, new_rank):
        """This function enables the update of a player's rank anytime"""
        self.rank = new_rank
        # The script below will update the player's rank in the players_table
        updateplayersrank(self.player_index, new_rank)

    def getplayerinfos(self):
        """This function returns the player infos as a list"""
        return [self.player_index, self.last_name, self.first_name, self.birth_date, self.gender, self.rank, self.score]

    def addscore(self, match_result):
        """This function updates the score attribute of the player instance depending on a match result"""
        for item in match_result:
            if item[0] == self.player_index:
                self.score += item[1]
