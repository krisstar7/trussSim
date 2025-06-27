from apps.aff_transf_motion.parse_transform import parse_transform_term
from geom2d import AffineTransform
from apps.aff_transf_motion.parse_geom import *

def read_input(inputtrans, inputprim):
    transform = __read_transform(inputtrans)
    primitives = __read_primitives(inputprim)
    return transform, primitives

def __read_transform(input):
    return AffineTransform(
        sx=parse_transform_term('sx', input[0]),
        sy=parse_transform_term('sy', input[1]),
        shx=parse_transform_term('shx', input[2]),
        shy=parse_transform_term('shy', input[3]),
        tx=parse_transform_term('tx', input[4]),
        ty=parse_transform_term('ty', input[5])
    )

def __read_primitives(input):
    prims = {'circs': [], 'rects': [], 'polys': [], 'segs': []}

    for line in input:
        print(line)
        if can_parse_circle(line):
            prims['circs'].append(parse_circle(line))

        elif can_parse_rect(line):
            prims['rects'].append(parse_rect(line))

        elif can_parse_polygon(line):
            prims['polys'].append(parse_polygon(line))

        elif can_parse_segment(line):
            prims['segs'].append(parse_segment(line))

    return prims

def split_input_file(input):
    inputtrans = input[:6]
    inputprim = input[6:] 

    return inputtrans, inputprim