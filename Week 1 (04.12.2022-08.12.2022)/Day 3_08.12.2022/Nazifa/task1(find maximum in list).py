
# list = []

# x = int(input("Enter number of elements in list: "))
# for i in range(x):
#     n = int(input("Enter elements: "))
#     list.append(n)

# maximum= max(list)
     
# print("Largest element in the list:", maximum)

def myfunc():
    list = []
    x = int(input("Enter number of elements in list: "))
    for i in range(x):
        n = int(input("Enter elements: "))
        list.append(n)
    maximum= max(list)
    print("Largest element in the list:", maximum)

myfunc()

