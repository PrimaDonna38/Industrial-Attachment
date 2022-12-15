class Employee:
    @staticmethod
    def is_workday(day):
        if day.weekday==4 or day.weekday==5:
            return False
        return True

import datetime
today= datetime.date(2022, 12, 11)
print(Employee.is_workday(today))