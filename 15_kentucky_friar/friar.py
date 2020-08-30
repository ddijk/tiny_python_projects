#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-28
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        lines = []
        for line in open(args.text):
            lines.append(line.rstrip())

        args.text = '\n'.join(lines)
    return args


def fry(word):
    """ Convert some words to Kentucky slang"""

    pattern1 = r"([yY])(ou)([\W][" + string.ascii_letters + "]*)"
    match = re.match(pattern1, word)

    if match:
        groups = match.groups()

        if groups[0] and groups[1]:
            return f"{groups[0]}'all" + (groups[2] if groups[2] else '')

    pattern3 = "([yY])(ou)$"
    match = re.match(pattern3, word)
    if match:
        groups = match.groups()
        return f"{groups[0]}'all"

    pattern2 = "([" + string.ascii_letters + r"]*)(ing)(\W)?"

    match = re.match(pattern2, word)
    if match:
        groups = match.groups()
        vowels = 'aeuoiAEUOI'
        if len(list(filter(lambda e: e in vowels, groups[0]))) > 0:
            return ''.join(groups[0]) + "in'" + (groups[2] if groups[2] else '')

    return word


def test_fry():
    """ Test the fry function """
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    for line in text.splitlines():
        print(' '.join([fry(w) for w in re.split(r'\s', line)]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
