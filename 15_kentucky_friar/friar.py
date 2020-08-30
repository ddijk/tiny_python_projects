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

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    

    args= parser.parse_args()

    if os.path.isfile(args.text):
        lines = []
        for line in open(args.text):
            lines.append(line.rstrip())

        args.text = '\n'.join(lines)
    return args

def fry(word):

    pattern1 = "([yY])(ou)([\W]["+string.ascii_letters+"]*)"
    m = re.match(pattern1, word)

    if m:
        g = m.groups()
        # print(g)
       
        if g[0] and g[1]:
            return f"{g[0]}'all"+ (g[2] if g[2] else '')

    pattern3 = "([yY])(ou)$"
    m = re.match(pattern3, word)
    if m:
        g = m.groups()
        return f"{g[0]}'all"

    pattern2 = "(["+string.ascii_letters+"]*)(ing)(\W)?"

    m = re.match(pattern2, word)
    if m:
        g = m.groups()
        # print(g)
        vowels = 'aeuoiAEUOI'
        if len(list(filter(lambda e: e in vowels, g[0]))) > 0:
            return ''.join(g[0])+"in'" + (g[2] if g[2] else '')

    return word

def test_fry():
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

    for line in args.text.splitlines():
        # print(line)
        # print(re.split('\s', line))
        print(' '.join([fry(w) for w in re.split('\s', line)]))
        



    # print(fry(text))

# --------------------------------------------------
if __name__ == '__main__':
    main()
