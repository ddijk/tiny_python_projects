#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-07-31
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs="*",
                        type=argparse.FileType('r'),
                        default='[sys.stdin]')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    files = args.files

    totalLines =0
    totalWords =0
    totalChars =0
    for fh in files:
        numOfLines = 0
        numOfWords = 0
        numOfChars = 0
        # naam ='<stdin>'
        if os.path.isfile(fh):
            naam = fh.name
        else:
            naam = 'bull'
        for line in fh:
            [numW, numCh] = processLine(line, numOfWords, numOfChars)
            numOfWords += numW
            numOfChars += numCh
            numOfLines += 1
        print('{:8}{:8}{:8} {}'.format(numOfLines, numOfWords, numOfChars, naam))
        totalLines += numOfLines
        totalWords += numOfWords
        totalChars += numOfChars

    if len(files) > 1:
        print('{:8}{:8}{:8} total'.format(totalLines, totalWords, totalChars))


def processLine(line, wordsList, charsList):
    words = line.split()
    return [len(words), len(line)]

#    print(f'Aantal woorden is {len(words)}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
