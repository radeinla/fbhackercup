#!/usr/bin/python

import sys

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

class Place(object):
    def __init__(self, name, popularity, visits):
        self.name = name
        self.popularity = popularity
        self.visits = visits

    def __lt__(self, other):
        return (self.visits, self.popularity) < (other.visits, other.popularity)

    def __repr__(self):
        return self.name

def simulate(S, R, K, N):
    for i in xrange(0, R):
        for j in xrange(0, N):
            S[j].visits += 1
        S = S[N:] + S[0:N]
    return S

def run(filename = 'sample1.in'):
    with open(filename) as f:
        T = int(f.readline().replace('\n', ''))
        for i in xrange(0, T):
            K, N, V = [int(n) for n in f.readline().replace('\n', '').split(' ')]
            S = [Place(f.readline().replace('\n', ''), n, 0) for n in xrange(0, K)]
            LCM = lcm(K, N)
            C = LCM/N
            R = (V) % C
            #print K, N, V, S, C, LCM, R
            S = simulate(S, R, K, N)
            print("Case #{}: {}".format(i+1, " ".join([p.name for p in sorted(S[K-N:], key=lambda x: x.popularity)])))

if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
