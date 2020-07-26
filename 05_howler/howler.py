#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-07-26
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='STR',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='A writable filename',
                        type=str,
                        metavar='str',
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.input
    file_arg = args.outfile

#    print(f'positional = "{pos_arg}"')
#    print(f'outfile file = "{file_arg}"')

    if os.path.isfile(pos_arg):
        output_text = open(pos_arg).read().rstrip().upper()
    else:
        output_text= pos_arg.upper()

    if len(file_arg) == 0:
        print(f'{output_text}')
    else:
        fh = open(file_arg, "wt")
        fh.write(output_text)
        fh.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()
