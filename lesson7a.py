# Functions Return Statements
# Used to end the execution of the function call
# Statements after the return statements are not executed
# Used to return the result of a function after execution
# Therefore, the returned values can be stored inside another variable to be used in another program

def multiply(a, b, c):
    return a * b * c
result = multiply(10, 10, 10)
print(result)

def sum(A, B, C):
    return A + B + C


def product(D):
    return D * 2
answer = product(sum(20, 20, 30))
print(answer)

def subtraction(x, y, z):
    return x - y - z

# Modules
# Sometimes called a library
# It's a python file containing python definitions and statements
