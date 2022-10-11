# Functions
# A function is a block of code that is performing a related task
# Functions are enclosed inside brackets
# Functions are in two categories
# 1. In-built functions, e.g. print(), input(), type(), int()
# 2. User-defined functions - They are created by the developer
# To create a function in Python, you start with the keyword "def"
# You then write the function name and the brackets followed by a full colon
# Any item of a function is indented. Indentation shows the members of a function.

# Let's create a function that adds two numbers

def add():
    a = 10
    b = 20
    sum = a + b
    print(sum)
# Calling a function - exit the function, then call starting with its name followed by the brackets
add()

# Create and call a function that computes the area of a circle
def area(radius):
    PI = 3.142
    circle = PI * (radius **2)
    print(circle)
area(10)

# Parameters are values passed inside a function

# def multiply(num1, num2):
#     product = num1 * num2
#     print(product)
# multiply(10, 200)

def greet(name):
    print("Hey {}".format(name))
greet("John")


# Using functions create a BMI calculator
def bmi_calculator(weight, height):
    bmi = weight / (height **2)
    print(bmi)
bmi_calculator(70, 1.72)


def maskify(secret):
    secret_word =

