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

        #  Tournament initialization
        tournoi = tournoicreation()
        print("")

        #  Players creation
        players_number = 0
        while players_number % 2 != 0 or players_number == 0:
            try:
                players_number = int(input('How many players do you want to add? (even numbers only): '))
            except ValueError:
                print('Please enter an even number of players')
        tournoi.players_list = gettheplayers(players_number)
        print("")

        #  Launch the rounds
        rounds_number = int(input('How many rounds do you want to play?: '))
        print("")
        classement = Classement()
        rounds_pairs_list = []
        for i in range(1, rounds_number + 1):
            """
            For each round, the program will follow the below steps:
            1. Refresh the ranking
            2. Generate a new set of pairs
            3. Play the round
            4. Add the round info to the tournoi
            5. Add the round pairs list to the instance of the round
            """
            players_ranking = classement.ranking(tournoi.players_list)  # Step 1
            pairs_list = generatepairs(players_ranking, rounds_pairs_list, i, players_number)  # Step2
            round_information = roundmanager(i, pairs_list)  # Step 3
            tournoi.rounds_list.append(round_information)  # Step 4
            rounds_pairs_list.append(pairs_list)  # Step 5
            print("")
            view.displayroundresult(i, round_information)
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
        user_choice = view.displayreportingmenu()

        if user_choice == "A":
            pass

        elif user_choice == "P":
            pass

    else:
        exit()


if __name__ == '__main__':
    main()
