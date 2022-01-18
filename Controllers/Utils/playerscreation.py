from Controllers.playersmanager import gettheplayers


def playerscreation(tournoi):
    """This function consolidates the code helping to create players"""
    players_number = 0
    while players_number % 2 != 0 or players_number == 0:
        try:
            players_number = int(input('How many players do you want to add? (even numbers only): '))
        except ValueError:
            print('Please enter an even number of players')
    tournoi.players_list = gettheplayers(tournoi.name, players_number)
    return tournoi
