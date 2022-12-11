# for i in range(6):
#     print(i*'*')
#     i+= 1



for i in range(1,6):
    for space in range((6-i)-1):
        print(" ", end=" ")
    for asterisk in range((2*i)-1):
        print("* ", end="")
    print()