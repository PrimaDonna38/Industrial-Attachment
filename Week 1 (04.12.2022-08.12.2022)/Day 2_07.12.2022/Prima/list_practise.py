letters= ["p", "r", "i", "m", "a"]
matrix= [[1,2], [4,5]]

# zeros= [0]*5
# concat= zeros +letters + matrix
# print(concat)

# numbers= list(range(3,5))
# print(numbers)

# char= list(" Bye bye ")
# print(char)
# print(len(char))

# letters[0]="A"
# print(letters[0:3])

numbers= list(range(20))
print(numbers[::2])
print(numbers[::-3])
first, *others, last=numbers
print(first, last)

for letter in enumerate(letters):
    print(letter)

items= (0,"a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)

letters.append("e")
letters.insert(3,"i")
letters.pop(0)
letters.remove("i")
del letters[0:2]
print(letters)

#letters.clear()
#print(letters)

print(letters.count("a"))
if "e" in letters:
    print(letters.index("e"))