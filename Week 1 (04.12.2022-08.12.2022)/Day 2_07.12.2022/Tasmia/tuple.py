a=(1,2,3,4)
b=(5,6,5,[2,3,4],7)
c= a+b
print(c)
b[3][1]=5
print(b)

del c

d=1,1,1,1,1,3,4,2,1
print(d.count(1))
print(d.index(2))
print(1 in d)
print(5 in d)

p=[1,2,3]
q=tuple(p)
print(q)
for i in q:
    print(i)