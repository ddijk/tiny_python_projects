#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-13
Purpose: Rock the Casbah
"""

import argparse
import os

from pprint import pprint as pp

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        choices=['a','e','i','o','u'],
                        type=str,
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    # pp(args)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text

    vowels ='aeiou'

    result=''
    for c in text:
        if c.lower() in vowels:
            result+= vowel if c.islower() else vowel.upper()
        else:
            result+=c

    print(result)




# --------------------------------------------------
if __name__ == '__main__':
    main()
