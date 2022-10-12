# A class called square

class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        area = self.width * self.height
        print(area)
    def perimeter(self):
        perimeter = (self.width + self.height) * 2
        print(perimeter)

square1 = Square(10,10)
square1.area()

perimeter1 = Square(20,20)
perimeter1.perimeter()




