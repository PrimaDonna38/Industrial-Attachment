""" numbers=[1,2,3,4]
first, second, third, forth= numbers
first, *others, forth= numbers
print(first, others, forth) """


letters=['a', 'b', 'c', 'd','d']
for index, letter in enumerate(letters):
    print(index, letter)

""" letters.append('f')
letters.insert(3, 'g')
print(letters)
letters.pop()
print(letters)
del letters[0:2]
print(letters)
letters.clear()
print(letters) """

if 'd' in letters:
    print(letters.count('d'))
    print(letters.index('d'))
    
