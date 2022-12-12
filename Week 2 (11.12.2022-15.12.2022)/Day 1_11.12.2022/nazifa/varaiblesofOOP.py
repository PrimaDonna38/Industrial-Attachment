class Employee:

    raise_amount= 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emps +=1
    
    def fullname(self):
        return ('{} {}'.format(self.first,self.last))
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount )

emp_1= Employee('nazifa', 'Afroz', 30000)
emp_2= Employee('tazifa', 'tafroz', 15500)
print(emp_1.pay)

print(emp_1.__dict__)
# emp_1.apply_raise()
# print(emp_1.pay)
