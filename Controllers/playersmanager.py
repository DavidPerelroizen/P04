from Models.classjoueur import Joueur
from Models.constants import gender_dict
import datetime


def gettheplayers(players_number):

    players_list = []

    for i in range(1, players_number+1):
        """For each player the code will request information that will help to instantiate the players objects"""
        print("")

        player_index = "Player " + str(i)
        print('Prepare to fill in information for ', player_index)
        player_last_name = input('Enter the player last name : ').upper()
        player_first_name = input('Enter the player first name : ').lower()
        print(f'Prepare to fill information {player_index} birth date: ')
        player_birth_day = ''
        while player_birth_day not in range(1, 32):
            try:
                player_birth_day = int(input('Enter the day: '))
            except ValueError:
                print('Please enter a valid day (integer from 1 to 31)')
        player_birth_month = ''
        while player_birth_month not in range(1, 13):
            try:
                player_birth_month = int(input('Enter the month (integer from 1 to 12): '))
            except ValueError:
                print('Please enter a valid month (integer from 1 to 12)')
        player_birth_year = ''
        while player_birth_year not in range(1900, 9999):
            try:
                player_birth_year = int(input('Enter the year (four digits integer): '))
            except ValueError:
                print('Please enter a valid year')
        player_birth_date = datetime.date(player_birth_year, player_birth_month, player_birth_day)
        player_gender = ''
        while player_gender == '':
            try:
                player_gender = gender_dict[int(input(
                    f'Enter the player gender (Man --> press 1, Woman--> press 2) : ')
                )]
            except KeyError:
                print('Please enter a valid gender')
        player_rank = 0
        while player_rank not in range(1, players_number + 1, 1):
            try:
                player_rank = int(input(f'Enter the player rank (only integers from 1 to {players_number}) : '))
            except ValueError:
                print('Integers only from 1 to ', players_number)
        player_score = 0

        print("")

        player = [
            player_index, player_last_name, player_first_name, player_birth_date, player_gender, player_rank,
            player_score
        ]

        players_list.append(player)

    return players_list
