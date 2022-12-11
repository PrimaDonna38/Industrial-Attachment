a1= (5,3,6,7,2,3,1)
print(a1)

a2= 10,2,4
print(a2)

print(a1[2])
print(a1[-2])

print(a1[3:5])

b=(1,3,4,5,[5,6,7])
b[4][2]=3
c=a1+b
print(c)
# del c
# print(c) 

print(a1.count(3))
print(a1.index(3))

d=[1,2,3]
e=tuple(d)
print(e)

for i in a1:
    print(i)

print(9 in a1)
