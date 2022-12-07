weight=int(input("Enter your weight: "))
unit=input("L(pounds) or K(kilograms? ")
if(unit.upper()== "K"):
    converted=weight/0.45
    print("weight in pound: " + str(converted))
else:
    converted=weight*0.45
    print("weight in kilogram: " + str(converted))


