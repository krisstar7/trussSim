import unittest

from geom2d.point import Point

class TestPoint(unittest.TestCase):
    def test_distance_to(self):
        p = Point(1, 2)
        q = Point(4, 6)
        expected = 5
        actual = p.distance_to(q)
        self.assertAlmostEqual(expected, actual)

    