import re
import json

import pkg_resources as res
from geom2d import Point

def parse_points(input):
    return (
        __point_from_string(input[0]),
        __point_from_string(input[1]),
        __point_from_string(input[2])
    )

def __point_from_string(string: str):
    matches = re.match(r'(?P<x>\d+)\s(?P<y>\d+)', string)
    return Point(
        int(matches.group('x')),
        int(matches.group('y'))
    )

def read_config():
    config = res.resource_string(__name__, 'config.json')
    return json.loads(config)

