class Employee:
    employee_no= 0
    def __init__(self, first, last,salary):
        self.first= first
        self.last= last
        self.salary= salary
        self.email= first+ '.'+ last+ '@company.com'
        Employee.employee_no+=1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.salary= int(self.salary*self.amount_raise)
    
    @classmethod
    def emp_str(cls, e_str):
        first, last, salary= e_str.split('-')
        return cls(first, last, salary)

emp_1='Sajid-Fahim-60000'
emp_2='Shakil-Rabbi-60000'
new_emp_1=Employee.emp_str(emp_1)

print(new_emp_1.email)