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
            code_result = int(input(f'Enter code result {match.paire_joueurs}: '))
            round_match_list.append(match.resultmatch(code_result))

    round_generated.finishround()

    return print('Début du round', round_generated.date_time_begin,
                 round_match_list,
                 'Fin du round', round_generated.date_time_finish)







