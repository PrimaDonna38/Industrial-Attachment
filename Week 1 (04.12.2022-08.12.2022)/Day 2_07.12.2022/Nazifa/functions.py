# def greet():
#     print("hello")
#     print("welcome")

# greet()

# def greet(first,last):
#     print("hello {first} {last}")
#     print("welcome")

# greet("nazifa","afroz")

# #return a value

# def getGreeting(name):
#     return f"hello {name}"

# message = getGreeting("Nazifaaa")
# print(message)

# def incre(number, by=1):
#     return number+by

# print(incre(2))

# def multiply(*numbers):
#     total=1
#     for number in numbers:
#         total=total*number
#     print(total)

# multiply(2,3,4,5)
# def save_user(**user):
#     print(user)

# save_user(id=1, name="nazifa", age=22)

message="a"

def usermsg(name):
    message="b"

usermsg("nazifa")
print(message)

message1="c"

def usermsg1(name):
    global message1
    message1="d"

usermsg1("nazifa")
print(message1)