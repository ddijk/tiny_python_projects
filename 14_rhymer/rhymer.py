#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-24
Purpose: Rock the Casbah
"""

import argparse
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to ryhme')


    return parser.parse_args()

def test_stemmer():
    """ Test stemmer """
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')

def stemmer(word):
    return ('', '')

def consonants():
    return ''.join(filter(lambda c: c not in 'aeoui', string.ascii_lowercase))

def test_consonants():
    assert consonants() == 'bcdfghjklmnpqrstvwxyz'
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.word

    pattern = '(['+consonants()+']+)(.*)'

    result = apply(pattern, text)

    print(''.join(result))

def apply(pattern, text):
    m = re.match(pattern, text)
    if not m:
        return ('', text)

    groups = m.groups()

    if not len(groups[1]):
        return groups
    else:
        return ('xx', groups[1])

# --------------------------------------------------
if __name__ == '__main__':
    main()
