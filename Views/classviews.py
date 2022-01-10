from Models.classtour import Tour

class View:

    def displaymainmenu(self):
        """
        Displays the app main menue
        """
        print(
            """
            CHESS APPLICATOR
        ----------------------------------
                MAIN MENU
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
                     REPORTING MENU
        --------------------------------------------
        1. All players list --> press A
        2. Players of a tournament list --> press P
        3. All tournaments list --> press T
        4. Tournament all rounds list --> press R
        5. Tournament all matches list --> press M        
        --------------------------------------------""")
        user_choice = input('        Press the appropriate key + ENTER : ').upper()

        return user_choice

    def displayroundresult(self, i):
        print('Round ', i, ' is finished')

    def proposerankingupdate(self):
        user_choice = input('Do you want to update the players ranking? (Yes/No)').upper()
        return user_choice

    def displayallplayerslist(self):
        pass

    def displaytournamentplayers(self, tournament_name):
        pass