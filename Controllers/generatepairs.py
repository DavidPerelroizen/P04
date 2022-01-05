def generatepairs(players_ranking, rounds_list, round_number):
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
        for j in range(1, len(players_ranking)):
            k = 0
            if i == j:
                continue

            elif [players_ranking[i], players_ranking[j]] \
                    or [players_ranking[j], players_ranking[i]] not in rounds_list[k]:
                new_pairs_list.append((players_ranking[i], players_ranking[j]))
                if i == j - 1:
                    i += 2
                else:
                    i += 1
            else:
                k += 1

    return new_pairs_list
