# Write a Rectangle class in Python language,
# allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle
# Create a method display() that display the length, width, perimeter and
# area of an object created using an instantiation on rectangle class.
# Create a Parallelepipede child class inheriting from the Rectangle class
# and with a height attribute and another Volume()
# method to calculate the volume of the Parallelepiped.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display(self):
        print(f"The length of the rectangle is {self.length}")
        print(f"The width of the rectangle is {self.width}")
        print(f"The perimeter of the rectangle is {self.length + self.width}")


perimeter = Rectangle(90, 80)
print(perimeter.width)
