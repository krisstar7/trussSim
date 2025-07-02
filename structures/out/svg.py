import json

import pkg_resources as res

from geom2d import AffineTransform
from graphic import svg
from structures.solution.structure import StructureSolution
from .bar_svg import bars_to_svg
from .load_svg import loads_to_svg
from .node_svg import nodes_to_svg
from .reaction_svg import node_reactions_to_svg

def __read_config():
    config = res.resource_string(__name__, 'config.json')
    return json.loads(config)

__expected_settings = (
    #scale
    'scale',
    #scale displacement
    'disp_scale',
    #scale load
    'load_scale',
    #draw original geometry
    'no_draw_original'
)

def __validate_settings(settings):
    for setting in __expected_settings:
        if setting not in settings:
            raise ValueError(f'"{setting}" missing in settings')

def structure_solution_to_svg(
        result: StructureSolution,
        settings,
        _config=None
):
    __validate_settings(settings)
    default_config = __read_config()

    config = {**default_config, **(_config or {})}
    
    viewbox = result.bounds_rect(
        config['sizes']['margin'],
        settings.scale
    )
    transform = AffineTransform(sx=1, sy=-1, tx=0, ty=0)

    svg_bars = bars_to_svg(result.bars, settings, config)
    svg_nodes = nodes_to_svg(result.nodes, settings, config)
    svg_react = node_reactions_to_svg(result, settings, config)
    svg_loads = loads_to_svg(result.nodes, settings, config)

    return svg.svg_content(
        size=viewbox.size,
        primitives=svg_bars + svg_nodes + svg_react + svg_loads,
        viewbox_rect=viewbox,
        transform=transform
    )








