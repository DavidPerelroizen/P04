from Models.classtournoi import Tournoi
from Models.constants import time_controllers


def tournoicreation():
    """This function initializes the creation of a tournament"""
    tournoi_name = input('Enter the tournament name : ')
    tournoi_place = input('Enter the tournament location : ')
    tournoi_date = ''
    while len(tournoi_date) != 10:
        try:
            tournoi_date = input('Enter the tournament date (JJ/MM/AAAA) : ')
        except ValueError:
            print("Please enter a valid date")
    tournoi_description = input('Enter the tournament description : ')
    tournoi_time_controller = ''
    while tournoi_time_controller not in time_controllers:
        tournoi_time_controller = input('Enter a time controller (blitz, coup rapide, bullet) : ')

    tournoi = Tournoi(tournoi_name, tournoi_place, tournoi_date, [], tournoi_description, tournoi_time_controller)

    return tournoi





