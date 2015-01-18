#!/usr/bin/python

import sys

def min_letters(N, words):
    # print N, words
    prefixes = set()
    v = 0
    for i in xrange(0, N):
        # print 'checking', words[i]
        found = False
        test = ""
        for j in xrange(0, len(words[i])):
            test += words[i][j]
            # print 'testing', test
            if not found and test not in prefixes:
                # print 'using', test
                v += j + 1
                found = True
            prefixes.add(test)
        if not found:
            v += len(words[i])
        # print prefixes
    return v

def run(filename = 'sample2.in'):
    with open(filename) as f:
        T = int(f.readline())
        for t in xrange(0, T):
            N = int(f.readline())
            words = [f.readline().replace('\n', '') for x in xrange(0, N)]
            print "Case #%d: %d" % (t+1, min_letters(N, words))

if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
