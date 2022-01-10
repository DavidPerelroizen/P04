from Models.classtour import Tour
from Models.classtournoi import Tournoi


class View:

    def displaymainmenu(self):
        """
        Displays the app main menue
        """
        print(
            """
            CHESS APPLICATOR
        ----------------------------------
                MAIN MENUE
        ----------------------------------
        1. Tournament manager --> press T
        2. Reports --> press R
        3. Exit program --> press X
        ----------------------------------""")
        user_choice = input('        Press the appropriate key + ENTER : ').upper()

        return user_choice

    def displayreportingmenu(self):
        """
        Displays the secondary secondary menue
        Application: reporting
        """
        print(
            """
                    CHESS APPLICATOR
        --------------------------------------------
                     REPORTING MENUE
        --------------------------------------------
        1. All players list --> press A
        2. Players of a tournament list --> press P
        3. All tournaments list --> press T
        4. Tournament all rounds list --> press R
        5. Tournament all matches list --> press M 
        6. Back to main menue --> press B   
        --------------------------------------------""")
        user_choice = input('        Press the appropriate key + ENTER : ').upper()

        return user_choice

    def displayroundresult(self, i, round_to_display):
        print('Round ', i, ' is finished')
        print(f'Round start time: {round_to_display.date_time_begin}')
        print(f'Round end time: {round_to_display.date_time_finish}')
        print('Matches list: ')
        for match in round_to_display.matches_list:
            print(match)

    def proposerankingupdate(self):
        user_choice = input('Do you want to update the players ranking? (Yes/No): ').upper()
        return user_choice

    def displayallplayerslist(self, tournaments_list):
        user_choice = ''
        while user_choice not in ['ALPHABETICAL', 'RANKING']:
            user_choice = input('Alphabetical or ranking display?: ').upper()
            if user_choice == 'ALPHABETICAL':
                print(f"Display all players list in alphabetical order")
                reporting_list = []
                for tournament in tournaments_list:
                    for player in tournament.players_list:
                        reporting_list.append(player)
                reporting_list.sort(key=lambda x: x[1])
                for item in reporting_list:
                    print(item)

            elif user_choice == 'RANKING':
                print(f"Display all players list in ranking order")
                reporting_list = []
                for tournament in tournaments_list:
                    for player in tournament.players_list:
                        reporting_list.append(player)
                reporting_list.sort(key=lambda x: x[5])
                for item in reporting_list:
                    print(item)

            else:
                print('Wrong value, try again!')

    def displaytournamentplayers(self, tournament):
        user_choice = ''
        while user_choice not in ['ALPHABETICAL', 'RANKING']:
            user_choice = input('Alphabetical or ranking display?: ').upper()
            if user_choice == 'ALPHABETICAL':
                print(f"Display {tournament.name} players list in alphabetical order")
                reporting_list =[]
                for player in tournament.players_list:
                    reporting_list.append(player)
                reporting_list.sort(key=lambda x: x[1])
                for item in reporting_list:
                    print(item)

            elif user_choice == 'RANKING':
                print(f"Display {tournament.name} players list in ranking order")
                reporting_list = []
                for player in tournament.players_list:
                    reporting_list.append(player)
                reporting_list.sort(key=lambda x: x[5])
                for item in reporting_list:
                    print(item)

            else:
                print('Wrong value, try again')

    def displayalltournaments(self, tournament_list):
        for tournament in tournament_list:
            print(f'{tournament.name} in {tournament.place} on {tournament.date_list}, was played with a '
                  f'{tournament.time_controller} time controller')

    def displaytournamentallrounds(self, tournament):
        for rounds in tournament.rounds_list:
            print(rounds)



