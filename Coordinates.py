import math


class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
        x = Point()
        y = Point()

    def get_distance(self, distance):
        if isinstance(distance, Point):
            distance = math.sqrt((self.x) ** 2 + (self.y) ** 2)
            print(distance)
        else:
            print('Передана не точка')

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
p1.get_distance(10)


