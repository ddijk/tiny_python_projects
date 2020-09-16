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
import sys
from tabulate import tabulate

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

    args = parser.parse_args()

    if args.num <=0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filename = args.file
    seed = args.seed
    num = args.num
    easy = args.easy

    random.seed(args.seed)
    data = read_csv(filename)

    if not data: 
        sys.exit("Geen data")

    oefeningen = random.sample(data, k=num)

    combined = lambda oef: load_level(calc_number(oef), easy)
    exercises = list(map(combined, oefeningen))

    print(tabulate( exercises,  headers=('Exercise', 'Reps')))

def load_level(oef, easy):

     divider = 2 if easy else 1

     return ( oef[0], int(oef[1]/divider))


def calc_number(oef):
    """ blah """
    naam, low, high = oef

    aantal = random.randint(low, high)

    return (naam, aantal)


def read_csv(bestand):
    """ blah """

    reader = csv.DictReader(bestand, delimiter=',')

    return list(map(convert, reader))


def convert(line):
    """ blah """
    exercise, reps = line['exercise'], line['reps']

    match = re.match(r'(\d+)-(\d+)', reps)

    # default reps when no valid number is given
    if not match:
        return (exercise, 50, 100)

    return (exercise, int(match.group(1)), int(match.group(2)))


def test_read_csv():
    """ blah """
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert list(read_csv(text))  == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
