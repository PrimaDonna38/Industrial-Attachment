list=[]
x= int(input("Enter the number of elements in the list: "))

for i in range(1,x+1):
    e= int(input("Enter elements: "))
    list.append(e)
    
#print("Largest Element in the List: ", max(list))

list.sort()
print("Largest element in the list:", (list[-1]))