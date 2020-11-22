#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-11-22
Purpose: Rock the Casbah
"""

import argparse
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic tac toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-b',
                        '--board',
                        help='A board',
                        metavar='board',
                        type=str,
                        default='')

    parser.add_argument('-c',
                        '--cell',
                        help='A Cell',
                        metavar='cell',
                        type=int,
                        choices=range(1,10)
                        )

    parser.add_argument('-p',
                        '--player',
                        help='A Player',
                        metavar='player',
                        type=str,
                        choices=['X','O'])
    parse_result =  parser.parse_args()

    bord=parse_result.board
    if not re.fullmatch('[OX.]{9}', parse_result.board):
        parser.error('geen  geldig bord')

    
    player = parse_result.player
    cell = parse_result.cell
    if player and cell:
        print("handle move")
    else: 
        print(format_board(bord))
        # if parse_result.cell:
            # parser.error("Must provide both --player and --cell")

    # validateBoard(parse_result.board)
    return parse_result

def  format_board(bord):
    board = []
    board.append('-'*13)
    board.append('\n|')
    for i, val in enumerate(bord, 1):
        if val == 'O' or val == 'X':
            board.append(f' {val} |')
        else: 
            board.append(f' {i} |')
        if i % 3 == 0 and i < 9:
            board.append('\n')
            board.append('-'*13)
            board.append('\n|')
        
        if i % 3 == 0 and i == 9:
            board.append('\n')
            board.append('-'*13)

    return ''.join(board)

def test_board_no_board():
    """makes default board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    assert format_board('.' * 9) == board
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = args.board
    cell = args.cell
    player = args.player

    # print(f'board = "{board}"')
    # print(f'cell = "{cell}"')
    # print(f'player = "{player}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
