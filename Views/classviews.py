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

    def displayroundresult(self, i):
        print('Round ', {i}, ' is finished')
