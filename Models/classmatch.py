from Models.constants import codes_results, match_points
from Controllers.dbplayers import updateplayersscore


class Match:

    def __init__(self, paire_joueurs):
        self.paire_joueurs = paire_joueurs

    def resultmatch(self, code_result):
        """
        This function returns the match result depending on the code_result provided
        List of possible codes for results: 0 = pat, 1 = player 1 wins, 2 = player 2 wins
        This list is stored in the constants module
        """

        if code_result == codes_results[0]:
            self.paire_joueurs[0][6] += match_points['Pat']
            self.paire_joueurs[1][6] += match_points['Pat']
            # Update the database with the new score of each player
            updateplayersscore(self.paire_joueurs[0][0], self.paire_joueurs[0][6])
            updateplayersscore(self.paire_joueurs[1][0], self.paire_joueurs[1][6])

            return [self.paire_joueurs[0][0], match_points['Pat']], \
                   [self.paire_joueurs[1][0], match_points['Pat']]

        elif code_result == codes_results[1]:
            self.paire_joueurs[0][6] += match_points['Victory']
            self.paire_joueurs[1][6] += match_points['Defeat']
            # Update the database with the new score of each player
            updateplayersscore(self.paire_joueurs[0][0], self.paire_joueurs[0][6])
            updateplayersscore(self.paire_joueurs[1][0], self.paire_joueurs[1][6])

            return [self.paire_joueurs[0][0], match_points['Victory']], \
                   [self.paire_joueurs[1][0], match_points['Defeat']]

        else:
            self.paire_joueurs[0][6] += match_points['Defeat']
            self.paire_joueurs[1][6] += match_points['Victory']
            # Update the database with the new score of each player
            updateplayersscore(self.paire_joueurs[0][0], self.paire_joueurs[0][6])
            updateplayersscore(self.paire_joueurs[1][0], self.paire_joueurs[1][6])

            return [self.paire_joueurs[0][0], match_points['Defeat']], \
                   [self.paire_joueurs[1][0], match_points['Victory']]
