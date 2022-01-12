from Models.classjoueur import Joueur
from Models.constants import gender_dict


def gettheplayers(players_number):

    players_list = []

    for i in range(1, players_number+1):
        print("")

        player_index = "Player " + str(i)
        print('Prepare to fill in information for ', player_index)
        player_last_name = input('Enter the player last name : ').upper()
        player_first_name = input('Enter the player first name : ').lower()
        player_birth_date = ''
        while len(player_birth_date) != 10:
            try:
                player_birth_date = input('Enter the player birth date (JJ/MM/AAAA) : ')
            except ValueError:
                print("Please enter a valid birth date")
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
