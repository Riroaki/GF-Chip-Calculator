import os
import re
import json
import numpy as np
from tqdm import tqdm
from itertools import combinations, product
from argparse import ArgumentParser
from queue import PriorityQueue
from data import COLORS, ATTR_UPPER_BOUND, SHAPE_M2, SHAPE_CHIP
from solve import find_solution

# Chip combination solution limit
COMBINATION_LIMIT = 100

# Combination directory
COMBINATION_PATH = 'combinations'

# Pattern: [index],[color],[count],[shape],[enhancement],[accuracy],[filling],[damage],[destruction]
CHIP_PAT = re.compile(
    '(\d+),([12]),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),1&')
ENHANCE_RANGE = range(0, 21)
COUNT_DICT = {'551': 5, '56': 6}


class Chip(object):
    """Store chip information."""

    def __init__(self, index: int, color: str, count_type: str, shape: str,
                 attrs: list):
        self.index = index
        self.color = color
        self.count = count_type
        self.shape = shape
        self.enhance = int(attrs[0])
        self.attrs = [int(item) for item in attrs[1:]]

    @property
    def data(self):
        return {
            'color': self.color,
            'name': '{}-{}'.format(self.count, self.shape),
            'enhance': self.enhance,
            'attrs': self.attrs
        }


def parse(codes: str, color_: str = None) -> dict:
    # Parse chip codes and store all information
    chip_dict = {}
    for chip_tuple in re.findall(CHIP_PAT, codes):
        index, color, count_type, shape_id, *attrs = chip_tuple
        # Leave only desired color
        if color_ is None or color == color_:
            try:
                assert int(attrs[0]) in ENHANCE_RANGE, \
                    'Invalid enhance range: {}'.format(attrs[0])
                assert sum(map(int, attrs[1:])) == COUNT_DICT[count_type], \
                    'Invalid chip attributes: {}'.format(str(attrs[1:]))
                name = '{}-{}'.format(count_type, shape_id)
                assert name in SHAPE_CHIP or name in SHAPE_M2, \
                    'Invalid shape name: {}'.format(name)
                chip = Chip(index, color, count_type, shape_id, attrs)
                chip_dict.setdefault(name, []).append(chip)
            except Exception as e:
                print(e)
    return chip_dict


def main(troop: str, fi: str, fo: str, limit: int):
    # Check arguments
    assert os.path.exists(fi)
    assert 0 < limit
    assert troop in COLORS
    # Check if solution files are ready
    if not os.path.exists(COMBINATION_PATH):
        os.mkdir(COMBINATION_PATH)
        print('Generating at most {} combinations for each troop...'.format(
            COMBINATION_LIMIT))
        find_solution(COMBINATION_PATH, COMBINATION_LIMIT)
    with open(fi, 'r') as f:
        content = f.read()
    # Parse store codes
    color = COLORS[troop]
    chip_dict = parse(content, color)
    upper_bound = np.array(ATTR_UPPER_BOUND[troop])
    with open(os.path.join(COMBINATION_PATH, '{}.json'.format(troop)),
              'r') as f:
        all_solutions = json.load(f)
    # Iterates on each combination and find best solutions
    heap = PriorityQueue()
    print('Calculating from {} valid combination sets of {}...'.format(
        len(all_solutions), troop))
    bar = tqdm(total=len(all_solutions))
    sol_idx, early_stop = 0, False
    for solution in all_solutions:
        # Check availability
        available = True
        for name, count in solution['count'].items():
            if name not in chip_dict or len(chip_dict[name]) < count:
                available = False
                break
        if available:
            # Permutations...
            candidates = []
            for name, count in solution['count'].items():
                candidates.append(list(combinations(chip_dict[name], count)))
            # Product: iterates all combinations
            for combination_list in product(*candidates):
                sol = []
                for part in combination_list:
                    sol.extend(part)
                # Calculate difference
                attrs = np.zeros(4)
                for chip in sol:
                    name = '{}-{}'.format(chip.count, chip.shape)
                    if name in SHAPE_CHIP:
                        attrs += np.array(chip.attrs) * 20
                    elif name in SHAPE_M2:
                        attrs += np.array(chip.attrs) * 18
                diff = np.abs((attrs - upper_bound)).sum()
                # Push solution into heap
                sol_data = [chip.data for chip in sol]
                # Push solution
                # Push negative value to make a maximum heap
                heap.put((-diff, -sol_idx, sol_data))
                sol_idx += 1
                # Pop out one item
                if heap.qsize() > limit:
                    _ = heap.get()
                # If all solutions now are the best ones, break
                if heap.queue[0][0] == 0:
                    early_stop = True
                    break
            if early_stop:
                print('{} top solutions found, stopped.'.format(limit))
                break
        bar.update(1)
    bar.close()
    print('Parsed {} solutions and got {} best.'.format(sol_idx + 1, limit))
    # Dump result
    with open(fo, 'w') as f:
        json.dump(heap.queue, f, indent=2, separators=(',', ':'))


if __name__ == '__main__':
    parser = ArgumentParser(
        'Simple chip calculator, able to parse store code'
        ' and calculate optimal combinations.')
    parser.add_argument('--limit', '-l', help='limit of solutions.',
                        type=int,
                        default=1000)
    parser.add_argument('--input', '-i',
                        help='name of input file containing store codes.')
    parser.add_argument('--output', '-o',
                        help='name of output file containing results.',
                        default='chips.txt')
    parser.add_argument('--type', '-t',
                        help='name of hyper fire troop, e.g.: bgm-14.')
    args = parser.parse_args()
    # Sample:
    # args = parser.parse_args(
    #     ['-l', '10', '-i', 'sample.txt', '-o', 'chip.txt', '-t', 'bgm-71'])
    main(args.type, args.input, args.output, args.limit)
