from operator import attrgetter
from itertools import groupby


class Player(object):
    def __init__(self, input):
        self.name = input[0]
        self.sp = int(input[1])
        self.h = int(input[2])
        self.p = 0
        self.playing = False
        self.draft = None

    def __repr__(self):
        return str((self.name, self.p, self.sp, self.h))


class Team(object):
    def __init__(self, P):
        self.field = []
        self.bench = []
        self.P = P

    def add(self, player):
        if len(self.field) < P:
            self.field.append(player)
        else:
            self.bench.append(player)

    def play(self):
        for p in self.field:
            p.p = p.p + 1
        self.sub()

    def sub(self):
        self.bench.append(self.field.pop(0))
        self.field.append(self.bench.pop(0))
        sorted(self.bench, key=bench_sort_score)
        sorted(self.field, key=field_sort_score)    


def bench_sort_score(p):
    return p.p*2640+(100-p.sp)*240+(240-p.h)


def field_sort_score(p):
    return (120-p.p)*2640+(p.sp)*240+(p.h)


def current(N, M, P, players):
    picks = sorted(players, key=bench_sort_score)

    # print picks

    teams = [Team(P), Team(P)]

    for i in xrange(0, N):
        picks[i].draft = i
        teams[i%2].add(picks[i])

    for i in xrange(0, M):
        # print '%d minute' % i
        for j in xrange(0, len(teams)):
            # print "team %d:" % j
            team = teams[j]
            team.play()
            # print 'field'
            # print team.field
            # print 'field'
            # print team.bench

    return sorted(teams[0].field + teams[1].field, key=lambda p: p.name)


with open("input2.txt") as f:
    T = int(f.readline())
    for t in xrange(0, T):
        N, M, P = [int(x) for x in f.readline().rstrip('\n').split(" ")]
        players = []
        for i in xrange(0, N):
            players.append(Player(f.readline().rstrip('\n').split(' ')))
        print ("Case #%d: %s" % (t+1, " ".join(map(lambda p: p.name, current(N, M, P, players)))))
