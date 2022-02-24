class MyFirstClass:
    pass


# create empty object of a class
a = MyFirstClass()
b = MyFirstClass()

print(a)


# adding attributes for a class
class Point:
    pass


p1 = Point()
p2 = Point()

p1.x = 5
p2.y = 4

print(p1.x, p2.y)
"""
Making it do something

"""


class Point:

    def reset(self):
        self.x = 0
        self.y = 0


p = Point()
p.reset()
print(p.x, p.y)


"""
More Arguments adn docstrings
"""

import math


class Point:
    """
        Represents a point in two-dimensional geometric coordinates
        >>> p_0 = Point()
        >>> p_1 = Point(3, 4)
        >>> p_0.calculate_distance(p_1)
        5.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize the position of a new point. The x and y
        Objects in Python
        
        coordinates can be specified. If they are not, the
        point defaults to the origin.

        :param x: float x-coordinate
        :param y: float x-coordinate
        """
        self.move(x, y)


    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance from this point 
        to a second point passed as a parameter.

        :param other: Point instance
        :return: float distance
        """

        return math.hypot(self.x - other.x, self.y - other.y)


point1 = Point()
point2 = Point()
print(point1.reset())
print(point2.move(5, 0))
print(point2.calculate_distance(point1))
