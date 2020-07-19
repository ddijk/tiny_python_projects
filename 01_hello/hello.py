#!/usr/bin/python3
""" Dit is mijn eerste Python module"""
import argparse


def main():
    """ Dit is mijn eerste Python functie"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                 default='World', help='Name to greet')
    args = parser.parse_args()

    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
