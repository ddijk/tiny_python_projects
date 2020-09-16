#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-09-15
Purpose: Rock the Casbah
"""

import argparse
import re
import io
import random
import csv

from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Half the reps',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filename = args.file
    seed = args.seed
    num = args.num
    easy = args.easy

    random.seed(seed)
    oefeningen = read_csv(filename)

    exercises = list(map(calc_number, oefeningen))

    if easy:
        exercises = list(map(lambda e: (e[0], int(e[1] / 2)), exercises))

    pprint(random.sample(exercises, k=num))


def calc_number(oef):
    """ blah """
    naam, low, high = oef

    aantal = random.randint(low, high)

    return (naam, aantal)


def read_csv(bestand):
    """ blah """

    reader = csv.DictReader(bestand, delimiter=',')

    return map(convert, reader)


def convert(line):
    """ blah """
    # pprint(line)
    exercise, reps = line['exercise'], line['reps']

    match = re.match(r'(\d+)-(\d+)', reps)

    return (exercise, int(match.group(1)), int(match.group(2)))


def test_read_csv():
    """ blah """
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert list(read_csv(text))  == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
