from Models.classclassement import Classement
from Models.constants import yes_list, no_list
from Views.classviews import View
from Controllers.generatepairs import generatepairs
from Controllers.roundmanager import roundmanager


def roundslauncher(tournoi):
    """This function consolidates the code helping to launch rounds"""
    view = View()
    players_number = len(tournoi.players_list)
    rounds_number = 0

    if not tournoi.rounds_list:
        while rounds_number > players_number - 1 or rounds_number == 0:
            try:
                rounds_number = int(
                    input(f'How many rounds do you want to play? (max value = {players_number - 1}): '))
            except ValueError:
                print('Please enter an integer.')
        print("")
        tournoi.rounds_number = rounds_number
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

            # Propose to save and postpone the rest of the tournament process
            user_choice = ''
            while user_choice not in yes_list and user_choice not in no_list:
                user_choice = input('Save and continue later ---> Yes, Continue now --> No: ')
            if user_choice in yes_list:
                break

        else:  # Enables the user to complete the missing rounds of a tournament
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
                pairs_list = generatepairs(players_ranking, rounds_pairs_list, i, players_number)  # Step2
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

    return tournoi
