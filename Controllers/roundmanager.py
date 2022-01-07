from Models.classtour import Tour
from Models.classmatch import Match
from Models.constants import codes_results


def roundmanager(round_index, pairs_list):

    round_match_list = []
    round_name = 'Round ' + str(round_index)

    round_generated = Tour(round_name)
    round_generated.initiateround()

    for pair in pairs_list:
        round_generated.addmatch(pair)


    enter_result = 'No'
    while enter_result == 'No':
        enter_result = input('Do you want to enter the results? (Yes/No) : ')

    if enter_result == 'Yes':
        for tuple in round_generated.matches_list:
            match = Match(tuple)
            print('Result codes: 0 = pat, 1 = player 1 wins, 2 = player 2 wins')
            code_result = int(input(f'Enter code result {match.paire_joueurs[0][0]} vs {match.paire_joueurs[1][0]} : '))
            round_match_list.append(match.resultmatch(code_result))

    round_generated.finishround()

    return round_match_list







