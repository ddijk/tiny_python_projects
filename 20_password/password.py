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
    max_len = args.max_word_len
    min_len = args.min_word_len
    obfuscate = args.l33t
    pos_arg = args.positional

    random.seed(args.seed)

    words = set()

    def word_len(word):
        return min_len <= len(word) <= max_len

    for file_handle in pos_arg:
        for line in file_handle:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word)

    passwords = list()
    for _ in range(num):
        passwords.append(''.join(
            random.sample(sorted(map(str.title, words)), num_words)))

    for password in passwords:
        if obfuscate:
            print(l33t(password))
        else:
            print(password)


def choose(letter):
    """ randomly upper case letter """
    return letter.lower() if random.choice([True, False]) else letter.upper()


def clean(word):
    """ remove all non-letter chars """
    if not word:
        return ''

    letters = '[A-Za-z]'

    return ''.join(filter(lambda c: re.match(letters, c), word))


def l33t(text):
    """ Obfuscate chars """
    jumper = {
        'a': '@',
        'A': '4',
        'O': '0',
        't': '+',
        'E': '3',
        'I': '1',
        'S': '5'
    }

    return ''.join(map(lambda c: jumper.get(c, c),
                       ransom(text))) + random.choice(string.punctuation)


def ransom(text):
    """ Randomly uppercase letters of text """
    return ''.join([choose(c) for c in text])


# --------------------------------------------------
if __name__ == '__main__':
    main()
