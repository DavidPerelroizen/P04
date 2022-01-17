from Models.classtour import Tour
from Models.constants import reporting_menu_list, main_menu_list, yes_list, reporting_ordering_dict, no_list, \
    header_allplayerslist
from Controllers.dbplayers import deserializeallplayers
from Controllers.dbtournoi import deserializetournoi, deserializealltournois, deserializerounds


class View:

    def displaymainmenu(self):
        """
        Displays the app main menu
        """

        user_choice = ''
        while user_choice not in main_menu_list:
            print(
                """
                CHESS APPLICATOR
            ----------------------------------
                    MAIN MENU
            ----------------------------------
            1. Tournament manager --> press T
            2. Reports --> press R
            3. Update player rank --> U
            4. Exit program --> press X
            ----------------------------------""")
            user_choice = input('        Press the appropriate key + ENTER : ').upper()

        return user_choice

    def displayreportingmenu(self):
        """
        Displays the secondary secondary menu
        Application: reporting
        """
        print(
            """
                    CHESS APPLICATOR
        --------------------------------------------
                     REPORTING MENU
        --------------------------------------------
        1. All players list --> press A
        2. Players of a tournament list --> press P
        3. All tournaments list --> press T
        4. Tournament all rounds list --> press R
        5. Tournament all matches list --> press M
        6. Back to main menu --> press B
        --------------------------------------------""")
        user_choice = ''
        while user_choice not in reporting_menu_list:
            user_choice = input('        Press the appropriate key + ENTER : ').upper()

        return user_choice

    def displayroundresult(self, i, round_to_display):
        """This function summarizes the information about a specific round"""

        print('Round ', i, ' is finished')
        print(f'Round start time: {round_to_display.date_time_begin}')
        print(f'Round end time: {round_to_display.date_time_finish}')
        print('Matches list: ')
        for match in round_to_display.matches_list:
            print(match)

    def proposerankingupdate(self):
        """Function to propose a ranking update"""

        user_choice = ''
        while user_choice not in yes_list and user_choice not in no_list:
            user_choice = input('Do you want to update the players ranking? (Yes/No): ').upper()
        return user_choice

    def displayallplayerslist(self):
        """Reporting function that will display all the players of all the tournaments in the database"""

        user_choice = ''

        while user_choice not in ['ALPHABETICAL', 'RANKING']:
            try:
                user_choice = reporting_ordering_dict[int(input(
                    'Alphabetical (press 1) or ranking display (press 2)?: '))]
            except ValueError:
                print('Please enter a valid key')
            except KeyError:
                print('Please enter a valid key')

            # Deserialize the database content
            deserialized_players = deserializeallplayers()

            # List displayed by alphabetical order
            if user_choice == 'ALPHABETICAL':
                print("Display all players list in alphabetical order")
                print(f"""
-------------------------------------------------------------------
{header_allplayerslist}
-------------------------------------------------------------------""")
                reporting_list = []
                for player_deserialized in deserialized_players:
                    reporting_list.append(player_deserialized)
                reporting_list.sort(key=lambda x: x[1])
                for item in reporting_list:
                    print(item)

            # List displayed by ranking order
            elif user_choice == 'RANKING':
                print("Display all players list in ranking order")
                print(f"""
-------------------------------------------------------------------
{header_allplayerslist}
-------------------------------------------------------------------""")
                reporting_list = []
                for player_deserialized in deserialized_players:
                    reporting_list.append(player_deserialized)
                reporting_list.sort(key=lambda x: x[5])
                for item in reporting_list:
                    print(item)

            else:
                print('Wrong value, try again!')

    def displaytournamentplayers(self):
        """Reporting function that will display all the players of a specific tournament"""

        user_choice = ''
        while user_choice not in ['ALPHABETICAL', 'RANKING']:
            try:
                user_choice = reporting_ordering_dict[int(input(
                    'Alphabetical (press 1) or ranking display (press 2)?: '))]
            except ValueError:
                print('Please enter a valid key')
            except KeyError:
                print('Please enter a valid key')

            # Deserialize the tournament
            tournament = deserializetournoi()

            # List displayed by alphabetical order
            if user_choice == 'ALPHABETICAL':
                print(f"Display {tournament.name} players list in alphabetical order")
                print(f"""
-------------------------------------------------------------------
{header_allplayerslist}
-------------------------------------------------------------------""")
                reporting_list = []
                for player in tournament.players_list:
                    reporting_list.append(player)
                reporting_list.sort(key=lambda x: x[1])
                for item in reporting_list:
                    print(item)

            # List displayed by ranking order
            elif user_choice == 'RANKING':
                print(f"Display {tournament.name} players list in ranking order")
                print("Display all players list in alphabetical order")
                print(f"""
-------------------------------------------------------------------
{header_allplayerslist}
-------------------------------------------------------------------""")
                reporting_list = []
                for player in tournament.players_list:
                    reporting_list.append(player)
                reporting_list.sort(key=lambda x: x[5])
                for item in reporting_list:
                    print(item)

            else:
                print('Wrong value, try again')

    def displayalltournaments(self):
        """Reporting function that displays all the tournaments info from a list"""
        tournament_list = deserializealltournois()
        print('')
        print("""
        --------------------------------------------------------
                        ALL TOURNAMENTS LIST
        --------------------------------------------------------""")
        for tournament in tournament_list:
            print(f'{tournament.name} in {tournament.place} on {tournament.date_list}, was played with a '
                  f'{tournament.time_controller} time controller')

    def displaytournamentallrounds(self):
        """Reporting function that displays all the rounds info from a specific tournament"""
        tournament = deserializetournoi()

        # For each round info contained into the tournament, the loop will instantiate a Tour object
        for rounds in tournament.rounds_list:
            tour = Tour(rounds['round_name'], rounds['date_time_begin'], rounds['date_time_finish'],
                        rounds['matches_list'])
            print("-----------------------------------------------")
            print(tour.round_name)
            print(f'Round start time: {tour.date_time_begin}')
            print(f'Round end time: {tour.date_time_finish}')
            print('Matches list: ')
            for match in tour.matches_list:
                print(match)
            print("-----------------------------------------------")

    def displaytournamenetallmatches(self):
        """Reporting function that displays all the matches from a specific tournament"""
        tournament = deserializetournoi()  # Deserialize the desired tournament

        rounds_list = deserializerounds(tournament)  # Get the list of Tour objects

        # From the Tour objects, get the matches list and print the desired output
        match_list = []
        for rounds in rounds_list:
            for match in rounds.matches_list:
                match_list.append(match)
        print(f"""
-------------------------------------------------------------------
                       MATCHES LIST
                        {tournament.name}
-------------------------------------------------------------------""")
        for item in match_list:
            if item[0][1] > item[1][1]:
                print(f'{item[0][0]} vs {item[1][0]} : {item[0][0]} wins')
            elif item[0][1] < item[1][1]:
                print(f'{item[0][0]} vs {item[1][0]} : {item[1][0]} wins')
            else:
                print(f'{item[0][0]} vs {item[1][0]} : stalemate')
