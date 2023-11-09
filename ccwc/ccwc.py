# accept command line arguments

import argparse
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ccwc -c test.txt
def parse_args():
    parser = argparse.ArgumentParser(description='CCWC')
    parser.add_argument('-c', '--count', type=str, help='text file')
    parser.add_argument('-l', '--line', type=str, help='text file')

    return parser.parse_args()


def count(filename):
    # return bytes of file
    with open(HERE + os.sep + filename, 'rb') as fr:
        content = fr.read()
    return len(content)

if __name__ == '__main__':
    args = parse_args()
    filename = args.count
    c = count(filename)
    print(c)

