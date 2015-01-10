#!/usr/bin/python

import sys

TURRET_MODES = ['<', '^', '>', 'v']
TURRET_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def valid_move(X, Y, M, N, MAP):
    if X < 0 or X >= M:
        return False
    if Y < 0 or Y >= N:
        return False
    if MAP[X][Y] in TURRET_MODES:
        return False
    if MAP[X][Y] == '#':
        return False
    return True

def toasted(NP, t, LASER_PATHS):
    return NP not in LASER_PATHS[t % 4]

def visualize(P, t, M, N, MAP, TURRETS, LASER_PATHS):
    print 'visualizing', P
    kill_paths = LASER_PATHS[t%4]
    for X in xrange(0, M):
        line = []
        for Y in xrange(0, N):
            if (X, Y) == P and (X, Y) in kill_paths:
                line.append('O')
            elif (X, Y) == P:
                line.append('X')
            elif (X, Y) in kill_paths:
                line.append('*')
            elif (X, Y) in TURRETS:
                line.append(TURRET_MODES[(TURRETS[(X,Y)]+t)%4])
            else:
                line.append('.')
        print ''.join(line)

def min_steps(M, N, MAP, G, TURRETS, LASER_PATHS, P, t, visited, current_min, cache):
    if P == G:
        return t
    if (P[0], P[1], t, t%4) in cache:
        return cache[(P[0], P[1], t, t%4)]
    if (P[0], P[1], t%4) in visited:
        return -1
    if current_min != -1:
        if t > current_min:
            return -1
    visited.append((P[0], P[1], t%4))
    for move in MOVES:
        NP = (P[0] + move[0], P[1] + move[1])
        # visualize(NP, t, M, N, MAP, TURRETS, LASER_PATHS)
        is_valid = valid_move(NP[0], NP[1], M, N, MAP)
        is_toasted = NP in LASER_PATHS[t%4]
        if is_valid and not is_toasted:
            move_min = min_steps(M, N, MAP, G, TURRETS, LASER_PATHS, NP, t+1, visited, current_min, cache)
            if move_min != -1:
                if current_min == -1:
                    current_min = move_min
                else:
                    current_min = min(current_min, move_min)
    cache[(P[0], P[1], t, t%4)] = current_min
    visited.pop()
    return current_min

def laser_path(T, mode, M, N, MAP):
    TX, TY = T[0], T[1]
    turret_dir = TURRET_DIRS[mode]
    d = 1
    path = []
    while True:
        LX = TX + (d*turret_dir[0])
        LY = TY + (d*turret_dir[1])
        if valid_move(LX, LY, M, N, MAP):
            path.append((LX, LY))
        else:
            break
        d += 1
    return path

def run(filename='sample3.in'):
    with open(filename) as f:
        T = int(f.readline())
        for t in xrange(0, T):
            M, N = [int(x) for x in f.readline().split(' ')]
            MAP = []
            S, G = (0, 0), (0, 0)
            TURRETS = {}
            for I in xrange(0, M):
                line = f.readline().replace('\n', '')
                for J in xrange(0, N):
                    if line[J] == 'S':
                        S = (I, J)
                    elif line[J] == 'G':
                        G = (I, J)
                    elif line[J] in TURRET_MODES:
                        TURRETS[(I,J)] = TURRET_MODES.index(line[J])
                MAP.append(line)
            LASER_PATHS = []
            for variation in xrange(0, 4):
                laser_paths = []
                for T in TURRETS:
                    initial_turret_mode = TURRETS[T]
                    turret_mode = (initial_turret_mode+variation)%4
                    laser_paths.extend(laser_path(T, turret_mode, M, N, MAP))
                LASER_PATHS.append(laser_paths)

            # print 'MAP'
            # for line in MAP:
            #     print line

            # for v, kill_paths in enumerate(LASER_PATHS):
            #     for X in xrange(0, M):
            #         line = []
            #         for Y in xrange(0, N):
            #             if (X, Y) in kill_paths:
            #                 line.append('*')
            #             elif (X, Y) in TURRETS:
            #                 line.append(TURRET_MODES[(TURRETS[(X,Y)]+v)%4])
            #             else:
            #                 line.append('.')
            #         print ''.join(line)
            #     print

            steps = min_steps(M, N, MAP, G, TURRETS, LASER_PATHS, S, 0, [], -1, {})
            if steps == -1:
                print 'Case %d: impossible' % (t+1)
            else:
                print 'Case %d: %d' % (t+1, steps)

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    filename = None
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run()
