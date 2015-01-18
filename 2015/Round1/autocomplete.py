#!/usr/bin/python

import sys

def run(filename = 'sample2.in'):
    with open(filename) as f:
        pass

if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
