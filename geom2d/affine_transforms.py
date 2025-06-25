import math

from geom2d.affine_transf import AffineTransform
from geom2d.point import Point
from geom2d.interpolation import ease_in_out_t_sequence, interpolate

def make_scale(sx: float, sy: float, center = Point(0, 0)):
    return AffineTransform(
        sx = sx,
        sy = sy,
        tx = center.x * (1.0 - sx),
        ty = center.y * (1.0 - sy)
    )

def make_rotation(radians: float, center = Point(0, 0)):
    cos = math.cos(radians)
    sin = math.sin(radians)
    one_minus_cos = 1.0 - cos

    return AffineTransform(
        sx = cos,
        sy = cos,
        tx = center.x * one_minus_cos + center.y * sin,
        ty = center.y * one_minus_cos - center.x * sin,
        shx = -sin,
        shy = sin
    )

def ease_in_out_t_interpolation(start, end, steps):
    t_seq = ease_in_out_t_sequence(steps)
    return [__interpolated(start, end, t) for t in t_seq]

def __interpolated(s: AffineTransform, e: AffineTransform, t):
    return AffineTransform(
        sx = interpolate(s.sx, e.sx, t),
        sy = interpolate(s.sy, e.sy, t),
        tx = interpolate(s.tx, e.tx, t),
        ty = interpolate(s.ty, e.ty, t),
        shx = interpolate(s.shx, e.shx, t),
        shy = interpolate(s.shy, e.shy, t)
    )


