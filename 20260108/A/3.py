import math


class Shape:
    def area(self):
        pass

    def __gt__(self, other):
        return self.area() > other.area()


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def read_shapes(filename):
    shapes = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if parts[0] == "C":
                radius = float(parts[1])
                shapes.append(Circle(radius))
            elif parts[0] == "R":
                width = float(parts[1])
                height = float(parts[2])
                shapes.append(Rectangle(width, height))

    return shapes


def sort_shapes(shapes):
    return sorted(shapes, reverse=True)


def generate_report(shapes, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=== 圖形面積排序報告 ===\n")
        for i, s in enumerate(shapes, 1):
            area = s.area()

            if isinstance(s, Circle):
                name = f"圓形 (半徑: {s.radius})"
                perimeter = 2 * math.pi * s.radius
            else:
                name = f"長方形 ({s.width} x {s.height})"
                perimeter = 2 * (s.width + s.height)

            file.write(f"{i}. {name} | 面積: {area:.2f} | 周長: {perimeter:.2f}\n")


if __name__ == "__main__":
    shapes = read_shapes("shapes.txt")
    sorted_shapes = sort_shapes(shapes)
    generate_report(sorted_shapes, "sorted_shapes.txt")
