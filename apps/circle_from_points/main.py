import os
import sys

parent_path = os.path.normpath(os.path.join(os.getcwd(), '..', '..'))
sys.path.append(parent_path)

from apps.circle_from_points.input import parse_points, read_config
from geom2d import make_circle_from_points
from apps.circle_from_points.output import draw_to_svg


if __name__ == '__main__':
    input = [line.strip() for line in open('input.txt')]
    (a, b, c) = parse_points(input)
    circle = make_circle_from_points(a, b, c)
    output = draw_to_svg((a, b, c), circle, read_config())
    
    open('output.svg', 'w').write(output)

