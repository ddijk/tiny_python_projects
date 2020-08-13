#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-13
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        choices=['a','e','i','o','u'],
                        type=str,
                        default='a')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    textOrFile = args.positional


    if os.path.isfile(textOrFile):
        text = open(textOrFile).read().rstrip()
    else:
        text = textOrFile

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
