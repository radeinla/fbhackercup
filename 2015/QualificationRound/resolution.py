#!/usr/bin/python

import sys

def done(G):
    for i in G:
        if i < 0:
            return False, False
        if i > 0:
            return False, True
    return True, True

def consume(G, F):
    return (G[0]-F[0], G[1]-F[1], G[2]-F[2])

def is_possible(GS, N, F, i):
    if i == N:
        return 'no'
    if not GS:
        return 'no'
    NGS = set()
    for G in GS:
        d, v = done(G)
        if d:
            return 'yes'
        elif v:
            NGS.add(G)
            NG = consume(G, F[i])
            d, v = done(NG)
            if d:
                return 'yes'
            elif v:
                NGS.add(NG)
    return is_possible(NGS, N, F, i+1)

def run(filename="sample2.in"):
    with open(filename) as f:
        T = int(f.readline())
        for t in xrange(0, T):
            G = tuple([int(x) for x in f.readline().split(" ")])
            N = int(f.readline())
            F = []
            for n in xrange(0, N):
                F.append(tuple([int(x) for x in f.readline().split(" ")]))
            print "Case %d: %s" % (t+1, is_possible([G], N, F, 0))

if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
