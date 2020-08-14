#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-13
Purpose: Rock the Casbah
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    args = parser.parse_args()

    if args.adjectives < 1:
        return parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        return parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.number
    numOfadjectives = args.adjectives
    seed = args.seed

    random.seed(seed)

    numOfadjectives=['aap', 'noot','mies']
    nouns = ['a','b','c']
    # print(f'number = "{number}"')
    # print(f'adjectives = "{adjectives}"')
    # print(f'seed = "{seed}"')
    for n in range(number):
        adjectives = random.sample(numOfadjectives, number)
        noun = random.choice(nouns)
        print('You {} {}!'.format(', '.join(adjectives), noun))


# --------------------------------------------------
if __name__ == '__main__':
    main()
