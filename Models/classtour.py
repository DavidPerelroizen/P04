import datetime


class Tour:
    """This class aims at modeling a round inside a tournament"""

    def __init__(self, round_name, date_time_begin=0, date_time_finish=0, matches_list=[]):
        self.round_name = round_name
        self.date_time_begin = date_time_begin
        self.date_time_finish = date_time_finish
        self.matches_list = matches_list

    def initiateround(self):
        """This function will automatically return the starting time of the round"""
        self.date_time_begin = datetime.datetime.today().replace(microsecond=0)
        return self.date_time_begin

    def addmatch(self, match_tuple):
        """This function will a match instance to the list of matches of the round"""
        self.matches_list.append(match_tuple)
        return self.matches_list

    def finishround(self):
        """This function will automatically return the starting time of the round"""
        self.date_time_finish = datetime.datetime.today().replace(microsecond=0)
        return self.date_time_finish
