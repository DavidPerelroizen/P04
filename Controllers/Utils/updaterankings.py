from Views.classviews import View
from Models.constants import yes_list
from Controllers.allplayersrankingupdate import allplayersrankingupdate
from Controllers.dbtournoi import serializetournoi


def updaterankings(tournoi):
    """This function consolidates the code helping to update the rankings"""
    view = View()
    user_choice_for_update = view.proposerankingupdate()
    if user_choice_for_update in yes_list:
        allplayersrankingupdate(tournoi)
        serializetournoi(tournoi)

    else:
        serializetournoi(tournoi)
