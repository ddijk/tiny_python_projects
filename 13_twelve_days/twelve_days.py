#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-23
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile (STDOUT)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    num = args.num
    if num not in range(1, 13):
        parser.error(f'--num "{num}" must be between 1 and 12')

    return args


def verse(number):
    """Create a verse"""
    ordinal = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }
    presents = """
    partridge in a pear tree.
Two turtle doves,
Three French hens,
Four calling birds,
Five gold rings,
Six geese a laying,
Seven swans a swimming,
Eight maids a milking,
Nine ladies dancing,
Ten lords a leaping,
Eleven pipers piping,
Twelve drummers drumming,
""".strip().split("\n")

    result = [
        f'On the {ordinal[number]} day of Christmas,',
        'My true love gave to me,'
    ]

    prefix = ''
    for i in reversed(range(1, number + 1)):
        if number == 1:
            prefix = 'A '
        elif i == 1:
            prefix = 'And a '
        else:
            pass
        result.append(prefix + presents[i - 1])

    return "\n".join(result)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num = args.num

    print('\n\n'.join(map(verse, range(1, num + 1))), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
