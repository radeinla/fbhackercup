#!/usr/bin/python

import math
import sys
import time

DEBUG = False

def seive_erathosthenes(N):
    factors = [set() for x in xrange(0, N+2)]
    primes = [True] * (N+1)
    primes[0] = False
    primes[1] = False
    for i in xrange(2, int(math.sqrt(N))+1):
        if primes[i]:
            factors[i].add(i)
            for j in xrange(2*i, N+1, i):
                primes[j] = False
                if factors[j] is None:
                    factors[j].add(i)
                else:
                    factors[j].add(i)
    if DEBUG:
        for i in xrange(0, 100):
            print '%d %s %s' % (i, primes[i], factors[i]) 
    return primes, factors

def primacity(A, B, K, cache):
    count = 0
    for i in xrange(A, B+1):
        if len(cache[1][i]) == K:
            count += 1
    return count

def run(filename = 'sample1.in'):
    start = time.time()
    cache = seive_erathosthenes(10**7)
    if DEBUG:
        print 'elapsed: %f' % (time.time()-start)
    with open(filename) as f:
        T = int(f.readline())
        for t in xrange(0, T):
            A, B, K = [int(i) for i in f.readline().split(' ')]
            print "Case #%d: %d" % (t+1, primacity(A, B, K, cache))
    if DEBUG:
        print 'elapsed full: %f' % (time.time()-start)

if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
