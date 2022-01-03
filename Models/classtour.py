import datetime


class Tour:

    def __init__(self, round_name, date_time_begin, date_time_finish, matches_list):
        self.round_name = round_name
        self.date_time_begin = date_time_begin
        self.date_time_finish = date_time_finish
        self.matches_list = matches_list

    def initiateround(self):
        self.date_time_begin = datetime.datetime.today().replace(microsecond=0)
        return self.date_time_begin

    def addmatch(self, match_tuple):
        self.matches_list.append(match_tuple)
        return self.matches_list

    def finishround(self):
        self.date_time_finish = datetime.datetime.today().replace(microsecond=0)
        return self.date_time_finish

