from Models.classtour import Tour
from Models.classmatch import Match
from Models.constants import codes_results, yes_list


def roundmanager(round_index, pairs_list):
    """
    For a given index and a given list of pairs of players, this function will instantiate a round,
    create matches and then allow the user to input the match result.
    Information about the round start and end time, and the list of match/results will be stored in the round instance.
    """

    round_match_list = []
    round_name = 'Round ' + str(round_index)

    round_generated = Tour(round_name, 0, 0, [])

    round_generated.initiateround()  # Registers the start time of the round

    for pair in pairs_list:
        round_generated.addmatch(pair)  # Transforms a players pair into a match instance in the round match list

    enter_result = 'No'
    while enter_result not in yes_list:
        enter_result = input('Do you want to enter the results? (Yes/No) : ').lower()

    if enter_result in yes_list:
        for game in round_generated.matches_list:
            # Enables to input the result of each match from the match list
            match = Match(game)
            print('Result codes: 0 = pat, 1 = player 1 wins, 2 = player 2 wins')
            code_result = ''
            while code_result not in codes_results:
                try:
                    code_result = int(
                        input(f'Enter code result {match.paire_joueurs[0][0]} vs {match.paire_joueurs[1][0]} : '))
                except ValueError:
                    print('Please enter a valid code result (0, 1 or 2)')
            round_match_list.append(match.resultmatch(code_result))  # Appends to the match list of the round a \
            # tuple containing two lists. Each contains the player instance and the score earned

    round_generated.matches_list = round_match_list  # Round instance receives the matches with player info and score

    round_generated.finishround()  # Registers the end time of the round

    return round_generated
