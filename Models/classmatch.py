from Models.constants import codes_results, match_points


class Match:

    def __init__(self, paire_joueurs):
        self.paire_joueurs = paire_joueurs

    def resultmatch(self, code_result):
        """
        This function returns the match result depending on the code_result provided
        (0 = pat, 1 = player 1 wins, 2 = player 2 wins)
        """

        if code_result == codes_results[0]:
            self.paire_joueurs[0][6] += match_points['Pat']
            self.paire_joueurs[1][6] += match_points['Pat']
            return [self.paire_joueurs[0][0], match_points['Pat']], \
                   [self.paire_joueurs[1][0], match_points['Pat']]

        elif code_result == codes_results[1]:
            self.paire_joueurs[0][6] += match_points['Victory']
            self.paire_joueurs[1][6] += match_points['Defeat']
            return [self.paire_joueurs[0][0], match_points['Victory']], \
                   [self.paire_joueurs[1][0], match_points['Defeat']]

        else:
            self.paire_joueurs[0][6] += match_points['Defeat']
            self.paire_joueurs[1][6] += match_points['Victory']
            return [self.paire_joueurs[0][0], match_points['Defeat']], \
                   [self.paire_joueurs[1][0], match_points['Victory']]
