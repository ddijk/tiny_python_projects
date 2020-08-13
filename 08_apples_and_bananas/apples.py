#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-13
Purpose: Rock the Casbah
"""

import argparse


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
    text = args.positional

    # print(f'str_arg = "{str_arg}"')
    # print(f'positional = "{pos_arg}"')

    vowels ='aeiou'

    trTable= { 'a': vowel, 'e':vowel, 'i': vowel,'u': vowel, 'o': vowel}
    trText= text.translate(str.maketrans(trTable))
    print(trText)




# --------------------------------------------------
if __name__ == '__main__':
    main()
