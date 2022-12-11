from array import *

arr=array("i", [2,3,5,2,7 ])
print(arr)
""" for i in arr:
    print(i)

for i in range(4):
    print(i, arr[i]) """

arr.reverse()
print(arr)
arr.append(10)
print(arr)
arr.remove(2)
print(arr)
arr.remove(arr[2])
print(arr)