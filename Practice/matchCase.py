num = int(input("Enter a number : "))

match num:
    case 12:
        print("The number is", num)
    case 50:
        print("The number is ", num)
    case _:
        print("Your entered number is ", num)

num1 = int(input("Enter next number : "))
match num1:
    case 12:
        print("The number is", num1)
    case 50:
        print("The number is ", num1)
    case _ if num1 > 12 and num1 < 60:
        print("Your entered number is greater than 12 ")
    case _ if num1 < 12:
        print("Your entered number is less than 12 ")
    case _:
        print("ENTERED NUMBER IS ", num1)
