import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    

radius = float(input("Enter radius of circle"))

circle = Circle(radius)

area = circle.calculate_area()

perimeter = circle.calculate_perimeter()

print("Area of the circle is:", area)
print("Perimeter of circle is:", perimeter)
