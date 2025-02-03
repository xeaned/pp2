class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


shape = Shape()
print("Shape area:", shape.area())  
n=int(input())
square = Square(n)
print("Square area:", square.area()) 