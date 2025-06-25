import geom2d.tparam as tparam

def uniform_t_sequence(steps: int):
    return [t / steps for t in range(steps + 1)]

def ease_in_out_t_sequence(steps: int):
    return [east_in_out_t(t) for t in uniform_t_sequence(steps)]

def east_in_out_t(t: float):
    return t ** 2 / (t ** 2 + (1 - t) ** 2)

def interpolate(vs: float, ve: float, t: float):
    tparam.ensure_valid(t)
    return vs + t * (ve - vs)

