#
#! 1. Write a program that asks the user for a positive integer value. The program should calculate the sum of all the integers from 1 up to the number entered. For example, if the user enters 20, the loop will find the sum of 1, 2, 3, 4…20.
# limit = int(input("Enter limit upto which you want to find sum : "))

# sum = (limit * (limit + 1)) / 2

# print(f"Summation of all the numbers from 1 to {limit} is {int(sum)}.")

#! 2. Write a program that prompts the user to input a number and prints its multiplication table.

# num = int(input("Enter a number for which you want Multiplication Table : "))
# lim = (
#     int(input("Enter a number upto which multiplication table needs to be printed : "))
#     + 1
# )

# print(f"Multiplication Table of {num} --", end="\n")

# for x in range(1, lim):
#     print(f"{num} X {x} = {num * x}")

#! 3. Write a program that prompts the user to input a number and prints its factorial. The factorial of an integer n is defined as n! = 1 x 2 x 3 x ... x n; if n > 0 = 1; if n = 0 For instance, 6! can be calculated as 1 x 2 x 3 x 4 x 5 x 6.

# num = int(input("Input a number for which you want Factorial : ")) + 1

# multiplier = 1

# for x in range(1, num):
#     multiplier *= x

# print(f"Factorial of {num - 1} is {multiplier}")

#! 4. Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another.
# n1 = int(input("Enter a Number : "))
# p = int(input("Enter its Power : "))

# print(f"{n1}^{p} = {n1**p} ")

#! 5. Write a program that prompts the user to input a number and reverse its digits. For example, the reverse of 12345 is 54321; reverse of 5600 is 65.

# num = input("Enter a number : ")

# numList = list()

# for x in num:
#     numList.append(x)

# numList.reverse()

# print(int("".join(numList)))

#! 6. Write a program that asks the user to input a positive integer. Your program should find and display the sum of digits of number. For example, sum of digits of number 32518 is 3+2+5+1+8 = 19.
# sum = 0
# num = input("Enter a positive integer : ")

# for x in num:
#     sum += int(x)

# print(f"The sum of all the digits of a given positive integer is {sum}")

#! 7. A palindromic number is a number that remains the same when its digits are reversed. For example, 16461. Write a program that prompts the user to input a number and determine whether the number is palindrome or not.

# num = input("Enter a number : ")
# numList = list()

# for x in num:
#     numList.append(x)

# originalNum = int("".join(numList))
# numList.reverse()
# reversedNum = int("".join(numList))

# if originalNum == reversedNum:
#     print(f"{num} is a Palindrome.")
# else:
#     print(f"{num} is NOT a Palindrome.")

num = input("Enter a number : ")
print(num == num[::-1])

#! 8. Write a program that prompts the user to input a decimal integer and display its binary equivalent.

# integerNum = int(input("Enter an Integer : "))
# binaryNum = str(bin(integerNum)).lstrip("0b")
# print(f"Binary conversion of {integerNum} is {binaryNum}")

# # @ OR - Using recursive
# def dec2bin(x):
#     if x > 1:
#         dec2bin(x // 2)
#     print(x % 2, end="")


# decimal = int(input("Enter a decimal number:"))
# dec2bin(decimal)

#! 9. Write a program that prompts the user to input a binary number and display its  decimal equivalent.

#! 10.Write a program that prompts the user to input two numbers and display its HCF. The  Highest Common Factor (HCF) also called the Greatest Common Divisor (GCD) of two whole numbers, is the largest whole number that's a factor of both of them.
# a = int(input("Enter n1:"))
# b = int(input("Enter n2:"))
# for x in range(1, min(a, b) + 1):
#     if a % x == 0 and b % x == 0:
#         hcf = x

# print("HCF=", hcf)
#! 11.Write a program to enter the numbers till the user wants and at the end it should  display the count of positive, negative and zeros entered.
#! 12.Write a program to obtain the first 25 numbers of a Fibonacci sequence. In a Fibonacci  sequence the sum of two successive terms gives the third term.
#! Following are the first few terms of the Fibonacci sequence: 0 1 1 2 3 5 8 13 21 34 55 89...
#! 13.Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.
