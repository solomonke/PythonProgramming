# Triangle class  with three properties and two methods

class Triangle:
    def __init__(self, base, height, hypotenuse):
        self.base = base
        self.height = height
        self.hypotenuse = hypotenuse

    def area(self):
        area = (self.base / 2) * self.height
        print(area)

    def perimeter(self):
        perimeter = self.base + self.height + self.hypotenuse
        print(perimeter)


triangle_area1 = Triangle(20, 30, 40)
triangle_area1.area()

triangle_perimeter = Triangle(10, 20, 30)
triangle_perimeter.perimeter()
