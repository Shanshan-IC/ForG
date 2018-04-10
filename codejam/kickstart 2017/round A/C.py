# -*- coding: utf-8 -*-

'''
给你若干个星球，每个星球在(x,y,z)，半径为r
现在让你用两个边长为r的正方体来覆盖，要求每个星球都至少被一个正方体完全包含
问r的最小值

分别考虑x,y,z的最小值，最优解肯定至少有一个立方体边界由这三个最小值确定

又因为有三个最小值只有两个正方体，所以至少有一个正方体的边界是由两个最小值确定的

那么我们枚举哪两维确定，然后枚举剩下一维的起点。再二分边长r贪心验证是否可行即可
'''



def cover(xs, xe, ys, ye, zs, ze, balls):
    e = xe - xs
    q = len(balls)
    vs = [0 for _ in xrange(q)]
    for i in xrange(q):
        if balls[i][0]-balls[i][3] >= xs and balls[i][0]+balls[i][3] <= xe \
            and balls[i][1]-balls[i][3] >= ys and balls[i][1]+balls[i][3] <= ye \
            and balls[i][2]-balls[i][3] >= zs and balls[i][2]+balls[i][3] <= ze:
            vs[i] = 1
    minx = miny = minz = 300000000
    maxx = maxy = maxz = -300000000
    for i in xrange(q):
        if not vs[i]:
            minx = min(minx, balls[i][0]-balls[i][3])
            maxx = max(maxx, balls[i][0]+ balls[i][3])
            miny = min(miny, balls[i][1] - balls[i][3])
            maxy = max(maxy, balls[i][1] + balls[i][3])
            minz = min(minz, balls[i][2] - balls[i][3])
            maxz = max(maxz, balls[i][2] + balls[i][3])
    if maxx-minx <= e and maxy-miny <= e and maxz-minz <= e:
        return True
    return False

def solve(balls):
    minx = miny = minz = 300000000
    maxx = maxy = maxz = -300000000
    for ball in balls:
        minx = min(minx, ball[0]-ball[3])
        maxx = max(maxx, ball[0]+ball[3])
        miny = min(miny, ball[1] - ball[3])
        maxy = max(maxy, ball[1] + ball[3])
        minz = min(minz, ball[2] - ball[3])
        maxz = max(maxz, ball[2] + ball[3])

    # 用二分法
    rs, re = 0, 500000000
    while rs < re:
        r = (rs+re) / 2
        if cover(minx, minx+r, miny, miny+r, minz, minz+r, balls) \
                or cover(minx, minx+r, miny, miny+r, maxz-r, maxz, balls) \
                or cover(minx, minx+r, maxy-r, maxy, minz, minz+r, balls) \
                or cover(minx, minx+r, maxy-r, maxy, maxz-r, maxz, balls) \
                or cover(maxx-r, maxx, miny, miny+r, minz, minz+r, balls) \
                or cover(maxx-r, maxx, miny, miny+r, maxz-r, maxz, balls) \
                or cover(maxx-r, maxx, maxy-r, maxy, minz, minz+r, balls) \
                or cover(maxx-r, maxx, maxy-r, maxy, maxz-r, maxz, balls):
            re = r
        else:
            rs = r + 1
    return rs

with open('C-large-practice.in', 'r') as f:
    with open('C-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            q = int(f.readline())
            balls = []
            for i in xrange(q):
                ball = [int(ss) for ss in f.readline().split(' ')]
                balls.append(ball)
            f_out.write('Case #%d: %d\n' % (cas+1, solve(balls)))