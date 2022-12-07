
def fizz_buzz(number):
    if((number%3)==0 and (number%5)!=0):
        print("Fizz")
    elif((number%5)==0 and (number%3)!=0):
        print("buzz")
    elif((number%15)==0):
        print("fizzbuzz")
    else:
        print(number)

fizz_buzz(5)