from Models.classjoueur import Joueur
from Models.classtournoi import Tournoi
from Controllers.dbplayers import players_table, updateplayersrank, deserializeplayersdicos
from Controllers.dbtournoi import tournois_table, serializetournoi, serializetherounds, serializetheplayerslist,\
    deserializerounds
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
        joueur.updaterank(updated_rank)  # Updates the rank of a player instance in the players database
        updated_players_list.append([joueur.player_index, joueur.last_name, joueur.first_name, joueur.birth_date,
                                     joueur.gender, joueur.rank, joueur.score])

    tournoi.players_list = updated_players_list  # Updates the tournament instance with the new rankings


def specificplayerrankingupdate():
    """
    This function will enable the user to update the rank of a specific player in the database
    :return: none
    """
    global tournoi_deserialized
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

    # Player's rank update in the players database
    updateplayersrank(player_index_for_update, updated_rank)

    # Look for the tournament linked with the player's index
    tournoi_to_update_name = player_index_for_update[:-9]
    tournoi_search = Query()
    tournoi_dict = tournois_table.search(tournoi_search.name == tournoi_to_update_name)

    # The loop below allows to work directly on the only dictionary contained in the tournoi_dict list
    tournoi_deserialized = ''
    for element in tournoi_dict:
        tournoi_deserialized = Tournoi(element['name'], element['place'], element['date_list'], element['rounds_list'],
                                       element['description'], element['time_controller'],
                                       deserializeplayersdicos(element['players_list']),
                                       element['rounds_number'])

    # In the tournoi deserialized instance, update the right player's rank
    updated_players_list = tournoi_deserialized.players_list
    for player in updated_players_list:
        if player[0] == player_index_for_update:
            player[5] = updated_rank
    tournoi_deserialized.players_list = updated_players_list

    # Deserialize the rounds and updated the deserialized tournament with rounds list with serializable data
    rounds_deserialized = deserializerounds(tournoi_deserialized)
    tournoi_deserialized.rounds_list = rounds_deserialized

    # Serialize the rounds list and the players list of the deserialized tournament
    serializetherounds(tournoi_deserialized)
    serializetheplayerslist(tournoi_deserialized)

    # Remove the original instance of the tournoi
    tournois_table.remove(tournoi_search.name == tournoi_to_update_name)

    # Serialize the updated tournoi
    serializetournoi(tournoi_deserialized)

    print('Rank updated')
