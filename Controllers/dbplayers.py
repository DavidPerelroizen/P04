import json
from tinydb import TinyDB


playersdb = TinyDB('db.json')
playersdb.truncate()


def serializeplayer(player_for_serializing):
    """This function aims at serializing a player (class = Joueur()) and insert is in the tiny DB"""
    player_dict = {
        'player_index': player_for_serializing.player_index, 'last_name': player_for_serializing.last_name,
        'first_name': player_for_serializing.first_name,
        'birth_date': json.dumps(player_for_serializing.birth_date, default=str),
        'gender': player_for_serializing.gender,
        'rank': player_for_serializing.rank, 'score': player_for_serializing.score
    }
    playersdb.insert(player_dict)
