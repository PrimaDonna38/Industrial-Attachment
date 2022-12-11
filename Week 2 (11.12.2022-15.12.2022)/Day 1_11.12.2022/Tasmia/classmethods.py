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
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount= amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp1= employee('Tasmia', 'Hasan', 30000)
emp2= employee('John', 'Smith', 40000)

emp_str1= 'Tasmia-Raisa-50000'
emp_str2= 'Kashfia-Parisa-60000'

new_emp1= employee.from_string(emp_str1)
new_emp2= employee.from_string(emp_str2)

""" employee.set_raise_amount(1.8)
print(employee.raise_amount) """

print(new_emp2.fname)