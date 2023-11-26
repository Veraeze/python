class Point:
    # class attribute
    color = "blue"

    def __init__(self, a, b):
        # instance/object attribute
        self.a = a
        self.b = b

    def draw(self):
        print(f"drawing from point {self.a} to point {self.b}")


point1 = Point(1, 2)
point2 = Point(5, 6)
Point.color = "red"
point1.a = 3
point1.draw()
point2.draw()
print(point1.color)
print(point2.color)
