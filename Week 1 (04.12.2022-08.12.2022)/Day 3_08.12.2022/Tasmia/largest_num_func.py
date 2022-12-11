def func():
    list=[]

    x=int(input("Enter the number of elements: "))
    print("Enter elements: ")

    for i in range(x):
        elements=int(input())
        list.append(elements)

    print("The largest number: " , max(list))

func()