p= {1:"Prima", 2:"Donna", 3:"Sarker"}
print(p)
print(p[2])
p[4]="Chotton"
print(p)

b=p.copy()
print(b)

print(p.values())
print(p.update())
print(p.get(3))
print(p.items())
print(p.keys())
print(p.pop(3))
print(p.popitem())
print(p.setdefault(1))

mydict= dict(key1="hello",key2="byebye")
print(mydict)

print(p.fromkeys(mydict))
print(p.clear())
