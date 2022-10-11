# Modules in Python
# Sometimes called a library
# It's a python file containing python definitions and statements
# Two categories:
# 1. Ready-made modules 2. User-defined modules
# Modules use import statements. Import statements are used to call modules.

# import math
# from math import pow, sqrt, sin
# power = pow(8, 2)
# print(power)
#
# print(sqrt(600))
# print(sin(30))
#
#
# import os
#
# help(os)


# User-defined modules
# Volume of some figures

# Cuboid

def cuboid(l, w, h):
    return l * w * h

def sphere(r):
    PI = 3.142
    answer = 4/3 * PI * r**3
    return answer

def cylinder(r, h):
    PI = 3.142
    result = PI * (r**2) * h
    return result