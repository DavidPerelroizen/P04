from Models.classjoueur import Joueur
from Models.classtournoi import Tournoi


def allplayersrankingupdate(tournoi):
    forbidden_ranks = []
    updated_rank = 0
    joueur = ''

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
