import math

from geom2d.nums import are_close_enough
from geom2d.point import Point
from geom2d.polygon import Polygon

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def contains_point(self, point: Point):
        return point.distance_to(self.center) < self.radius
    
    def to_polygon(self, divisions: int):
        angle_delta = 2 * math.pi / divisions
        return Polygon(
            [self.__point__at_angle(angle_delta * i)
            for i in range(divisions)]
        )
    
    def __point__at_angle(self, angle: float):
        return Point(
            self.center.x + self.radius * math.cos(angle),
            self.center.y + self.radius * math.sin(angle)
        )
    
    def __eq__(self, other):
        if self is other:
            return True
        
        if not isinstance(other, Circle):
            return False
        
        return self.center == other.center and are_close_enough(self.radius, other.radius)
    
    def __str__(self):
        return f'circle c = {self.center}, r = {self.radius}'
    
    