def make_round_pairs(sequence):
    length = len(sequence)
    return [(sequence[i], sequence[(i+1) % length]) for i in range(length)]
