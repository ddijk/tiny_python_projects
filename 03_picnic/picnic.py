#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-07-21
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sorted = args.sorted
    pos_arg = args.positional

    if sorted:
        pos_arg.sort()

    formatItems(pos_arg)

def formatItems(items):
    if len(items) == 1:
         print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
         print(f'You are bringing {items[0]} and {items[1]}.')
    else:
         firstFew = ", ".join(items[:-1])
         print(f'You are bringing {firstFew}, and {items[-1]}.')
# --------------------------------------------------
if __name__ == '__main__':
    main()
