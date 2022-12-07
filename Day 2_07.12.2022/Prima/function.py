#def greet():
    #print("Hi there")
    #print("Welcome Abroad")


#greet()

#def greet(first_name, last_name):
    #print(f"Hi {first_name} {last_name}")
    #print("Welcome Abroad")
    #return "..."


#print(greet("Prima Donna", "Sarker"))

#def get_greeting(name):
    #return f"Hello {name}"

#message= get_greeting("Prima Donna Sarker")
#print(message)

#def multiply(*numbers):
    #for number in numbers:
        #print(number)

#multiply(2,3,4,5,6)

#def multiply(*numbers):
    #total= 1
    #for number in numbers:
        #total*=number
    #return total

#print(multiply(2,3,4,5,6))

def multiply(**numbers):
    print(numbers)

multiply(first=1, second=2)
