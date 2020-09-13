#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-09-12
Purpose: Rock the Casbah
"""

import argparse

import re
from pprint import pprint
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs="*",
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    pos_arg = args.positional

    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'positional = "{pos_arg.name}"')
    # print(f'inputs = "{inputs}"')

    # text ='The quick <adjective> <noun> jumps <preposition> the lazy <noun>.'

    text = pos_arg.read().rstrip()

    # print(text)

    match = re.findall('(<([^<>]+)>)', text)

    if not match:
        print(f'"{pos_arg.name}" has no placeholders.', file=sys.stderr)
        sys.exit(1)

    # print(inputs)

    # pprint(match)

    # print('text before:'+text)
    for placeholder, name in match:
        article = "a" if name[0].lower() in 'aeoiu' else "an"
        val = inputs.pop(0) if inputs else input("Give me {} {} ".format(article, name))
        text = re.sub(placeholder, val, text, 1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
