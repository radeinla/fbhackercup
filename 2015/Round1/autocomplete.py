#!/usr/bin/python

import sys

def min_letters_old(N, words, lens):
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

def min_letters(N, words, lens):
    letters = 0
    offsets = [[0 for y in xrange(0, N)] for x in xrange(0, N)]
    # full = [False] * N

    for i in xrange(0, N):
        # print words[i]
        offset = max(offsets[i])
        # print 'offset', offsets[i], offset
        if offset == lens[i]:
            # full[i] = True
            letters += offset
        else:
            letters += offset + 1
            for j in xrange(0, lens[i]):
                for k in xrange(i+1, N):
                    # if not full[k]:
                    if j < lens[k]:
                        if words[i][j] == words[k][j] and offsets[k][i] == j:
                            offsets[k][i] += 1
        # print offsets
    return letters

def run(filename = 'sample2.in'):
    with open(filename) as f:
        T = int(f.readline())
        for t in xrange(0, T):
            N = int(f.readline())
            words = [f.readline().replace('\n', '') for x in xrange(0, N)]
            lens = [len(word) for word in words]
            # old = min_letters_old(N, words, lens)
            new = min_letters(N, words, lens)
            # assert old == new
            # print "Case #%d: %d" % (t+1, old)
            print "Case #%d: %d" % (t+1, new)

if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
