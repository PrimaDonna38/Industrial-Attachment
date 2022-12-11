weight= float(input("Enter your weight : "))
unit = input("kg or lbs? ")
if unit.upper() == "L":
    converted= weight/.45
    print("your wight in lbs : " + str(converted))
else:
    converted= weight*.45
    print("your wight in kgs : " + str(converted))
