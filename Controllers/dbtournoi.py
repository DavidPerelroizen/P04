import json
from tinydb import TinyDB, Query
from Models.classtournoi import Tournoi
from Controllers.dbplayers import deserializeplayersdicos
from Models.classtour import Tour


db = TinyDB('db.json')
tournois_table = db.table('tournois')


def serializetherounds(tournoi_for_serializing):
    """This function helps serializing a rounds list for a specific tournament"""
    rounds_list_for_serialization = []
    for round_instance in tournoi_for_serializing.rounds_list:
        round_dict = {'round_name': round_instance.round_name,
                      # Use json.dumps to avoid bugs when serializing dates
                      'date_time_begin': json.dumps(round_instance.date_time_begin, default=str),
                      # Use json.dumps to avoid bugs when serializing dates
                      'date_time_finish': json.dumps(round_instance.date_time_finish, default=str),
                      'matches_list': round_instance.matches_list
                      }
        rounds_list_for_serialization.append(round_dict)

    return rounds_list_for_serialization


def serializetheplayerslist(tournoi_for_serializing):
    """This function helps serializing a players list for a specific tournament"""
    players_list_for_serialization = []
    for player_instance in tournoi_for_serializing.players_list:
        player_dict = {'player_index': player_instance[0],
                       'last_name': player_instance[1],
                       'first_name': player_instance[2],
                       # Use json.dumps to avoid bugs when serializing dates
                       'birth_date': json.dumps(player_instance[3], default=str),
                       'gender': player_instance[4],
                       'rank': player_instance[5],
                       'score': player_instance[6]}
        players_list_for_serialization.append(player_dict)

    return players_list_for_serialization


def serializetournoi(tournoi_for_serializing):
    """
    This function aims at serializing a tournoi (class = Tournoi()) and insert is in the tiny DB
    :param tournoi_for_serializing:
    :return:
    """
    # Step 1: serialize the rounds
    rounds_list_for_serialization = serializetherounds(tournoi_for_serializing)

    # Step 2: serialize the players list
    players_list_for_serialization = serializetheplayerslist(tournoi_for_serializing)

    # Instantiate the tournament dictionary
    tournoi_dict = {
        'name': tournoi_for_serializing.name, 'place': tournoi_for_serializing.place,
        # Use json.dumps to avoid bugs when serializing dates
        'date_list': json.dumps(tournoi_for_serializing.date_list, default=str),
        'rounds_list': rounds_list_for_serialization,
        'description': tournoi_for_serializing.description,
        'time_controller': tournoi_for_serializing.time_controller,
        'players_list': players_list_for_serialization,
        'rounds_number': tournoi_for_serializing.rounds_number
    }

    tournois_table.insert(tournoi_dict)


def deserializetournoi():
    """This function deserializes a specific tournoi provided by user"""
    tournoi_dict = []

    while tournoi_dict == []:
        tournoi_name = input('Enter the tournament name: ').upper()
        tournoi_search = Query()
        tournoi_dict = tournois_table.search(tournoi_search.name == tournoi_name)

    tournoi_deserialized = ''

    # The loop below allows to work directly on the only dictionary contained in the tournoi_dict list
    for element in tournoi_dict:
        element_date = element['date_list']
        if len(element_date) == 10:
            element_date = element['date_list']
        elif len(element_date) == 12:
            element_date = element['date_list'][1: -1]
        elif len(element_date) == 14:
            element_date = element['date_list'][2: -2]
        else:
            element_date = element['date_list'][3: -3]

        tournoi_deserialized = Tournoi(element['name'], element['place'], element_date,
                                       element['rounds_list'],
                                       element['description'], element['time_controller'],
                                       deserializeplayersdicos(element['players_list']),
                                       element['rounds_number'])

    return tournoi_deserialized


def deserializealltournois():
    """This function will deserialize all the tournois in the DB and return a list containing all of them"""

    tournament_list = []
    deserialized_tournoi_list = tournois_table.all()

    # The loop below allows to work directly on the only dictionary contained in the deserialized tournoi list
    for element in deserialized_tournoi_list:
        tournoi_deserialized = Tournoi(element['name'], element['place'], element['date_list'], element['rounds_list'],
                                       element['description'], element['time_controller'],
                                       deserializeplayersdicos(element['players_list']),
                                       element['rounds_number'])
        tournament_list.append(tournoi_deserialized)

    return tournament_list


def deserializerounds(tournoi_deserialized):
    rounds_dict = tournoi_deserialized.rounds_list
    rounds_list = []

    for round_dico in rounds_dict:
        round_deserialized = Tour(round_dico['round_name'], round_dico['date_time_begin'],
                                  round_dico['date_time_finish'], round_dico['matches_list'])
        rounds_list.append(round_deserialized)

    return rounds_list


def deserializetournoiwithname(tournoi_name):
    """This function deserializes a specific tournoi based on the name"""
    tournoi_search = Query()
    tournoi_dict = tournois_table.search(tournoi_search.name == tournoi_name)

    tournoi_deserialized = ''

    # The loop below allows to work directly on the only dictionary contained in the tournoi_dict list
    for element in tournoi_dict:
        element_date = element['date_list']
        if len(element_date) == 10:
            element_date = element['date_list']
        elif len(element_date) == 12:
            element_date = element['date_list'][1: -1]
        elif len(element_date) == 14:
            element_date = element['date_list'][2: -2]
        else:
            element_date = element['date_list'][3: -3]

        tournoi_deserialized = Tournoi(element['name'], element['place'], element_date,
                                       element['rounds_list'],
                                       element['description'], element['time_controller'],
                                       deserializeplayersdicos(element['players_list']),
                                       element['rounds_number'])

    return tournoi_deserialized
