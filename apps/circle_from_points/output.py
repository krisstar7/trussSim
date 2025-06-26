from geom2d import Circle, Point, make_rect_centered, Vector, AffineTransform
from graphic import svg

def draw_to_svg(points: [Point], circle: Circle, config):
    svg_output = output_to_svg(circle, config['output'])
    pt_radius = circle.radius / 20
    svg_input = input_to_svg(points, pt_radius, config['input'])

    transform = AffineTransform(1, -1)

    viewbox = make_viewbox(circle)
    svg_img = svg.svg_content(
        viewbox.size, svg_output + svg_input, viewbox, transform
    )

    return(svg_img)

def output_to_svg(circle: Circle, config):
    style = style_from_config(config)
    label_style = label_style_from_config(config)

    transform = svg.affine_transform(AffineTransform(1, -1, ty=circle.center.y*2))
    attrs = label_style + [transform]
    return [
        svg.circle(circle, style),
        svg.text(
            f'0 {circle.center}',
            circle.center,
            Vector(0, 0),
            attrs
        ),
        svg.text(
            f'r = {circle.radius}',
            circle.center,
            Vector(0, 20),
            attrs
        )
    ]

def make_viewbox(circle: Circle):
    height = 2.5 * circle.radius
    width = 4 * circle.radius
    return make_rect_centered(circle.center, width, height)

def style_from_config(config):
    return [
        svg.stroke_color(config['stroke-color']),
        svg.stroke_width(config['stroke-width']),
        svg.fill_color(config['fill-color'])
    ]

def label_style_from_config(config):
    return [
        svg.font_size(config['label-size']),
        svg.font_family(config['font-family']),
        svg.fill_color(config['stroke-color'])
    ]

def input_to_svg(points: [Point], point_radius: float, config):
    style = style_from_config(config)
    label_style = label_style_from_config(config)
    [a, b, c] = points
    disp = Vector(1.25 * point_radius, 0)

    attrs = lambda point: label_style + [svg.affine_transform(AffineTransform(1, -1, ty=point.y*2))]

    return[
        svg.circle(Circle(a, point_radius), style),
        svg.circle(Circle(b, point_radius), style),
        svg.circle(Circle(c, point_radius), style),
        svg.text(f'A {a}', a, disp, attrs(a)),
        svg.text(f'B {b}', b, disp, attrs(b)),
        svg.text(f'C {c}', c, disp, attrs(c))
    ]