#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-15
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()
    if ( os.path.isfile(args.text)):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    mutations = args.mutations
    seed = args.seed
    text = args.text


    random.seed(seed)

    num_of_changes = round(len(text)*mutations)

    # replacements = string.ascii_lowercase + string.punctuation
    replacements = ''.join(sorted(string.ascii_letters + string.punctuation))

    # print(f'number of changes {num_of_changes}')
    print(f'You said: "{args.text}"')


    result = text
    for i in random.sample(range(len(text)), num_of_changes):
        # print(f'waarde {i}')
        new_char = random.choice(replacements.replace(result[i], ''))
        result = ''.join([result[0:i], new_char, result[i+1:]])

    print(f'I heard : "{result}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
