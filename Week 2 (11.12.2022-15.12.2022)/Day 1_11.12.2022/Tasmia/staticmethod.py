class timedate:
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

import datetime
date= datetime.date(2022,12,12)

print(timedate.is_workday(date))
