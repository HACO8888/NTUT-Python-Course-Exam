import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(3)
print("Area of the circle:", circle.area())
print("Circumference of the circle:", circle.circumference())