def generatepairs(players_ranking, rounds_list, round_number, number_of_players=8):
    """
    This function will generate pairs of players for a given round number
    It will return a list of tuples
    """
    new_pairs_list = []
    if round_number == 1:
        new_pairs_list = [
            (players_ranking[0], players_ranking[4]),
            (players_ranking[1], players_ranking[5]),
            (players_ranking[2], players_ranking[6]),
            (players_ranking[3], players_ranking[7])
        ]

    else:
        i = 0
        taken_indexes = []
        for j in range(number_of_players):
            k = 0
            if i == j:
                continue

            elif j in taken_indexes:
                continue

            elif [players_ranking[i], players_ranking[j]] \
                    or [players_ranking[j], players_ranking[i]] not in rounds_list[k] and \
                    [players_ranking[i], players_ranking[j]] \
                    or [players_ranking[j], players_ranking[i]] not in new_pairs_list:
                new_pairs_list.append((players_ranking[i], players_ranking[j]))
                taken_indexes.append(j)
                #  The "if" block below prevents a player to play against himself
                if i == j - 1:
                    i += 2
                else:
                    i += 1
            else:
                k += 1

    return new_pairs_list
