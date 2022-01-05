from Models.classjoueur import Joueur
from Models.constants import gender_list

def gettheplayers(players_number):

    players_list = []

    for i in range(1, players_number+1):
        """player_index, last_name, first_name, birth_date, gender, rank"""
        player_index = "Player" + str(i)
        print('Prepare to fill in information for ', player_index)
        player_last_name = input('Enter the player last name : ')
        player_first_name = input('Enter the player first name : ')
        player_birth_date = input('Enter the player birth date (JJ/MM/AAAA) : ')
        player_gender = ''
        while player_gender not in gender_list:
            player_gender = input(f'Enter the player gender {gender_list} : ')
        player_rank = 0
        while player_rank not in range(1, players_number + 1, 1):
            try:
                player_rank = int(input(f'Enter the player rank (only integers from 1 to {players_number}) : '))
            except ValueError:
                print('Integers only from 1 to ', players_number)

        player = Joueur(
            player_index, player_last_name, player_first_name, player_birth_date, player_gender, player_rank
        )

        players_list.append(player)

    return players_list


