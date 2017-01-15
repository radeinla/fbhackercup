import sys
import copy

filename =  sys.argv[1] if len(sys.argv) > 1 else None

with open(filename or 'progress_pie_sample.in') as f:
    T = int(f.readline().strip())
    for t in xrange(1, T+1):
        N, M = (int(p) for p in f.readline().strip().split(' '))
        min_cost = 0
        available = [[] for i in xrange(0, N)]
        for day in xrange(0, N):
            available[day][:] = sorted([int(p) for p in f.readline().strip().split(' ')])
            picked = -1
            min_day = 1000000*N + (300**2) + 1
            for i in xrange(0, day+1):
                if len(available[i]) > 0:
                    already_picked = M-len(available[i])
                    cost = available[i][0] + (already_picked + 1)**2-(already_picked**2)
                    if cost < min_day:
                        picked = i
                        min_day = cost
            min_cost = min_cost + min_day
            available[picked] = available[picked][1:]

        best = min_cost
        print("Case #{}: {}".format(t, best))



