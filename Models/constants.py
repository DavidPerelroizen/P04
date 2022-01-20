""" This module contains all the constants and generic lists used in the code"""

time_controllers = ['bullet', 'coup rapide', "blitz"]

codes_results = [0, 1, 2]

match_points = {'Stalemate': 0.5, 'Victory': 1, 'Defeat': 0}

gender_dict = {1: 'man', 2: 'woman'}

yes_list = ['y', 'Y', 'Yes', 'YES', 'yes', 'yES']

no_list = ['No', 'NO', 'no', 'nO', 'N', 'n']

reporting_menu_list = ['A', 'P', 'T', 'R', 'M', 'B']

main_menu_list = ['T', 'R', 'X', 'U', 'C', 'S', 'M']

time_controllers_dict = {3: 'bullet', 2: 'coup rapide', 1: 'blitz'}

header_allplayerslist = ['Player index', 'Last name', 'First name', 'Birthday', 'Gender', 'Rank', 'Score']

reporting_ordering_dict = {1: 'ALPHABETICAL', 2: 'RANKING'}

main_menu_display = """
                CHESS APPLICATOR
            --------------------------------------------
                    MAIN MENU
            --------------------------------------------
            1. Tournament manager --> press T
            2. Complete a saved tournament with players
                and rounds --> press C
            3. Complete a saved tournament with rounds
                --> press S
            4. Complete a saved tournament with the 
                missing rounds --> M
            5. Reports --> press R
            6. Update player rank --> U
            7. Exit program --> press X
            --------------------------------------------"""

reporting_menu_display = """
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
        --------------------------------------------"""
