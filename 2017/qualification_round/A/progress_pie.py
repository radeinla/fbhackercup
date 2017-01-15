import math

def slope(x1, y1, x2, y2):
    return y1-y2 / x1-x2

def angle(X, Y):
    angle1 = math.atan2(50-100, 50-50)
    angle2 = math.atan2(50-Y, 50-X)
    angle_between_radians = angle1-angle2
    deg = math.degrees(angle_between_radians)
    if deg < 0:
        deg = 360.0+deg
    return deg

def get_color(P, X, Y):
    if P == 0:
        return 'white'
    if X == 50 and Y == 50:
        return 'black'
    if math.sqrt((X - 50) ** 2 + (Y - (50)) ** 2) > 50:
        return 'white'
    if P == 100:
        return 'black'
    if X == 50 and Y > 50:
        return 'black'
    if X == 50 and Y < 50:
        if P >= 50:
            return 'black'
        else:
            return 'white'
    if Y == 50 and X > 50:
        if P >= 25:
            return 'black'
        else:
            return 'white'
    if Y == 50 and X < 50:
        if P <= 75:
            return 'black'
        else:
            return 'white'
    angle1 = math.atan2(50-100, 50-50)
    angle2 = math.atan2(50-Y, 50-X)
    deg = angle(X, Y)
    P = (P * 360.0) / 100
    if P >= deg:
        return 'black'
    else:
        return 'white'

import sys
filename = None
if len(sys.argv) == 2:
    filename = sys.argv[1]

with open(filename or 'problem1.in') as file:
    T = int(file.readline())
    for t in xrange(1, T+1):
        P, X, Y = (int(s) for s in file.readline().strip().split(' '))
        color = get_color(P, X, Y)
        print "Case #{}: {}".format(t, color)
        