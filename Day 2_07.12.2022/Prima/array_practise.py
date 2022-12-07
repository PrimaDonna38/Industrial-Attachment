from array import *
arr= array('i',[-1,2,3,4,5])

print(arr)
print(arr[4])
print(arr.index(4))

for i in arr:
    print(i)

for i in range(1,4):
    print(arr[i])

for i in range(1,4):
    print(i, arr[i])

# arr.reverse()
# print(arr)

arr.append(6)
print(arr)

arr.remove(3)
print(arr)

arr1= array("i", [])
x=int(input("enter the size of array : "))
print("Enter the elements")
for i in range(x):
    n=int(input())
    arr1.append(n)
print(arr1)