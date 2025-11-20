class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

rectangle = Rectangle(4, 5)
print("Area of the rectangle:", rectangle.area())
print("Perimeter of the rectangle:", rectangle.perimeter())
print("Is the rectangle a square?", rectangle.is_square())