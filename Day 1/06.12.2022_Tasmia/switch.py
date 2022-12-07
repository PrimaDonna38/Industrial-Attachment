language = input("Enter the programming language: ")
match language:
    case "JavaScript":
        print("Web developer")
    case "Python":
        print("Data Scientist")
    case "PHP":
        print("Backend developer")
    case "Solidity":
        print("Blockchain developer")
    case "Java":
        print("Mobile app developer")
    case _:
        print("The language doesn't matter")