import json
from tinydb import TinyDB, Query


db = TinyDB('db.json')
players_table = db.table('players')

def serializeplayer(player_for_serializing):
    """This function aims at serializing a player (class = Joueur()) and insert is in the tiny DB"""
    player_dict = {
        'player_index': player_for_serializing.player_index, 'last_name': player_for_serializing.last_name,
        'first_name': player_for_serializing.first_name,
        'birth_date': json.dumps(player_for_serializing.birth_date, default=str),
        'gender': player_for_serializing.gender,
        'rank': player_for_serializing.rank, 'score': player_for_serializing.score
    }

    players_table.insert(player_dict)

def deserializeallplayers():
    """
    This function aims at deserializing the all the players data from the players_table in order to use it
     as lists in reporting
    """
    deserialized_players_list = []
    deserialized_players = players_table.all()

    for dico in deserialized_players:
        player_info_list = [
                            dico['player_index'], dico['last_name'], dico['first_name'], dico['birth_date'],
                            dico['gender'], dico['rank'], dico['score']
                            ]
        deserialized_players_list.append(player_info_list)

    return deserialized_players_list

def updateplayersscore(player_index_researched, score_update):
    """Function that updates a given player's score depending on his index"""
    Playerquery = Query()
    players_table.update({'score': score_update}, Playerquery.player_index == player_index_researched)

def updateplayersrank(player_index_researched, rank_update):
    """Function that updates a given player's rank depending on his index"""
    Playerquery = Query()
    players_table.update({'rank': rank_update}, Playerquery.player_index == player_index_researched)
