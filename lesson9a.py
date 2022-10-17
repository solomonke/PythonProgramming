# Object-Oriented programming (inheritance)

# Python for Databases
# Python for file management
# Advanced functions (MPesa, random number generator, SMS applications, Emails)
# Python for cybersecurity (encryption)
#GUI applications

# Libraries in data science for Python
# numpy, pandas, matplotlib(pyplot),sklearn libraries

# OOP --> made up of classes and objects
# A class is a blueprint  of an object
# Object is an instance of a class

# Inheritance

class Fish:
    def __init__(self, color, size, location):
        self.color = color
        self.size = size
        self.location = location

    def name(self, name):
        print("The fish Species is {}".format(name))
        return name

    def details(self):
        print(f"The fish color is {self.color}, size is {self.size}, and its located in {self.location}")


tilapia = Fish("Grey", "medium", "Lake Naivasha")
tilapia.details()


# The concept of inheritance --> concept where one class takes the properties and methods of another class
# Child class inherits the parent class

class Tilapia(Fish):
    Fish.__init__('Grey', 'Bigger', 'Lake Victoria')
    pass


tilapia2 = Tilapia()

tilapia2.name("Tilapia2")
tilapia2.details()
