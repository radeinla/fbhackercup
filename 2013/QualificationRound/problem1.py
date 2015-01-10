
def is_black(x):
    return x == '#'

def is_square(box, N):
    size = None
    fbj1 = None
    fbj2 = None
    fbi1 = None
    fbi2 = None

    blank = "."*N

    for i in xrange(0, N):
        for j in xrange(0, N):
            if fbj1 is None or fbj2 is None:
                if is_black(box[i][j]):
                    if fbj1 is None:
                        fbj1 = j
                        fbi1 = i
                    elif j == N-1:
                        fbj2 = j
                        fbi2 = fbi1 + fbj2 - fbj1
                else:
                    if fbj1 is not None:
                        fbj2 = j-1
                        fbi2 = fbi1 + fbj2 - fbj1
            else:
                if is_black(box[i][j]):
                    if (j < fbj1 or j > fbj2) or i - fbi1 > fbj2 - fbj1:
                        return False
                else:
                    if fbj1 <= j <= fbj2 and i - fbi1 <= fbj2 - fbj1:
                        return False
    return fbj1 is not None

with open("input1.txt") as f:
    T = int(f.readline())
    for t in xrange(0, T):
        N = int(f.readline())
        c = []
        for i in xrange(0, N):
            c.append(f.readline().rstrip('\n'))
        print "Case #%d: %s" % (t+1, 
                                "YES" if is_square(c, N) else "NO")
