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
            lines.append(line.strip())

        args.text = '\n'.join(lines)
    return args

def fry(word):
    pattern1 = '([yY])(ou)([\W]*$)'
    m = re.match(pattern1, word)



    if m:
        g = m.groups()
        if g[0] and g[1]:
            return f"{g[0]}'all"

    vowels = 'aeuoiAEUOI'
    consonants = ''.join(filter(lambda e: e not in vowels, string.ascii_letters))
    pattern2 = "(["+consonants+"]*)(["+vowels+"]+)[^'](["+consonants+"]*)(ing)(\W)?"

    m = re.match(pattern2, word)
    if m:
        g = m.groups()
        print(g)
        if g[4]:
            end = g[4]
        else:
            end =''
        if g[1]:
           return ''.join(g[:3])+"in'" + end

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
        print(' '.join([fry(w) for w in line.split()]))
        



    # print(fry(text))

# --------------------------------------------------
if __name__ == '__main__':
    main()
