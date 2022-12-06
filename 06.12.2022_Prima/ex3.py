#Exercise 3
weight= int(input("Weight: "))
measure= input("(K)g or (L)bs: ")
if measure == "L" or measure=="l":
    convert= weight*.45
    print("Weight in kgs:" + str(convert))
elif measure=="K" or measure=="k":
    convert= weight/0.45
    print("Weight in lbs: " + str(convert))
