import json
from tinydb import TinyDB, Query
from Models.classtournoi import Tournoi
from Controllers.dbplayers import deserializeplayersdicos


db = TinyDB('db.json')
tournois_table = db.table('tournois')


def serializetournoi(tournoi_for_serializing):
    """
    This function aims at serializing a tournoi (class = Tournoi()) and insert is in the tiny DB
    :param tournoi_for_serializing:
    :return:
    """
    rounds_list_for_serialization = []
    for round_instance in tournoi_for_serializing.rounds_list:
        round_dict = {'round_name': round_instance.round_name,
                      'date_time_begin': json.dumps(round_instance.date_time_begin, default=str),
                      'date_time_finish': json.dumps(round_instance.date_time_finish, default=str),
                      'matches_list': round_instance.matches_list
                      }
        rounds_list_for_serialization.append(round_dict)

    players_list_for_serialization = []
    for player_instance in tournoi_for_serializing.players_list:
        player_dict = {'player_index': player_instance[0],
                       'last_name': player_instance[1],
                       'first_name': player_instance[2],
                       'birth_date': json.dumps(player_instance[3], default=str),
                       'gender': player_instance[4],
                       'rank': player_instance[5],
                       'score': player_instance[6]}
        players_list_for_serialization.append(player_dict)

    tournoi_dict = {
        'name': tournoi_for_serializing.name, 'place': tournoi_for_serializing.place,
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
        tournoi_name = input('Enter the tournament name: ')
        Tournoi_search = Query()
        tournoi_dict = tournois_table.search(Tournoi_search.name == tournoi_name)

    tournoi_deserialized = ''

    for element in tournoi_dict:
        tournoi_deserialized = Tournoi(element['name'], element['place'], element['date_list'], element['rounds_list'],
                                       element['description'], element['time_controller'],
                                       deserializeplayersdicos(element['players_list']),
                                       element['rounds_number'])

    return tournoi_deserialized

def deserializealltournois():
    """This function will deserialize all the tournois in the DB and return a list containing all of them"""

    tournament_list = []
    deserialized_tournoi_list = tournois_table.all()

    for element in deserialized_tournoi_list:
        tournoi_deserialized = Tournoi(element['name'], element['place'], element['date_list'], element['rounds_list'],
                                       element['description'], element['time_controller'],
                                       deserializeplayersdicos(element['players_list']),
                                       element['rounds_number'])
        tournament_list.append(tournoi_deserialized)

    return tournament_list

