class employee:
    num_of_emp=0
    raise_amount=1.5

    def __init__ (self, first, last, pay):
        self.fname= first
        self.lname= last
        self.pay= pay
        self.email= first + '.' + last + '@company.com'

        employee.num_of_emp+= 1

    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
    def apply_raise(self):
        self.pay= int(self.pay * self.raise_amount)
    

emp1= employee('Tasmia', 'Hasan', 30000)
emp2= employee('John', 'Smith', 40000)
emp1.raise_amount= 1.7

print(employee.num_of_emp)

print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

""" print(emp1.fullname())
print(employee.fullname(emp2))

print(emp2.pay)
 """