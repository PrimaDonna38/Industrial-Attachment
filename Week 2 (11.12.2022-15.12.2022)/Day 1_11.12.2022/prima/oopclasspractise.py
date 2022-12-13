class Employee:

    employee_no= 0
    amount_raise= 1.05

    def __init__(self, first, last,salary):
        self.first= first
        self.last= last
        self.salary= salary
        self.email= first+ '.'+ last+ '@company.com'
        # self.fullname=first+ ' '+last
        Employee.employee_no+=1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.salary= int(self.salary*self.amount_raise)
    @classmethod 
    def set_raise(cls, amount):
        cls.amount_raise= amount
    
    @classmethod
    def emp_str(cls, e_str):
        first, last, salary= e_str.split('-')
        return cls(first, last, salary)
    
    @staticmethod
    def is_workday(day):
        if day.weekday==4 or day.weekday==5:
            return False
        return True


Employee_1=Employee("Prima","Donna",70000)
Employee_2=Employee("Tasmia","Raisa",70000)
Employee_3=Employee("Nazifa","Afroz",70000)

emp_1='Sajid-Fahim-60000'
emp_2='Shakil-Rabbi-60000'
new_emp_1=Employee.emp_str(emp_1)

print(Employee_1.first, Employee_2.first, Employee_3.first)
print(Employee_1.fullname(), Employee_2.fullname(), Employee_3.fullname())
print(Employee_1.salary)
Employee_1.apply_raise()
print(Employee_1.salary)
print(Employee.employee_no)
print(Employee.amount_raise)
Employee.set_raise(1.06)
print(Employee_1.amount_raise)
print(new_emp_1.email)

import datetime
today= datetime.date(2022, 12, 11)
print(Employee.is_workday(today))