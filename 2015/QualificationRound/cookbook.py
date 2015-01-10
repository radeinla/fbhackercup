#!/usr/bin/python

import sys

def idigits(digits):
    i = 0
    for d in digits:
        i = (i * 10) + d
    return i

def swap(digits, i, j):
    swapped = list(digits)
    swapped[i], swapped[j] = swapped[j], swapped[i]
    return idigits(swapped)
    # swapped = []
    # for x, d in enumerate(digits):
    #     if x == i:
    #         swapped.append(digits[j])
    #     elif x == j:
    #         swapped.append(digits[i])
    #     else:
    #         swapped.append(d)
    # return idigits(swapped)

def get_min(digits):
    # min_value = []
    # sorted_digits = sorted(set(digits))
    # for i, d in enumerate(digits):
    #     for j, d2 in enumerate(digits[i+1:]):
    #         if d2 == sorted_digits[0]:

    #latest
    # L = len(digits)
    # mapping = zip(digits, xrange(0, L))
    # sorted_mapping = sorted(mapping, key=lambda x: x[0] * 10 + x[1])
    # for d, i in sorted_mapping:
    #     # try largest digits
    #     for j in xrange(L-1, i, -1):
    #         if d == 0:
    #             if sorted_mapping[j][0] > d and j != 0:

        # for j in xrange(len(sorted_mapping)-1, i, -1):
        #     if d == 0:
        #         if sorted_mapping[j][0] > d and j != 0:
        #             return swap(digits, i, j)
        #     else:
        #         if sorted_mapping[j][0] > d:

    # 9115999555    
    # print mapping
    # print sorted_mapping
    # min_value = digits[0]
    # min_value_i = 0
    # max_value = digits[0]
    # max_value_i = 0
    # for i, d in enumerate(digits):
    #     if min_value < d:
    #         min_value = d
    #         min_value_i = i
    #     if max_value > d:
    #         max_value = d
    #         max_value_i = i

    return digits

    # for d in digits:
    #     if d == 1:
    #         return digits
    #     for d2 in di
    # return "".join(min_value)

def get_max(digits):
    return None

def run(filename = 'sample1.in'):
    with open(filename) as f:
        T = int(f.readline())
        for t in xrange(T):
            digits = [int(x) for x in f.readline().replace('\n', '')]
            L = len(digits)
            combis = set()
            combis.add(idigits(digits))
            for i in xrange(0, L):
                for j in xrange(i+1, L):
                    if i == 0 and digits[j] == 0:
                        continue
                    else:
                        combis.add(swap(digits, i, j))
            S = sorted(combis)
            print "Case #%d: %s %s" % (t+1, S[0], S[-1])


if __name__ == '__main__':
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
