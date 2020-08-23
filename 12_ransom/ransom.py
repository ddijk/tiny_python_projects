#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-23
Purpose: Rock the Casbah
"""

import argparse
import random
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        help='Random seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip() 

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    seed = args.seed

    random.seed(args.seed)

    result=''
    for c in args.text:
        result += choose(c)

    print(result)

def choose(c):
    return c.lower() if random.choice([True, False]) else c.upper()



# --------------------------------------------------
if __name__ == '__main__':
    main()
