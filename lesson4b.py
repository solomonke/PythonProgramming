# Control Flow, Control Structures
# Control flow is subdivided into three categories
# 1. Sequential control flow
# This is the default flow of a program. The program execution happens line by line
# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))
# result = number1 = number2
# print("")
# print(result)

# 2. Decisional control flow also called selection control flow
# The program tests conditions. Flow of the program is based on conditions
# Decisional control flow is subdivide into four
# 1. if 2. if..else 3. elif..else 4. nested if
# They're shown using flow chart diagrams

# if statements
# num = int(input("Enter the number : "))
#
# if num >= 9:
#     print(num)
#     print("The number if greater or equal to zero")
# else:
#     print(num)
#     print("The number is negative")

# Using the modulus operator % test a number from a user input whether it is odd or even
# number % 2 == 0 even, else that number if odd

num = int(input("Enter number : "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")





