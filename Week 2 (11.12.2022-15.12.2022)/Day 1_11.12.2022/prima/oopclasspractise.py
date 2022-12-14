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
    
Employee_1=Employee("Prima","Donna",70000)
Employee_2=Employee("Tasmia","Raisa",70000)
Employee_3=Employee("Nazifa","Afroz",70000)

print(Employee_1.first, Employee_2.first, Employee_3.first)
print(Employee_1.fullname(), Employee_2.fullname(), Employee_3.fullname())
print(Employee_1.salary)

Employee_1.apply_raise()
print(Employee_1.salary)
print(Employee.employee_no)
print(Employee.amount_raise)

Employee.set_raise(1.06)
print(Employee_1.amount_raise)