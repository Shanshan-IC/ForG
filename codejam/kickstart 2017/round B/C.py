# -*- coding: utf-8 -*-

def gb(x, y, N, M):
    if a[x][y] == '.':
        return 0
    k = 0
    while x+k+1 < N and y-k-1 > 1 and y+k+1 < M:
        ok = True
        for j in xrange(y-k)

with open('B-large-practice.in', 'r') as f:
    with open('B-large.out', 'w+') as f_out:
        t = int(f.readline())
        for cas in xrange(t):
            inp = [int(i) for i in f.readline().split(' ')]
            N, M, K = inp[0], inp[1], inp[2]
            sz = [0 for i in xrange(107)]
            for i in xrange(1, 101):
                sz[i] = sz[i-1] + 2*i-1 # 已知树的高度，获得总的#个数
            a = []
            for i in xrange(N):
                a.append([int(i) for i in f.readline().split(' ')])

            for k in xrange(k):
                for i in xrange(N):
                    for j in xrange(M):




