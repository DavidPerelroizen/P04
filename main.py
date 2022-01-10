from Views.classviews import View
from Controllers.tournoicreator import tournoicreation
from Controllers.playersmanager import gettheplayers
from Controllers.generatepairs import generatepairs
from Models.classclassement import Classement
from Controllers.roundmanager import roundmanager
from Models.classjoueur import Joueur
from Models.constants import yes_list


def main():
    view = View()
    user_choice = view.displaymainmenu().upper()

    if user_choice == 'T':
        """Tournament management"""
        #  Tournament creation
        tournoi = tournoicreation()
        print("")
        #  Players creation
        players_number = int(input('How many players do you want to add?: '))
        tournoi.players_list = gettheplayers(players_number)
        print("")
        #  Launch the rounds
        rounds_number = int(input('How many rounds do you want to play?: '))
        print("")
        classement = Classement()
        rounds_pairs_list = []
        for i in range(1, rounds_number + 1):
            players_ranking = classement.ranking(tournoi.players_list)
            pairs_list = generatepairs(players_ranking, rounds_pairs_list, i, players_number)
            round_match_list = roundmanager(i, pairs_list)
            tournoi.rounds_list.append(round_match_list)
            rounds_pairs_list.append(pairs_list)
            view.displayroundresult(i)
            print("")

        #  Update rankings
        user_choice_for_update = view.proposerankingupdate()
        if user_choice_for_update in yes_list:
            for player in tournoi.players_list:
                joueur = Joueur(player[0], player[1], player[2], player[3], player[4], player[5], player[6])
                updated_rank = int(input(f'Enter the new rank for {joueur.player_index} (Integer between 1 and 8): '))
                joueur.updaterank(updated_rank)
            print("End of the game")
            main()

        else:
            print("End of the game")
            main()

    elif user_choice == 'R':
        """Reporting management"""
        view.displayreportingmenu()

    else:
        exit()


if __name__ == '__main__':
    main()
