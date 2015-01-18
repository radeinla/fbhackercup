#!/usr/bin/python

if __name__ == '__main__':
    # print 102

    # print 2
    # mx = 1000000
    # print ''.join(['a'] * (mx/2-1))
    # print ''.join(['a'] * (mx/2+1))
    
    print 100
    total = 0
    words = []
    i = 1
    mx = 1000000
    while total < mx:
        words.append(''.join(['a'] * i))
        total += i
        i += 1
    if total > mx:
        words[-1] = words[-1][0:total-mx]
    for i in xrange(0, 100):
        print len(words)
        for w in words:
            print w