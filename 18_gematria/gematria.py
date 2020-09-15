#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-09-15
Purpose: Rock the Casbah
"""

import argparse

import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')


    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def calc(word):
    return str(sum([ord(c) for c in word]))

def test_calc():
    assert calc("AA") == 130
    assert calc("ddd") == 300
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    for line in args.text.splitlines():
        # print(list(map(lambda x: calc(re.sub('[^A-Za-z0-9]', '', x)), line.split())))
        print(' '.join(map(lambda x: calc(re.sub('[^A-Za-z0-9]', '', x)), line.split())))


# --------------------------------------------------
if __name__ == '__main__':
    main()
