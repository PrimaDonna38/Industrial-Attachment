from array import *
arr=array("i", [])
x=int(input("Enter the number of elements: "))
print("Enter %d elements" %x)
for i in range(x):
    n=int(input())
    arr.append(n)
print(arr)
