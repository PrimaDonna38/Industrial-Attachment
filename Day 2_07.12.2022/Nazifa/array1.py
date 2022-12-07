from array import *
arr = array('i', [1,2,3,4])
# print(arr)
# # print(arr[3])

# for i in arr:
#     print(i)

for i in range(4):
    print( arr[i])
print("after removing")

arr.remove(arr[1])
for i in arr:
    print(i)


# arr1= array("i", [])
# x=int(input("enter the size of array : "))
# print("Enter the elements")
# for i in range(x):
#     n=int(input())
#     arr1.append(n)
# print(arr1)
