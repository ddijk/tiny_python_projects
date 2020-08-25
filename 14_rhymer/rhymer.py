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

    pattern = '(['+consonants()+']+)?(.*)?'

    groups =  re.match(pattern, text.lower()).groups()

    if groups[1]:
        printRhymeWords(groups[0], groups[1])
    else:
        first=groups[0] or ''
        print(f'Cannot rhyme "{args.word}"')


def printRhymeWords(leading_consonants, rest):

    replacements="""
    bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st
sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr
  """.strip().split(" ")
   
    replacements.extend(list(consonants()))

    sorted_list = sorted(replacements)

    [print(c+rest) for c in sorted_list if c != leading_consonants]
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
