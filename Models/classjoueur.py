class Joueur:

    def __init__(self, last_name, first_name, birth_date, gender, rank):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank

    def updaterank(self, new_rank):
        """This function unables the update of a player's rank anytime"""
        self.rank = new_rank