from exeptions import DateError, DayError, MonthError, YearError


class Date:
    """Date validation class"""

    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def unpack(cls, date_str):
        """Date str unpack and covert to int"""
        date_list = list(filter(lambda x: x.isdigit(), date_str.split('-')))
        if len(date_list) == 3:
            return cls(*list(map(int, date_list)))
        else:
            raise DateError(f'Date error ({date_str}), date should be look like "int-int-int"')

    @staticmethod
    def validate(date_object):
        """Date validator"""
        if date_object.d > 31 or date_object.d < 1:
            raise DayError(f'Day error ({date_object.d}): day should be more or equals 1 and less or equals 31')
        if date_object.m > 12 or date_object.m < 1:
            raise DayError(f'Month error ({date_object.m}): month should be more or equals 1 and less or equals 12')
        if date_object.y <= 0:
            raise DayError(f'Year error ({date_object.y}): year should be more or equals 1')
        return date_object

    def __str__(self):
        return f'{self.d:02} day {self.m:02} month {self.y} year'


'''
Simple-tests
'''
try:
    print(Date.validate(Date.unpack('1-04-1994')))
except (DayError, DateError, MonthError, YearError) as error:
    print(error)

try:
    print(Date.validate(Date.unpack('-04-1994')))
except Exception as error:
    print(error)

try:
    print(Date.validate(Date.unpack('12-13-1994')))
except Exception as error:
    print(error)
