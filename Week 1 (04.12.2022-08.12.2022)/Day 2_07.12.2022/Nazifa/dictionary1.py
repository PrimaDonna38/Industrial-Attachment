# a={1:'nazifa', 2:'tanisha', 3:'maliha'}
# print(a[2])
# print(a.get(2))

# b=a.copy()
# print(b)

# print(a.items())

capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}
 
print(dir(capitals))
print(help(capitals))
print(capitals.get("Japan"))

if capitals.get("Russia"):
   print("That capital exists")
else:
   print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()
capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
  print(key)

values = capitals.values()
for value in capitals.values():
print(value)

items = capitals.items()
for key, value in capitals.items():
   print(f"{key}: {value}") 