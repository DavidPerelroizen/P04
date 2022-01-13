import json
from tinydb import TinyDB


tournoidb = TinyDB('db.json')
tournoidb.truncate()

def serializetournoi(tournoi_for_serializing):
    """
    This function aims at serializing a tournoi (class = Tournoi()) and insert is in the tiny DB
    :param tournoi_for_serializing:
    :return:
    """

    tournoi_dict = {
                    'name': tournoi_for_serializing.name, 'place': tournoi_for_serializing.place,
                    'date_list': json.dumps(tournoi_for_serializing.date_list, default=str),
                    'rounds_list': tournoi_for_serializing.rounds_list,
                    'description': tournoi_for_serializing.description,
                    'time_controller': tournoi_for_serializing.time_controller,
                    'players_list': tournoi_for_serializing.players_list,
                    'rounds_number': tournoi_for_serializing.rounds_number
                    }

    tournoidb.insert(tournoi_dict)
