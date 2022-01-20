from Models.classtournoi import Tournoi
from Models.constants import time_controllers_dict
import datetime


def tournoicreation():
    """This function initializes the creation of a tournament"""

    tournoi_name = input('Enter the tournament name : ').upper()
    tournoi_place = input('Enter the tournament location : ')

    #  Define the date with checks and controls
    tournoi_date = datetime.date(1900, 1, 1)
    while tournoi_date < datetime.date.today():
        print('The tournament date must not be in the past')
        tournoi_day = ''
        while tournoi_day not in range(1, 32):
            try:
                tournoi_day = int(input('Enter the day: '))
            except ValueError:
                print('Please enter a valid day (integer from 1 to 31)')
        tournoi_month = ''
        while tournoi_month not in range(1, 13):
            try:
                tournoi_month = int(input('Enter the month (integer from 1 to 12): '))
            except ValueError:
                print('Please enter a valid month (integer from 1 to 12)')
        tournoi_year = ''
        while tournoi_year not in range(1900, 9999):
            try:
                tournoi_year = int(input('Enter the year (four digits integer): '))
            except ValueError:
                print('Please enter a valid year')
        tournoi_date = datetime.date(tournoi_year, tournoi_month, tournoi_day)

    tournoi_description = input('Enter the tournament description : ')

    # Defines the time controller with input controls
    tournoi_time_controller = ''
    while tournoi_time_controller == '':
        try:
            tournoi_time_controller = time_controllers_dict[int(
                input('Enter a time controller (blitz--> 1, coup rapide --> 2, bullet --> 3) : '))]
        except KeyError:
            print('Please enter a valid key')
        except ValueError:
            print('Please enter a valid key')
    print(f'Time controller selected: {tournoi_time_controller}')

    # Tournament instantiation as a Tournoi object
    tournoi = Tournoi(tournoi_name, tournoi_place, tournoi_date, [], tournoi_description, tournoi_time_controller)

    return tournoi
