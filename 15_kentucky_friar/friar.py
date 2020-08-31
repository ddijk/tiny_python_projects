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

    ing = re.match('(.*)ing$', word)

    if ing:
        if re.search('[aouie]', ing.group(1), re.IGNORECASE):
            return ing.group(1)+"in'"
    
    you = re.match('([yY])ou$', word)

    if you:
        return you.group(1)+"'all"

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
        print(''.join([fry(w) for w in re.split(r'(\W+)', line)]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
