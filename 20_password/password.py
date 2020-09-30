#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-09-16
Purpose: Rock the Casbah
"""

import argparse

# from ransom import choose
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None,
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_words = args.num_words
    num = args.num
    max = args.max_word_len
    min = args.min_word_len
    obfuscate = args.l33t
    pos_arg = args.positional
    seed = args.seed

    random.seed(seed)

    words = set()

    def word_len(word):
        return min <= len(word) <= max

    for fh in pos_arg:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word)

    passwords = list()
    for _ in range(num):
        passwords.append(''.join(random.sample(sorted(map(str.title, words)), num_words)))

    for pw in passwords:
         print(l33t(pw)) if obfuscate else print(pw)

def choose(c):
    return c.lower() if random.choice([True, False]) else c.upper()

def clean(word):
    if not word:
         return ''

    letters = '[A-Za-z]'

    return ''.join(filter(lambda c: re.match(letters, c), word))

def l33t(text):
    jumper = { 'a' : '@', 'A' : '4', 'O' : '0', 't' : '+', 'E' : '3', 'I' : '1', 'S' : '5'}

    return ''.join(map(lambda c: jumper.get(c,c), ransom(text)))+random.choice(string.punctuation)

def ransom(text):
    return ''.join([choose(c) for c in text])

# --------------------------------------------------
if __name__ == '__main__':
    main()
