#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args

def verse(num_of_bottles):
    """bottle verse"""
    b = "bottle" if num_of_bottles == 1 else "bottles"

    if num_of_bottles==1:
        last = "No more bottles" 
    elif num_of_bottles==2:
        last = "1 bottle"
    else:
        last = f'{num_of_bottles-1} bottles'

    return '\n'.join([
        f'{num_of_bottles} {b} of beer on the wall,', f'{num_of_bottles} {b} of beer,',
        'Take one down, pass it around,',
        f'{last} of beer on the wall!'
    ])

def test_verse():
    """Test verse"""

    one = verse(1)
    assert one == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two = verse(2)
    assert two == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])

    three = verse(3)
    assert three == '\n'.join([
        '3 bottles of beer on the wall,', '3 bottles of beer,',
        'Take one down, pass it around,', '2 bottles of beer on the wall!'
    ])

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.num

    for i in range(number, 0, -1):
        print(verse(i))
        if i > 1: print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
