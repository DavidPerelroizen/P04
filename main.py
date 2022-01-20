from Views.classviews import View
from Controllers.tournoicreator import tournoicreation
from Models.constants import yes_list, no_list
from Controllers.allplayersrankingupdate import specificplayerrankingupdate
from Controllers.dbtournoi import serializetournoi, deserializetournoi, tournois_table
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
            user_choice = input('Do you want to save and continue the tournament creation later? (Yes/No): ')
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
                user_choice = input('Do you want to save and continue the tournament creation later? (Yes/No): ')
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
                user_choice = input('Do you want to save and continue the tournament creation later? (Yes/No): ')
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

    else:
        exit()


if __name__ == '__main__':
    main()
