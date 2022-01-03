class Tournoi:

    def __init__(
            self, name, place, date_list, rounds_list, description, time_controller, players_list=[],
            rounds_number=4
    ):
        self.name = name
        self.place = place
        self.date_list = date_list
        self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description
        self.time_controller = time_controller
        self.rounds_number = rounds_number

    def addplayer(self, player):
        """This function adds a player to the players list"""
        self.players_list.append(player)

    def displayplayerslist(self):
        """This function displays the players list of the tournament"""
        print(self.players_list)
