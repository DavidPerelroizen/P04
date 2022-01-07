from Views.classviews import View
from Controllers.tournoicreator import tournoicreation
from Controllers.playersmanager import gettheplayers
from Controllers.generatepairs import generatepairs
from Models.classclassement import Classement
from Controllers.roundmanager import roundmanager


def main():
    view = View()
    user_choice = view.displaymainmenu()

    if user_choice == 'T':
        """Tournament management"""
        #  Tournament creation
        tournoi = tournoicreation()
        #  Players creation
        players_number = int(input('How many players do you want to add?: '))
        tournoi.players_list = gettheplayers(players_number)
        print("""
        
        """)
        #  Launch the rounds
        rounds_number = int(input('How many rounds do you want to play?: '))
        print("""

        """)
        for i in range(rounds_number):
            players_ranking = Classement()
            players_ranking.ranking(tournoi.players_list)
            pairs_list = generatepairs(players_ranking, tournoi.rounds_list, i)
            round_match_list = roundmanager(i, pairs_list)
            tournoi.rounds_list.append(round_match_list)
            view.displayroundresult(i)
            print("""

            """)


    else:
        """Reporting management"""
        view.displayreportingmenu()

if __name__ == '__main__':
    main()

