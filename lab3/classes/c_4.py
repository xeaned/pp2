import math

class Point:
    def __init__(self, x_a=0, y_a=0, x_b=0, y_b=0):
        self.x_a = x_a
        self.y_a = y_a
        self.x_b = x_b
        self.y_b = y_b

    def get_coord(self):
        self.x_a = int(input("x_a coordinate: "))
        self.y_a = int(input("y_a coordinate: "))
        self.x_b = int(input("x_b coordinate: "))
        self.y_b = int(input("y_b coordinate: "))

    def show(self):
        print(f"Point A coordinates: ({self.x_a}, {self.y_a})")
        print(f"Point B coordinates: ({self.x_b}, {self.y_b})")

    def move(self, dx_a, dy_a, dx_b, dy_b):
        self.x_a += dx_a
        self.y_a += dy_a
        self.x_b += dx_b
        self.y_b += dy_b
        print(f"Moved Point A to: ({self.x_a}, {self.y_a})")
        print(f"Moved Point B to: ({self.x_b}, {self.y_b})")

    def dist(self):
        distance = math.sqrt(((self.x_b - self.x_a) ** 2) + ((self.y_b - self.y_a) ** 2))
        print(f"The distance between Point A and Point B is: {distance}")


my_obj = Point()
my_obj.get_coord()
my_obj.show()
my_obj.move(1, 3, -1, 4)  
my_obj.dist()