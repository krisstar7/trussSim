from geom2d.point import Point
from geom2d.vector import Vector

def make_vector_between(p: Point, q: Point):
    return q - p

def make_versor(u: float, v: float):
    return Vector(u, v).normalized()

def make_versor_between(p: Point, q: Point):
    return make_vector_between(p, q).normalized()

