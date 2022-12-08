from datetime import date


class CheckRent:
    def __get__(self, obj, objtype=None):
        return obj.rent_end_date.day - date.today().day == 0
