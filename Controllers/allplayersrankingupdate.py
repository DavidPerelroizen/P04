from Models.classjoueur import Joueur
from Controllers.dbplayers import players_table, updateplayersrank
from tinydb import Query


def allplayersrankingupdate(tournoi):
    forbidden_ranks = []
    updated_rank = 0
    joueur = ''
    updated_players_list = []

    for player in tournoi.players_list:
        while updated_rank not in range(1, len(tournoi.players_list) + 1) or updated_rank in forbidden_ranks:
            try:
                joueur = Joueur(player[0], player[1], player[2], player[3], player[4], player[5], player[6])
                updated_rank = int(
                    input(
                        f'Enter the new rank for {joueur.player_index} '
                        f'(Integer between 1 and {len(tournoi.players_list)}): ')
                )
                if updated_rank in forbidden_ranks:
                    print(
                        f'Rank n° {updated_rank} was already assigned to another player. Please enter another one.'
                    )
            except ValueError:
                print(f'Integers only from 1 to {len(tournoi.players_list)}')

        forbidden_ranks.append(updated_rank)
        joueur.updaterank(updated_rank)
        updated_players_list.append([joueur.player_index, joueur.last_name, joueur.first_name, joueur.birth_date,
                                     joueur.gender, joueur.rank, joueur.score])

    tournoi.players_list = updated_players_list


def specificplayerrankingupdate():
    """
    This function will enable the user to update the rank of a specific player in the database
    :return: none
    """
    player_index_for_update = input('Type the player index you are looking for: ')
    player_search = Query()
    search_result = players_table.search(player_search.player_index == player_index_for_update)
    print(f'{player_index_for_update} current rank is ', {search_result[0]['rank']})

    updated_rank = 0
    while updated_rank not in range(1, 999):
        try:
            updated_rank = int(input('Enter the new rank: '))
        except ValueError:
            print('Please input only integers')

    updateplayersrank(player_index_for_update, updated_rank)
    print('Rank updated')
