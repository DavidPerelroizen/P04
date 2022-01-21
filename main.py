from Views.classviews import View
from Models.classclassement import Classement
from Controllers.roundmanager import roundmanager
from Controllers.generatepairs import generatepairs
from Controllers.tournoicreator import tournoicreation
from Models.constants import yes_list, no_list
from Controllers.allplayersrankingupdate import specificplayerrankingupdate
from Controllers.dbtournoi import serializetournoi, deserializetournoi, tournois_table, deserializetournoiwithname,\
    deserializerounds
from Controllers.Utils.playerscreation import playerscreation
from Controllers.Utils.roundslauncher import roundslauncher
from Controllers.Utils.updaterankings import updaterankings
from tinydb import Query


def main():
    view = View()
    user_choice = view.displaymainmenu().upper()

    if user_choice == 'T':
        """Tournament management"""

        #  Tournament initialization
        tournoi = tournoicreation()
        print("")

        # Propose to save and postpone the rest of the tournament process
        user_choice = ''
        while user_choice not in yes_list and user_choice not in no_list:
            user_choice = input('Save and continue later ---> Yes, Continue now --> No: ')
        if user_choice in yes_list:
            serializetournoi(tournoi)
            main()
        else:
            #  Players creation
            tournoi = playerscreation(tournoi)
            print("")

            # Propose to save and postpone the rest of the tournament process
            user_choice = ''
            while user_choice not in yes_list and user_choice not in no_list:
                user_choice = input('Save and continue later ---> Yes, Continue now --> No: ')
            if user_choice in yes_list:
                serializetournoi(tournoi)
                main()
            else:
                #  Launch the rounds
                tournoi = roundslauncher(tournoi)

                #  Update rankings
                updaterankings(tournoi)
                print("End of the game")
                main()

    elif user_choice == 'C':
        """Complete an already created tournament with players and rounds"""
        print("""
        -----------------------------------------
                    Complete an existing
                        Tournament
        -----------------------------------------""")
        tournament_list = view.displaytournamentwithoutplayerslistsimplified()
        if not tournament_list:
            print('No tournament needs completion')
            main()
        else:
            print('')

            # Deserialize a tournoi to complete and removes the incomplete instance from the database
            tournoi = deserializetournoi()
            tournoi_search = Query()
            tournois_table.remove(tournoi_search.name == tournoi.name)

            #  Players creation
            tournoi = playerscreation(tournoi)
            print("")

            # Propose to save and postpone the rest of the tournament process
            user_choice = ''
            while user_choice not in yes_list and user_choice not in no_list:
                user_choice = input('Save and continue later ---> Yes, Continue now --> No: ')
            if user_choice in yes_list:
                serializetournoi(tournoi)
                main()
            else:
                #  Launch the rounds
                tournoi = roundslauncher(tournoi)

                #  Update rankings
                updaterankings(tournoi)
                print("End of the game")
                main()

    elif user_choice == 'R':
        """Reporting management"""
        user_choice = view.displayreportingmenu()

        if user_choice == "A":
            view.displayallplayerslist()
            print('')
            main()

        elif user_choice == "P":
            view.displaytournamentlistsimplified()
            print('')
            view.displaytournamentplayers()
            print('')
            main()

        elif user_choice == "T":
            view.displayalltournaments()
            print('')
            main()

        elif user_choice == "R":
            view.displaytournamentlistsimplified()
            print('')
            view.displaytournamentallrounds()
            print('')
            main()

        elif user_choice == "M":
            view.displaytournamentlistsimplified()
            print('')
            view.displaytournamenetallmatches()
            print('')
            main()

        else:
            print('')
            main()

    elif user_choice == 'S':
        """Complete an already created tournament with rounds"""
        print("""
        -----------------------------------------
                    Complete an existing
                    tournament with rounds
        -----------------------------------------""")
        tournament_list = view.displaytournamentwithoutroundslistsimplified()
        if not tournament_list:
            print('No tournament needs completion')
            main()
        else:
            print('')

            # Deserialize a tournoi to complete and removes the incomplete instance from the database
            tournoi = deserializetournoi()
            tournoi_search = Query()
            tournois_table.remove(tournoi_search.name == tournoi.name)

            #  Launch the rounds
            tournoi = roundslauncher(tournoi)

            #  Update rankings
            updaterankings(tournoi)
            print("End of the game")
            main()

    elif user_choice == 'U':
        print(
            """
            ------------------------
               PLAYER RANK UPDATE
            ------------------------
            """
        )
        user_option = 'Yes'
        while user_option in yes_list:
            specificplayerrankingupdate()
            user_option = input('Do you want to update another players rank? (Yes/No): ').upper()
        main()

    elif user_choice == 'M':
        """Complete an already created tournament for which some rounds have been played with the missing rounds"""
        print("""
        -----------------------------------------
                    Complete an existing
            tournament with the missing rounds
        -----------------------------------------""")
        tournament_list = view.displaytournamentwithmissingroundslistsimplified()
        if not tournament_list:
            print('No tournament needs completion')
            main()
        else:
            print('')
            tournament_name_for_update = ''
            while tournament_name_for_update not in tournament_list:
                try:
                    tournament_name_for_update = input('Please enter the name of the tournament to update: ').upper()
                    ' '.join(tournament_name_for_update.split())
                except ValueError:
                    print('Enter the tournament exact name.')

            # Deserialize a tournoi to complete and removes the incomplete instance from the database
            tournoi = deserializetournoiwithname(tournament_name_for_update)
            tournoi_search = Query()
            tournois_table.remove(tournoi_search.name == tournoi.name)

            # Deserialize the rounds
            rounds_list_deserialized = deserializerounds(tournoi)

            # Inject the deserialized rounds list in the tournoi instance
            tournoi.rounds_list = rounds_list_deserialized

            #  Launch the rounds
            classement = Classement()
            rounds_pairs_list = []
            for i in range(len(tournoi.rounds_list) + 1, tournoi.rounds_number + 1):
                """
                For each round, the program will follow the below steps:
                1. Refresh the ranking
                2. Generate a new set of pairs
                3. Play the round
                4. Add the round info to the tournoi
                5. Add the round pairs list to the instance of the round
                """

                players_ranking = classement.ranking(tournoi.players_list)  # Step 1
                pairs_list = generatepairs(players_ranking, rounds_pairs_list, i, len(tournoi.players_list))  # Step2
                round_information = roundmanager(i, pairs_list)  # Step 3
                tournoi.rounds_list.append(round_information)  # Step 4
                rounds_pairs_list.append(pairs_list)  # Step 5
                print("")
                view.displayroundresult(i, round_information)
                print("")

                # Propose to save and postpone the rest of the tournament process
                user_choice = ''
                while user_choice not in yes_list and user_choice not in no_list:
                    user_choice = input('Save and continue later ---> Yes, Continue now --> No: ')
                if user_choice in yes_list:
                    break

            #  Update rankings
            updaterankings(tournoi)
            print("End of the game")
            main()

    else:
        exit()


if __name__ == '__main__':
    main()
