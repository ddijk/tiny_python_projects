#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-11-22
Purpose: Rock the Casbah
"""

import argparse
import re
import random

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
                        default='.........')

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

    if not re.fullmatch('[OX.]{9}', bord):
        parser.error(f'--board "{bord}" must be 9 characters of ., X, O')

    
    player = parse_result.player
    cell = parse_result.cell
    if player and cell:
        if list(bord)[cell-1] != '.':
            parser.error(f'--cell "{cell}" already taken') 
    else: 
        if player and not cell:
            parser.error("Must provide both --player and --cell")


    return parse_result

def format_board(bord):
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

def find_winner(board):
    """ return X or O"""

    if try_winner('X', board):
        return 'X'
    
    if try_winner('O', board):
        return 'O'

    return None

def try_winner(player, board):
    winning_combinations = ['123','456','789','147','258','369','159','357']

    selectedFields = ''.join(map(lambda y: str(y[0]), filter(lambda e: e[1]==player, enumerate(board, 1))))

    # print(f'selectedFields {selectedFields}')

    return player if len(list(filter(lambda winning_comb: is_match(winning_comb, selectedFields), winning_combinations)))>0 else None

def is_match(winning_combination, selectedFields):
    return all(i in selectedFields for i in winning_combination)
    # return len([i in selectedFields for i in winning_combination])==3

def test_is_match():

    assert is_match('123', '1234')

def test_try_winner():

    assert try_winner('X', 'XXXOOO...') == 'X'
    assert try_winner('O', 'XXXOOO...') == 'O'
    assert try_winner('X', '..XOXOX..') == 'X'
    assert try_winner('X', '..XO.OX..') == None
    assert try_winner('O', 'XXO...OOX') == 'O'


def test_winning():
    """test winning boards"""

    wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
            ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]

    for player in 'XO':
        other_player = 'O' if player == 'X' else 'X'

        for board in wins:
            board = board.replace('P', player)
            dots = [i for i in range(len(board)) if board[i] == '.']
            mut = random.sample(dots, k=2)
            test_board = ''.join([
                other_player if i in mut else board[i]
                for i in range(len(board))
            ])
            assert find_winner(test_board) == player

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
def test_board_with_board():
    """makes board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    assert format_board('...OXX...') == board

def main():
    """Make a jazz noise here"""

    args = get_args()
    board = args.board
    cell = args.cell
    player = args.player

    if ( cell ):
        board = processMove(board, cell, player)
        print(format_board(board))
    else:
        print(format_board(board))

    winner = find_winner(board)
    print(f'{winner} has won!') if winner else print("No winner.")
    # print(f'board = "{board}"')
    # print(f'cell = "{cell}"')
    # print(f'player = "{player}"')


def test_move():
    board = 'X.O'

    assert processMove(board,2, 'X') == 'XXO'

def processMove(bord, cel, speler):
    updatedBord = list(bord)
    updatedBord [cel-1]=speler
    return ''.join(updatedBord)
# --------------------------------------------------
if __name__ == '__main__':
    main()
