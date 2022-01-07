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
        ----------------------------------""")
        user_choice = input('        Press the appropriate key + ENTER : ')

        return user_choice

    def displaytournamentmenu(self):
        """
        Displays the first secondary menue
        Application: Tournament management
        """
        print(
            """
                CHESS APPLICATOR
        ----------------------------------
                TOURNAMENT MENU
        ----------------------------------
        1. Create tournament --> press C
        2. Add players --> press A
        3. Start tournament --> press S
        4. Update rankings --> press U        
        ----------------------------------""")
        user_choice = input('        Press the appropriate key + ENTER : ')

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
        user_choice = input('        Press the appropriate key + ENTER : ')

        return user_choice
