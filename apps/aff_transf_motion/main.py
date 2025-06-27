import os
import sys

parent_path = os.path.normpath(os.path.join(os.getcwd(), '..', '..'))
sys.path.append(parent_path)

from apps.aff_transf_motion.input import read_input, split_input_file
from apps.aff_transf_motion.config import read_config
from apps.aff_transf_motion.simulation import simulate

if __name__ == '__main__':
    input = [line.strip() for line in open('input.txt')]
    inputtrans, inputprim = split_input_file(input)

    (transform, primitives) = read_input(inputtrans, inputprim)
    config = read_config()
    simulate(transform, primitives, config)
