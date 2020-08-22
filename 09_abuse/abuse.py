#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-08-13
Purpose: Rock the Casbah
"""

import argparse
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    args = parser.parse_args()

    if args.adjectives < 1:
        return parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        return parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.number
    numOfadjectives = args.adjectives
    seed = args.seed

    random.seed(seed)

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    assert len(adjectives) == 36

    assert len(nouns) == 39

    for _ in range(number):
        adj= random.sample(adjectives, numOfadjectives)
        noun = random.choice(nouns)
        a = ", ".join(adj)
        print(f'You {a} {noun}!')

    # for _ in range(args.number):
        # adjs = ', '.join(random.sample(adjectives, k=args.adjectives))
        # print(f'You {adjs} {random.choice(nouns)}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
