# accept command line arguments

import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# ccwc -c test.txt
def parse_args():
    parser = argparse.ArgumentParser(description='CCWC')
    parser.add_argument('-c', '--bytes', type=str, help='text file')
    parser.add_argument('-l', '--lines', type=str, help='text file')
    parser.add_argument('-w', '--words', type=str, help='text file')
    parser.add_argument('-m', '--chars', type=str, help='text file')
    # there can be no argument and make it optional
    parser.add_argument('filename', nargs='?', help='text file')

    return parser.parse_args()


def bytes_count(filename):
    # return bytes of file
    with open(HERE + os.sep + filename, 'rb') as fr:
        content = fr.read()
    return len(content)

def lines(filename):
    # return lines of file
    with open(HERE + os.sep + filename, 'r') as fr:
        content = fr.readlines()
    return len(content)

def words(filename):
    # return words of file
    with open(HERE + os.sep + filename, 'r') as fr:
        content = fr.read()
    return len(content.split())

def chars(filename):
    # return chars of file
    with open(HERE + os.sep + filename, 'rb') as fr:
        content = fr.read().decode()
    return len(content)

def default_count(filename):
    return f"{lines(filename)} {words(filename)} {bytes_count(filename)}"

if __name__ == '__main__':
    args = parse_args()
    if args.bytes:
        filename = args.bytes
        r = bytes_count(filename)
    elif args.lines:
        filename = args.lines
        r = lines(filename)
    elif args.words:
        filename = args.words
        r = words(filename)
    elif args.chars:
        filename = args.chars
        r = chars(filename)
    else:
        filename = args.filename
        r = default_count(filename)
    print(r, filename)
