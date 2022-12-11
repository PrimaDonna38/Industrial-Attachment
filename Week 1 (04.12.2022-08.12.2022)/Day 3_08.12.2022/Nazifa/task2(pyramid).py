
star = 0

for i in range(1,6):
    for space in range(1, (5-i)+1  ):
        print(end="  ")
   
    while star!=(2*i-1):
        print("* ", end="")
        star += 1
   
    star = 0
    print()

# for i in range(5):
#     for j in range(5-i-1):
#         print(" ", end=" ")
#     for star in range((2*i)-1):
#         print("* ", end="")
#     print()
# row = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, row+1):
#     for space in range(1, (row-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
   
#     k = 0
#     print()

# rows = int(input("Enter number of rows: "))